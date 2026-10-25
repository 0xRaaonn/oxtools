#!/usr/bin/env python3
"""Read-only image triage with Python's standard library and optional allowed tools.

Usage: python image_triage.py IMAGE [--output DIRECTORY] [--deep] [--no-wsl]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import mmap
import os
from pathlib import Path
import re
import shutil
import struct
import subprocess
import sys
from datetime import datetime
import zlib


MAGIC = {
    "PNG": b"\x89PNG\r\n\x1a\n",
    "JPEG": b"\xff\xd8\xff",
    "GIF87a": b"GIF87a",
    "GIF89a": b"GIF89a",
    "BMP": b"BM",
    "PDF": b"%PDF-",
    "ZIP": b"PK\x03\x04",
    "7z": b"7z\xbc\xaf\x27\x1c",
    "gzip": b"\x1f\x8b\x08",
    "XZ": b"\xfd7zXZ\x00",
    "ELF": b"\x7fELF",
    "PE/MZ": b"MZ",
    "SQLite": b"SQLite format 3\x00",
}
IMAGE_EXTENSIONS = {
    "PNG": {".png"},
    "JPEG": {".jpg", ".jpeg", ".jpe"},
    "GIF": {".gif"},
    "BMP": {".bmp", ".dib"},
    "WEBP": {".webp"},
    "TIFF": {".tif", ".tiff"},
    "SVG": {".svg"},
    "AVIF": {".avif"},
    "HEIC": {".heic", ".heif"},
}
FLAG_RE = re.compile(rb"(?:flag|ctf|picoctf|htb)\{[^\r\n}]{1,160}\}", re.I)
ASCII_RE = re.compile(rb"[\x20-\x7e]{8,4096}")
UTF16_RE = re.compile(rb"(?:[\x20-\x7e]\x00){8,2048}")
BASE64_RE = re.compile(rb"(?<![A-Za-z0-9+/=_-])[A-Za-z0-9+/_-]{24,4096}={0,2}(?![A-Za-z0-9+/=_-])")


def fmt_offset(value: int) -> str:
    return f"{value} (0x{value:x})"


def safe_text(data: bytes, limit: int = 180) -> str:
    value = data[:limit].decode("utf-8", "replace")
    return "".join(c if c.isprintable() else " " for c in value)


def hash_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


class Report:
    def __init__(self, image: Path, output: Path, size: int, max_scan: int):
        self.image = image
        self.output = output
        self.size = size
        self.max_scan = max_scan
        self.kind = "Unknown"
        self.details: dict[str, object] = {}
        self.findings: list[dict[str, object]] = []
        self.tools: list[dict[str, object]] = []
        self.end: int | None = None

    def add(self, level: str, title: str, detail: str, offset: int | None = None):
        item: dict[str, object] = {"level": level, "title": title, "detail": detail}
        if offset is not None:
            item["offset"] = offset
        self.findings.append(item)


def detect_kind(data: mmap.mmap) -> str:
    head = data[:64]
    if head.startswith(MAGIC["PNG"]):
        return "PNG"
    if head.startswith(MAGIC["JPEG"]):
        return "JPEG"
    if head.startswith((MAGIC["GIF87a"], MAGIC["GIF89a"])):
        return "GIF"
    if head.startswith(MAGIC["BMP"]):
        return "BMP"
    if head.startswith((b"II*\x00", b"MM\x00*")):
        return "TIFF"
    if head.startswith(b"RIFF") and head[8:12] == b"WEBP":
        return "WEBP"
    if len(head) >= 12 and head[4:8] == b"ftyp":
        brand = head[8:12]
        if brand in (b"avif", b"avis", b"mif1", b"miaf"):
            return "AVIF"
        if brand in (b"heic", b"heix", b"hevc", b"hevx", b"heim", b"heis", b"heif"):
            return "HEIC"
    stripped = head.lstrip(b"\xef\xbb\xbf \t\r\n")
    if stripped.startswith((b"<svg", b"<?xml")) and b"<svg" in data[:4096]:
        return "SVG"
    return "Unknown"


def parse_png(data: mmap.mmap, rep: Report):
    pos = 8
    chunks: list[str] = []
    n = len(data)
    count = 0
    while pos + 12 <= n and count < 100000:
        count += 1
        length = struct.unpack_from(">I", data, pos)[0]
        name = data[pos + 4:pos + 8]
        stop = pos + 12 + length
        if stop > n:
            rep.add("warning", "Truncated PNG chunk", f"{safe_text(name)} declares {length} bytes beyond file end", pos)
            break
        content = memoryview(data)[pos + 8:pos + 8 + length]
        stored_crc = struct.unpack_from(">I", data, pos + 8 + length)[0]
        computed_crc = zlib.crc32(name)
        computed_crc = zlib.crc32(content, computed_crc) & 0xFFFFFFFF
        label = name.decode("ascii", "replace")
        chunks.append(label)
        if stored_crc != computed_crc:
            rep.add("warning", "PNG CRC mismatch", f"Chunk {label}: stored {stored_crc:08x}, computed {computed_crc:08x}", pos)
        if name == b"IHDR" and length >= 13:
            width, height, depth, color = struct.unpack_from(">IIBB", content)
            rep.details.update(width=width, height=height, bit_depth=depth, color_type=color)
        if name in (b"tEXt", b"iTXt", b"zTXt"):
            preview = safe_text(bytes(content[:240]), 240)
            rep.add("lead", f"PNG {label} metadata", preview, pos)
            text_chunk = bytes(content[:min(len(content), 1_000_000)])
            if name == b"zTXt" and b"\x00" in text_chunk:
                try:
                    after_key = text_chunk.split(b"\x00", 1)[1]
                    if after_key[:1] == b"\x00":
                        decoder = zlib.decompressobj()
                        text = decoder.decompress(after_key[1:], 4096)
                        rep.add("lead", "Decompressed zTXt preview", safe_text(text), pos)
                except zlib.error:
                    rep.add("warning", "zTXt decompression failed", "The text chunk may be damaged or use unexpected data", pos)
            if name == b"iTXt" and b"\x00" in text_chunk:
                try:
                    keyword, after_key = text_chunk.split(b"\x00", 1)
                    compressed = after_key[0] == 1
                    language_and_text = after_key[2:]
                    language, after_language = language_and_text.split(b"\x00", 1)
                    translated, text = after_language.split(b"\x00", 1)
                    if compressed:
                        decoder = zlib.decompressobj()
                        text = decoder.decompress(text, 4096)
                    rep.add("lead", "Decoded iTXt preview", f"{safe_text(keyword)}: {safe_text(text)}", pos)
                except (IndexError, ValueError, zlib.error):
                    rep.add("warning", "iTXt parsing failed", "The international text chunk may be damaged", pos)
        if name not in {
            b"IHDR", b"PLTE", b"IDAT", b"IEND", b"tEXt", b"zTXt", b"iTXt",
            b"gAMA", b"sRGB", b"iCCP", b"pHYs", b"tIME", b"bKGD", b"tRNS",
            b"sBIT", b"hIST", b"sPLT", b"eXIf", b"acTL", b"fcTL", b"fdAT",
            b"cHRM", b"sTER", b"vpAg",
        }:
            rep.add("lead", "Unusual PNG chunk", f"{label}, {length} bytes; preview: {safe_text(bytes(content[:60]), 60)}", pos)
        if name == b"acTL":
            rep.add("info", "Animated PNG", "acTL chunk indicates animation; inspect frames individually", pos)
        if name == b"IEND":
            rep.end = stop
            break
        pos = stop
    rep.details["png_chunks"] = chunks[:200]
    if count >= 100000:
        rep.add("warning", "PNG chunk limit reached", "Stopped after 100000 chunks")
    if rep.end is None:
        rep.add("warning", "No complete PNG IEND", "Could be truncated, malformed, or parser-limited")


def parse_jpeg(data: mmap.mmap, rep: Report):
    n = len(data)
    pos = 2
    markers: list[str] = []
    segment_count = 0
    while pos < n and segment_count < 100000:
        if data[pos] != 0xFF:
            rep.add("warning", "Unexpected JPEG byte", "Expected a marker outside entropy-coded data", pos)
            break
        marker_start = pos
        while pos < n and data[pos] == 0xFF:
            pos += 1
        if pos >= n:
            break
        marker = data[pos]
        pos += 1
        segment_count += 1
        markers.append(f"FF{marker:02X}")
        if marker == 0xD9:
            rep.end = pos
            break
        if marker in range(0xD0, 0xD8) or marker == 0x01:
            continue
        if pos + 2 > n:
            break
        length = struct.unpack_from(">H", data, pos)[0]
        if length < 2 or pos + length > n:
            rep.add("warning", "Bad JPEG segment length", f"Marker FF{marker:02X} length {length}", marker_start)
            break
        if marker == 0xFE:
            rep.add("lead", "JPEG comment", safe_text(data[pos + 2:pos + length]), marker_start)
        if marker in (0xC0, 0xC1, 0xC2, 0xC3) and length >= 7:
            height, width = struct.unpack_from(">HH", data, pos + 3)
            rep.details.update(width=width, height=height)
        pos += length
        if marker == 0xDA:
            while pos < n:
                ff = data.find(b"\xff", pos)
                if ff < 0 or ff + 1 >= n:
                    pos = n
                    break
                next_byte = data[ff + 1]
                if next_byte == 0x00 or next_byte in range(0xD0, 0xD8):
                    pos = ff + 2
                    continue
                pos = ff
                break
    rep.details["jpeg_markers"] = markers[:200]
    if rep.end is None:
        rep.add("warning", "No complete JPEG EOI", "Image may be truncated or use unsupported marker structure")


def skip_gif_subblocks(data: mmap.mmap, pos: int) -> int | None:
    n = len(data)
    while pos < n:
        length = data[pos]
        pos += 1
        if length == 0:
            return pos
        pos += length
        if pos > n:
            return None
    return None


def parse_gif(data: mmap.mmap, rep: Report):
    n = len(data)
    if n < 13:
        rep.add("warning", "Truncated GIF header", "Need at least 13 bytes")
        return
    width, height = struct.unpack_from("<HH", data, 6)
    rep.details.update(width=width, height=height)
    packed = data[10]
    pos = 13 + (3 * (1 << ((packed & 7) + 1)) if packed & 0x80 else 0)
    frames = 0
    blocks = 0
    while pos < n and blocks < 100000:
        blocks += 1
        kind = data[pos]
        pos += 1
        if kind == 0x3B:
            rep.end = pos
            break
        if kind == 0x21:
            if pos >= n:
                break
            label = data[pos]
            pos += 1
            start = pos
            pos = skip_gif_subblocks(data, pos)
            if pos is None:
                break
            if label == 0xFE:
                rep.add("lead", "GIF comment extension", safe_text(data[start:pos]), start - 2)
            continue
        if kind == 0x2C:
            if pos + 9 > n:
                break
            frames += 1
            local_packed = data[pos + 8]
            pos += 9
            if local_packed & 0x80:
                pos += 3 * (1 << ((local_packed & 7) + 1))
            if pos >= n:
                break
            pos += 1  # LZW minimum code size
            pos = skip_gif_subblocks(data, pos)
            if pos is None:
                break
            continue
        rep.add("warning", "Unexpected GIF block", f"Byte 0x{kind:02x}", pos - 1)
        break
    rep.details["gif_frames"] = frames
    if frames > 1:
        rep.add("lead", "Multiple GIF frames", f"{frames} image frames; inspect each one")
    if rep.end is None:
        rep.add("warning", "No complete GIF trailer", "Could be truncated or malformed")


def parse_bmp(data: mmap.mmap, rep: Report):
    if len(data) < 26:
        rep.add("warning", "Truncated BMP header", "Need at least 26 bytes")
        return
    declared = struct.unpack_from("<I", data, 2)[0]
    pixel_start = struct.unpack_from("<I", data, 10)[0]
    dib_size = struct.unpack_from("<I", data, 14)[0]
    rep.details.update(declared_size=declared, pixel_offset=pixel_start, dib_header_size=dib_size)
    if dib_size >= 40 and len(data) >= 30:
        width, height = struct.unpack_from("<ii", data, 18)
        rep.details.update(width=width, height=height)
    if 26 <= declared <= len(data):
        rep.end = declared
    elif declared > len(data):
        rep.add("warning", "BMP file size exceeds actual size", f"Declared {declared}, actual {len(data)}")


def parse_webp(data: mmap.mmap, rep: Report):
    if len(data) < 12:
        return
    declared = struct.unpack_from("<I", data, 4)[0] + 8
    rep.details["riff_declared_size"] = declared
    if 12 <= declared <= len(data):
        rep.end = declared
    else:
        rep.add("warning", "Invalid WebP RIFF size", f"Declared {declared}, actual {len(data)}")
    pos = 12
    chunks = []
    stop = min(declared, len(data))
    while pos + 8 <= stop and len(chunks) < 10000:
        name = data[pos:pos + 4].decode("ascii", "replace")
        size = struct.unpack_from("<I", data, pos + 4)[0]
        chunks.append(name)
        if name in ("EXIF", "XMP "):
            rep.add("lead", f"WebP {name.strip()} chunk", f"{size} metadata bytes", pos)
        pos += 8 + size + (size & 1)
    rep.details["webp_chunks"] = chunks[:200]


def parse_bmff(data: mmap.mmap, rep: Report):
    pos = 0
    boxes = []
    n = len(data)
    while pos + 8 <= n and len(boxes) < 10000:
        size = struct.unpack_from(">I", data, pos)[0]
        name = data[pos + 4:pos + 8].decode("ascii", "replace")
        header = 8
        if size == 1:
            if pos + 16 > n:
                break
            size = struct.unpack_from(">Q", data, pos + 8)[0]
            header = 16
        elif size == 0:
            size = n - pos
        if size < header or pos + size > n:
            rep.add("warning", "Invalid BMFF box", f"{name} size {size}", pos)
            break
        boxes.append(name)
        pos += size
    rep.details["top_level_boxes"] = boxes[:200]
    if pos == n:
        rep.end = n
    elif pos > 0:
        rep.add("lead", "Bytes after BMFF boxes", f"Unparsed data starts at {fmt_offset(pos)}", pos)


def inspect_structure(data: mmap.mmap, rep: Report):
    rep.kind = detect_kind(data)
    ext = rep.image.suffix.lower()
    expected = IMAGE_EXTENSIONS.get(rep.kind, set())
    if expected and ext not in expected:
        rep.add("lead", "Extension differs from format", f"Named {ext or '(none)'}, header indicates {rep.kind}")
    if rep.kind == "Unknown":
        rep.add("warning", "Unrecognized image header", "External metadata tools may identify a newer or damaged format")
    if rep.kind == "PNG":
        parse_png(data, rep)
    elif rep.kind == "JPEG":
        parse_jpeg(data, rep)
    elif rep.kind == "GIF":
        parse_gif(data, rep)
    elif rep.kind == "BMP":
        parse_bmp(data, rep)
    elif rep.kind == "WEBP":
        parse_webp(data, rep)
    elif rep.kind in ("AVIF", "HEIC"):
        parse_bmff(data, rep)
    elif rep.kind == "SVG":
        sample = data[:min(len(data), 1024 * 1024)].lower()
        if b"<script" in sample:
            rep.add("lead", "SVG script element", "Inspect the XML; SVG can contain active content")
        if b"data:" in sample and b"base64," in sample:
            rep.add("lead", "SVG data URI", "Embedded Base64 data may be an image, font, or other object")
    if rep.end is not None and rep.end < rep.size:
        trailing = rep.size - rep.end
        rep.add("lead", "Data after image end", f"{trailing} bytes start at {fmt_offset(rep.end)}", rep.end)
        if trailing <= 64 * 1024 * 1024:
            out = rep.output / "trailing_bytes.bin"
            out.write_bytes(data[rep.end:])
            rep.details["trailing_file"] = str(out)
        else:
            rep.add("info", "Trailing data not carved", "More than 64 MiB; inspect offset manually")


def inspect_bytes(data: mmap.mmap, rep: Report):
    length = min(rep.size, rep.max_scan)
    if length < rep.size:
        rep.add("info", "Byte scan capped", f"Scanned first {length} of {rep.size} bytes; structure scan used whole file")
    entropy_sample = data[:min(rep.size, 1024 * 1024)]
    if entropy_sample:
        counts = [0] * 256
        for byte in entropy_sample:
            counts[byte] += 1
        entropy = -sum((count / len(entropy_sample)) * math.log2(count / len(entropy_sample)) for count in counts if count)
        rep.details["first_mib_entropy_bits_per_byte"] = round(entropy, 3)
    hits = []
    for label, signature in MAGIC.items():
        pos = 0
        per_type = 0
        while per_type < 12:
            found = data.find(signature, pos, length)
            if found < 0:
                break
            if found > 0:
                hits.append({"type": label, "offset": found})
            per_type += 1
            pos = found + 1
    hits.sort(key=lambda item: item["offset"])
    rep.details["embedded_signature_candidates"] = hits[:100]
    if hits:
        preview = ", ".join(f"{x['type']}@{fmt_offset(x['offset'])}" for x in hits[:12])
        rep.add("lead", "Embedded signature candidates", preview + (" ..." if len(hits) > 12 else ""))
    flag_hits = []
    for pattern, encoding in ((FLAG_RE, "ASCII/UTF-8"), (re.compile(rb"(?:f\x00l\x00a\x00g\x00|c\x00t\x00f\x00)\x00?\{\x00(?:[^}\x00]\x00){1,160}}\x00?", re.I), "UTF-16LE")):
        for match in pattern.finditer(data, 0, length):
            raw = match.group(0)
            text = raw.decode("utf-16le" if encoding == "UTF-16LE" else "utf-8", "replace")
            flag_hits.append({"offset": match.start(), "encoding": encoding, "text": text})
            if len(flag_hits) >= 50:
                break
    rep.details["flag_shaped_strings"] = flag_hits
    if flag_hits:
        rep.add("lead", "Flag-shaped byte strings", f"{len(flag_hits)} candidate(s); verify context and challenge format")
    strings = []
    for regex, encoding in ((ASCII_RE, "ASCII"), (UTF16_RE, "UTF-16LE")):
        seen = 0
        for match in regex.finditer(data, 0, length):
            seen += 1
            raw = match.group(0)
            text = raw.decode("utf-16le" if encoding == "UTF-16LE" else "ascii", "replace")
            if len(strings) < 300 and (len(text) >= 12 or "flag" in text.lower()):
                strings.append({"offset": match.start(), "encoding": encoding, "text": text[:240]})
            if seen >= 100000:
                rep.add("info", f"{encoding} string limit reached", "Stopped after 100000 matches")
                break
    rep.details["readable_strings"] = strings
    (rep.output / "strings.json").write_text(json.dumps(strings, indent=2, ensure_ascii=False), encoding="utf-8")
    base64 = []
    for match in BASE64_RE.finditer(data, 0, length):
        value = match.group(0)
        if len(value) > 4096:
            continue
        # Restrict to readable results or a recognizable binary header.
        import base64 as base64_module
        try:
            decoded = base64_module.b64decode(value.replace(b"-", b"+").replace(b"_", b"/") + b"===")
        except (ValueError, base64_module.binascii.Error):
            continue
        if len(decoded) < 8:
            continue
        recognizable = any(decoded.startswith(sig) for sig in MAGIC.values())
        readable = sum(32 <= x <= 126 or x in (9, 10, 13) for x in decoded) / len(decoded) > 0.85
        if recognizable or readable:
            base64.append({"offset": match.start(), "encoded": safe_text(value, 80), "decoded_preview": safe_text(decoded, 120)})
        if len(base64) >= 30:
            break
    rep.details["base64_candidates"] = base64
    if base64:
        rep.add("lead", "Plausible Base64 strings", f"{len(base64)} candidate(s), including metadata or incidental text")


def candidate_tools(image: Path, no_wsl: bool):
    names = ("exiftool", "binwalk", "zbarimg", "zsteg")
    found = {}
    for name in names:
        native = shutil.which(name)
        if name == "exiftool" and not native and os.name == "nt":
            native = shutil.which("exiftool(-k).exe")
        if native:
            found[name] = (native, str(image))
            continue
        if os.name == "nt" and not no_wsl and shutil.which("wsl.exe"):
            try:
                probe = subprocess.run(
                    ["wsl.exe", "--", "sh", "-lc", f"command -v {name}"],
                    capture_output=True, text=True, timeout=10, check=False,
                )
                mapped = subprocess.run(
                    ["wsl.exe", "--", "wslpath", "-a", "-u", str(image)],
                    capture_output=True, text=True, timeout=10, check=False,
                )
                if probe.returncode == 0 and mapped.returncode == 0 and mapped.stdout.strip():
                    found[name] = (["wsl.exe", "--", name], mapped.stdout.strip())
                    continue
            except (OSError, subprocess.TimeoutExpired):
                pass
        found[name] = None
    return found


def run_tool(name: str, tool, args: list[str], rep: Report, timeout: int):
    if tool is None:
        rep.tools.append({"name": name, "status": "not installed", "note": "Skipped; core Python checks still ran"})
        return
    executable, path = tool
    prefix = executable if isinstance(executable, list) else [executable]
    command = prefix + args + [path]
    try:
        done = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout, check=False)
        stdout = done.stdout[:2_000_000].decode("utf-8", "replace")
        stderr = done.stderr[:100_000].decode("utf-8", "replace")
        output_path = rep.output / f"{name}.txt"
        output_path.write_text(stdout + ("\n[stderr]\n" + stderr if stderr else ""), encoding="utf-8")
        status = "completed" if done.returncode == 0 else f"exit {done.returncode}"
        if name == "zbarimg" and done.returncode != 0 and not stdout.strip():
            status = "no barcode decoded"
        rep.tools.append({
            "name": name, "status": status,
            "command": command, "output_file": str(output_path),
            "stdout_preview": stdout[:1200], "stderr_preview": stderr[:400],
            "truncated": len(done.stdout) > 2_000_000,
        })
        if name == "zbarimg" and stdout.strip():
            rep.add("lead", "Barcode/QR result", safe_text(done.stdout, 300))
        if name == "zsteg":
            interesting = [line for line in stdout.splitlines() if ".. text:" in line or ".. file:" in line or ".. zlib:" in line]
            if interesting:
                rep.add("lead", "zsteg candidate channels", "; ".join(interesting[:6])[:600])
        if name == "binwalk" and any(line.strip()[:1].isdigit() for line in stdout.splitlines()):
            rep.add("lead", "binwalk signature results", "Inspect binwalk.txt and validate candidate offsets")
        for match in FLAG_RE.finditer(done.stdout[:2_000_000]):
            rep.add("lead", f"Flag-shaped string in {name} output", safe_text(match.group(0), 180))
    except subprocess.TimeoutExpired:
        rep.tools.append({"name": name, "status": f"timed out after {timeout}s"})
    except OSError as exc:
        rep.tools.append({"name": name, "status": "failed", "error": str(exc)})


def write_report(rep: Report, sha256: str):
    payload = {
        "input": str(rep.image), "size": rep.size, "sha256": sha256,
        "detected_format": rep.kind, "structure_end": rep.end,
        "details": rep.details, "findings": rep.findings, "tools": rep.tools,
    }
    (rep.output / "report.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    lines = [
        "# Image triage report", "",
        f"- Input: `{rep.image}`",
        f"- Size: {rep.size} bytes",
        f"- SHA-256: `{sha256}`",
        f"- Detected format: **{rep.kind}**",
        f"- Structure end: {fmt_offset(rep.end) if rep.end is not None else 'unknown'}",
        f"- Dimensions: {rep.details.get('width', '?')} × {rep.details.get('height', '?')}",
        "",
        "## Findings", "",
    ]
    if rep.findings:
        for item in rep.findings:
            offset = f" at {fmt_offset(item['offset'])}" if "offset" in item else ""
            lines.append(f"- **{item['level'].upper()} — {item['title']}**{offset}: {item['detail']}")
    else:
        lines.append("- No suspicious indicators found by these checks.")
    candidates = rep.details.get("flag_shaped_strings", [])
    if candidates:
        lines += ["", "## Flag-shaped strings", ""]
        for item in candidates[:20]:
            value = str(item["text"]).replace("`", "'").replace("\n", " ").replace("\r", " ")
            lines.append(f"- {fmt_offset(item['offset'])} ({item['encoding']}): `{value}`")
    base64 = rep.details.get("base64_candidates", [])
    if base64:
        lines += ["", "## Plausible Base64 previews", ""]
        for item in base64[:10]:
            preview = str(item["decoded_preview"]).replace("`", "'").replace("\n", " ").replace("\r", " ")
            lines.append(f"- {fmt_offset(item['offset'])}: decoded preview `{preview}`")
    strings = rep.details.get("readable_strings", [])
    interesting = [
        item for item in strings
        if any(word in str(item["text"]).lower() for word in ("flag", "ctf", "secret", "password", "http", "key"))
    ]
    if interesting:
        lines += ["", "## Notable readable strings", ""]
        for item in interesting[:20]:
            value = str(item["text"]).replace("`", "'").replace("\n", " ").replace("\r", " ")
            lines.append(f"- {fmt_offset(item['offset'])} ({item['encoding']}): `{value}`")
    lines += ["", "## Optional tools", ""]
    for item in rep.tools:
        lines.append(f"- **{item['name']}**: {item['status']}" + (f"; output: `{item['output_file']}`" if "output_file" in item else ""))
    lines += [
        "", "## Interpretation", "",
        "A finding is a lead, not proof of hidden data. Image compression and metadata can create false signature, entropy, text, and Base64 hits. Validate extracted bytes with the relevant file parser and the challenge prompt.",
        f"First-MiB Shannon entropy: {rep.details.get('first_mib_entropy_bits_per_byte', 'n/a')} bits/byte. High entropy is common in compressed images and does not by itself show encryption or steganography.",
        "This script cannot guarantee detection of every steganography method, encrypted payload, or proprietary format. Zsteg is used only for PNG/BMP; other image formats receive format/metadata/embedded-data checks.",
        "", "See `report.json`, `strings.json`, and optional-tool text files for details.",
    ]
    (rep.output / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def unique_output(base: Path) -> Path:
    if not base.exists():
        return base
    for number in range(2, 10000):
        candidate = Path(f"{base}_{number}")
        if not candidate.exists():
            return candidate
    raise RuntimeError("Could not choose a unique output directory")


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect one image for CTF-relevant metadata, structure, embedded data, and optional steganography/barcodes.")
    parser.add_argument("image", type=Path, help="Image file to inspect")
    parser.add_argument("--output", type=Path, help="Output directory (default: new folder beside the image)")
    parser.add_argument("--deep", action="store_true", help="Use zsteg --all and scan up to 1 GiB instead of 256 MiB")
    parser.add_argument("--no-wsl", action="store_true", help="Do not use WSL tools when launched from Windows")
    args = parser.parse_args()
    image = args.image.expanduser().resolve()
    if not image.is_file():
        parser.error(f"Not a file: {image}")
    size = image.stat().st_size
    if size == 0:
        parser.error("Input is empty")
    target = args.output.expanduser().resolve() if args.output else image.parent / f"{image.stem}_triage_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    target = unique_output(target)
    target.mkdir(parents=True)
    rep = Report(image, target, size, (1024 if args.deep else 256) * 1024 * 1024)
    sha256 = hash_file(image)
    with image.open("rb") as stream, mmap.mmap(stream.fileno(), 0, access=mmap.ACCESS_READ) as data:
        inspect_structure(data, rep)
        inspect_bytes(data, rep)
    tools = candidate_tools(image, args.no_wsl)
    run_tool("exiftool", tools["exiftool"], ["-a", "-G1", "-s"], rep, 45)
    run_tool("binwalk", tools["binwalk"], [], rep, 60)
    run_tool("zbarimg", tools["zbarimg"], ["--raw", "--quiet"], rep, 30)
    if rep.kind in ("PNG", "BMP"):
        run_tool("zsteg", tools["zsteg"], ["-a"] if args.deep else [], rep, 90 if args.deep else 45)
    else:
        rep.tools.append({"name": "zsteg", "status": "skipped", "note": "Only appropriate for PNG/BMP"})
    write_report(rep, sha256)
    print(f"Input: {image}")
    print(f"Format: {rep.kind}; size: {size} bytes")
    print(f"Findings: {len(rep.findings)}; optional tools available: {sum(x['status'] != 'not installed' and x['status'] != 'skipped' for x in rep.tools)}")
    print(f"Report: {target / 'report.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

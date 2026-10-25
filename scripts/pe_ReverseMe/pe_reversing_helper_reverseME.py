#!/usr/bin/env python3
"""Inspect a Windows PE CTF challenge without running the executable.

Handles ZIP passwords, UPX files with renamed UPX0/UPX1 sections, and the
split-key / XOR-output pattern used by ReverseMe. Other challenges still get
an unpacked binary and a short list of useful strings for manual analysis.

Dependencies: pip install pefile capstone; install the `upx` command.
"""

import argparse
import pathlib
import re
import shutil
import subprocess
import tempfile
import zipfile

try:
    import pefile
    from capstone import Cs, CS_ARCH_X86, CS_MODE_32
    from capstone.x86 import X86_OP_IMM, X86_OP_MEM, X86_OP_REG, X86_REG_EBP, X86_REG_EDX
except ImportError as exc:
    raise SystemExit("Install dependencies with: python3 -m pip install pefile capstone") from exc


def choose_input(path, member, password):
    if path.suffix.lower() != ".zip":
        return path.read_bytes(), path.stem
    with zipfile.ZipFile(path) as archive:
        names = [n for n in archive.namelist() if n.lower().endswith(".exe")]
        if member:
            if member not in archive.namelist():
                raise ValueError(f"ZIP member not found: {member}")
            chosen = member
        elif len(names) == 1:
            chosen = names[0]
        else:
            raise ValueError("Select an executable with --member; ZIP contains: " + ", ".join(names))
        try:
            data = archive.read(chosen, pwd=password.encode() if password else None)
        except RuntimeError as exc:
            raise ValueError("ZIP password required or incorrect; pass --password") from exc
        return data, pathlib.PurePosixPath(chosen).stem


def renamed_upx(data):
    """Change only the first two PE section names, using parsed offsets."""
    if b"UPX!" not in data:
        return None
    pe = pefile.PE(data=data, fast_load=True)
    if len(pe.sections) < 2:
        return None
    if pe.sections[0].Name.rstrip(b"\0") == b"UPX0" and pe.sections[1].Name.rstrip(b"\0") == b"UPX1":
        return None
    result = bytearray(data)
    for section, name in zip(pe.sections[:2], (b"UPX0", b"UPX1")):
        offset = section.get_file_offset()
        result[offset:offset + 8] = name.ljust(8, b"\0")
    return bytes(result)


def unpack(data):
    if not shutil.which("upx"):
        print("[!] upx unavailable; inspecting original executable")
        return data, False
    with tempfile.TemporaryDirectory(prefix="ctf-pe-") as directory:
        source = pathlib.Path(directory) / "input.exe"
        target = pathlib.Path(directory) / "unpacked.exe"
        for candidate, label in ((data, "original"), (renamed_upx(data), "restored UPX sections")):
            if candidate is None:
                continue
            source.write_bytes(candidate)
            result = subprocess.run(
                ["upx", "-d", str(source), "-o", str(target)],
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
            )
            if result.returncode == 0 and target.is_file():
                print(f"[+] Unpacked with {label}")
                return target.read_bytes(), True
        print("[!] UPX did not unpack this file; inspecting original executable")
        return data, False


def read_va(pe, address, limit=256):
    rva = address - pe.OPTIONAL_HEADER.ImageBase
    if rva < 0:
        return b""
    try:
        return pe.get_data(rva, limit)
    except (pefile.PEFormatError, ValueError):
        return b""


def ascii_at(pe, address, limit=128):
    raw = read_va(pe, address, limit).split(b"\0", 1)[0]
    if len(raw) < 3 or any(c < 32 or c > 126 for c in raw):
        return None
    return raw


def instructions(pe):
    decoder = Cs(CS_ARCH_X86, CS_MODE_32)
    decoder.detail = True
    base = pe.OPTIONAL_HEADER.ImageBase
    for section in pe.sections:
        if not (section.Characteristics & 0x20000000):
            continue
        code = section.get_data()
        yield from decoder.disasm(code, base + section.VirtualAddress)


def stack_address(operand):
    if operand.type == X86_OP_MEM and operand.mem.base == X86_REG_EBP and operand.mem.index == 0:
        return operand.mem.disp
    return None


def recover_key(pe, code):
    """Find copied input words and their later string comparisons."""
    starts = [0]
    for index in range(len(code) - 1):
        if (code[index].mnemonic == "push" and code[index].op_str == "ebp"
                and code[index + 1].mnemonic == "mov"
                and code[index + 1].op_str == "ebp, esp"):
            starts.append(index)
    starts.append(len(code))

    for begin, end in zip(starts, starts[1:]):
        function = code[begin:end]
        stack_to_input = {}
        sources = {}
        for ins in function:
            ops = ins.operands
            if ins.mnemonic != "mov" or len(ops) != 2:
                continue
            dst, src = ops
            if dst.type == X86_OP_REG:
                if src.type == X86_OP_MEM and src.mem.base == X86_REG_EDX and src.mem.index == 0:
                    sources[dst.reg] = (src.mem.disp, ins.address)
                else:
                    sources.pop(dst.reg, None)
            elif src.type == X86_OP_REG:
                stack = stack_address(dst)
                source = sources.get(src.reg)
                if stack is not None and source and ins.address - source[1] <= 48:
                    stack_to_input[stack] = source[0]

        chunks = {}
        for index, ins in enumerate(function):
            ops = ins.operands
            if ins.mnemonic != "mov" or len(ops) != 2 or ops[1].type != X86_OP_IMM:
                continue
            word = ascii_at(pe, ops[1].imm)
            if word is None or not re.fullmatch(rb"[0-9a-fA-F]{4,16}", word):
                continue
            for next_ins in function[index + 1:index + 7]:
                if next_ins.mnemonic != "lea" or len(next_ins.operands) != 2:
                    continue
                stack = stack_address(next_ins.operands[1])
                if stack in stack_to_input:
                    chunks[stack_to_input[stack]] = word
                    break

        if len(chunks) < 3 or 0 not in chunks:
            continue
        length = max(offset + len(word) for offset, word in chunks.items())
        if length > 256:
            continue
        key = bytearray(length)
        seen = bytearray(length)
        conflict = False
        for offset, word in chunks.items():
            for index, byte in enumerate(word, offset):
                if seen[index] and key[index] != byte:
                    conflict = True
                key[index], seen[index] = byte, 1
        if not conflict and all(seen):
            return bytes(key), chunks
    return None, {}


def recover_xor_output(pe, code, key):
    """Find constant 16-byte blocks copied to the stack before an XOR loop."""
    for start in range(len(code)):
        block = code[start:start + 85]
        if not block or block[0].mnemonic not in ("movaps", "movdqa", "movups"):
            continue
        blocks = {}
        source = None
        for ins in block:
            ops = ins.operands
            if len(ops) != 2:
                continue
            if ins.mnemonic in ("movaps", "movdqa", "movups") and ops[0].type == X86_OP_REG and ops[1].type == X86_OP_MEM:
                address = ops[1].mem.disp
                raw = read_va(pe, address, 16)
                source = raw if len(raw) == 16 else None
            elif ins.mnemonic in ("movaps", "movdqa", "movups") and ops[0].type == X86_OP_MEM:
                stack = stack_address(ops[0])
                if stack is not None and source:
                    blocks[stack] = source
            if len(blocks) >= 2 and ins.mnemonic == "xor" and "ecx, eax" in ins.op_str:
                offsets = sorted(blocks)
                if any(b - a != 16 for a, b in zip(offsets, offsets[1:])):
                    break
                encrypted = b"".join(blocks[offset] for offset in offsets)
                decoded = bytes(byte ^ key[i % len(key)] for i, byte in enumerate(encrypted))
                if decoded and all(32 <= byte <= 126 for byte in decoded):
                    return decoded, ins.address
                break
    return None, None


def interesting_strings(pe):
    found = []
    for section in pe.sections:
        if not (section.Characteristics & 0x40000000):
            continue
        raw = section.get_data()
        for match in re.finditer(rb"[\x20-\x7e]{4,}", raw):
            value = match.group()
            if any(token in value.lower() for token in (b"flag", b"key", b"correct", b"usage", b"password", b"ctf", b"csg_")):
                found.append((pe.OPTIONAL_HEADER.ImageBase + section.VirtualAddress + match.start(), value))
    return found[:30]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=pathlib.Path, help="PE executable or ZIP containing one")
    parser.add_argument("--password", help="ZIP password")
    parser.add_argument("--member", help="ZIP member name when there are multiple executables")
    parser.add_argument("--output", type=pathlib.Path, help="directory for unpacked file")
    args = parser.parse_args()
    if not args.input.is_file():
        parser.error(f"file does not exist: {args.input}")
    try:
        data, stem = choose_input(args.input, args.member, args.password)
        pefile.PE(data=data, fast_load=True)
        unpacked, changed = unpack(data)
        pe = pefile.PE(data=unpacked)
    except (ValueError, pefile.PEFormatError, zipfile.BadZipFile) as exc:
        parser.error(str(exc))

    if changed:
        output = args.output or args.input.parent / f"{stem}_analysis"
        output.mkdir(parents=True, exist_ok=True)
        path = output / f"{stem}_unpacked.exe"
        path.write_bytes(unpacked)
        print(f"[+] Saved unpacked executable: {path}")

    print("[+] Interesting strings:")
    for address, value in interesting_strings(pe):
        print(f"    0x{address:08x}  {value.decode('ascii')}")

    if pe.FILE_HEADER.Machine != 0x14c:
        print("[!] Automatic key recovery currently supports 32-bit x86 PE files")
        return
    code = list(instructions(pe))
    key, chunks = recover_key(pe, code)
    if not key:
        print("[!] Split key pattern not found; inspect the executable manually")
        return
    print("[+] Recovered key pieces:")
    for offset, word in sorted(chunks.items()):
        print(f"    +0x{offset:02x}: {word.decode('ascii')}")
    print(f"[+] Key: {key.decode('ascii')}")
    decoded, address = recover_xor_output(pe, code, key)
    if decoded is None:
        print("[!] XOR output pattern not found; inspect the key's uses manually")
        return
    print(f"[+] XOR decoded text (loop at 0x{address:08x}): {decoded.decode('ascii')}")
    strings = [value for _, value in interesting_strings(pe)]
    opening = next((value for value in strings if value.endswith(b"{")), None)
    if opening:
        prefix = next((value for value in strings if value.endswith(b"_") and len(value) < 24), b"")
        print(f"[+] Possible flag: {(prefix + opening + decoded + b'}').decode('ascii')}")


if __name__ == "__main__":
    main()

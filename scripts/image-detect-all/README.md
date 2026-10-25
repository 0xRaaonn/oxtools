# Image Detect All

Run [image_triage.py](image_triage.py) with one image path. It uses **Python 3 standard library only** for its built-in checks and, when present, runs the allowed CLI tools ExifTool, binwalk, ZBar (`zbarimg`), and zsteg. It does not install packages, upload files, edit the input, execute the image, or automatically extract every binwalk hit.

The name is a convenience: no program can detect every hidden message in every image format. The report separates concrete structure facts from candidates that need checking.

## Requirements

- Python 3 (Windows or WSL). No Python packages are required.
- Optional allowed command-line tools: `exiftool`, `binwalk`, `zbarimg`, and `zsteg`. The script skips any that are unavailable.
- If the image is on a read-only location, use `--output` to select a writable report directory.

## Run it

**Windows PowerShell:**

```powershell
py -3 .\image-detect-all\image_triage.py "C:\CTF\mystery image.png"
```

**WSL:**

```bash
python3 /mnt/c/path/to/image-detect-all/image_triage.py "/mnt/c/CTF/mystery image.png"
```

Use the actual path to this script and image. If launched in Windows and a tool is missing natively, the script tries that tool through WSL if WSL has it. Run `--no-wsl` to disable that fallback. WSL itself must already be installed and configured. If a tool is absent everywhere, the report marks it **not installed** and continues.

Optional flags:

```text
--output DIRECTORY   choose a report folder; existing folders are never overwritten
--deep               use zsteg --all and scan up to 1 GiB of bytes
--no-wsl             use only native Windows tools when run in Windows
```

Without `--output`, a timestamped `<image-stem>_triage_...` folder appears beside the image. The script prints the location of `report.md`. It chooses a new folder if a name already exists, so previous reports are retained.

## What it checks

| Check | What it can reveal |
| --- | --- |
| SHA-256 and header | Exact file identity, format, extension mismatch |
| PNG chunks and CRCs | Text chunks, unusual chunks, animation, damage, data after IEND |
| JPEG segments | Comments, dimensions, damage, data after EOI |
| GIF blocks | Comments, frame count, bytes after trailer |
| BMP/WebP container lengths | Size mismatch and trailing data |
| AVIF/HEIC top-level boxes | Basic container layout and unparsed tail |
| SVG text | Script elements and Base64 data URIs |
| Embedded magic bytes | Candidate ZIP/PDF/image/archive/executable offsets |
| Readable strings | ASCII and UTF-16LE text, including flag-shaped patterns |
| Base64 patterns | Plausible encoded text or known file signatures |
| First-MiB entropy | A rough byte-distribution measure, **not** a steganography verdict |
| ExifTool | Metadata, timestamps, comments, GPS, thumbnails, format details |
| binwalk | Embedded file/compression signature candidates |
| ZBar | QR and other supported barcode contents |
| zsteg | PNG/BMP bit-plane/steganography candidates; `--deep` tries more methods |

## Output files

- `report.md`: short human-readable findings and tool availability.
- `report.json`: machine-readable details, offsets, candidates, and tool output paths.
- `strings.json`: sampled readable strings and offsets.
- `exiftool.txt`, `binwalk.txt`, `zbarimg.txt`, `zsteg.txt`: created only for tools that ran.
- `trailing_bytes.bin`: created when a supported format has up to 64 MiB of bytes after its known end.

An “embedded signature candidate” is **not** automatic proof of an embedded file: compressed image data can accidentally contain signature bytes. Validate a candidate by carving at its offset and opening it with its own parser. A flag-shaped string can be a decoy. High entropy is normal for compressed images.

## Example interpretation

If the report says:

```text
PNG tEXt metadata at 33: Comment flag{example}
Data after image end at 109: 119 bytes
Embedded signature candidates: ZIP@109
```

The PNG contains a text chunk and extra bytes after IEND. Open `trailing_bytes.bin` with a ZIP parser to verify the ZIP; inspect the text chunk in the original PNG. The two findings may be independent.

## Limits

No scanner can detect every hidden payload. This script does not decode every image pixel format itself, brute-force passphrases, crack encryption, perform OCR, or infer the intended flag. zsteg applies only to PNG/BMP; its absence is reported. TIFF, AVIF, HEIC, and newer formats get header/metadata/signature checks, with detailed parsing delegated to ExifTool and binwalk. For visual clues, open the image manually and check frames, channels, contrast, and small text.

The script scans the first 256 MiB for strings/signatures by default, or 1 GiB with `--deep`; structure checks use the full file. Each optional tool has a timeout, so a timeout in the report means that check was incomplete.

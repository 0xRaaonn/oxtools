# Kali CTF workflow primer

Use this page when you have challenge material but do not yet know which of the [161 guides](README.md) to open. Commands assume a Kali shell and a competition-authorized target or a supplied local file.

## Set up a case folder

Create separate directories for originals, working copies, and outputs. In a terminal:

```bash
mkdir -p case/originals case/work case/output case/notes
cp supplied.bin case/originals/
sha256sum case/originals/supplied.bin
cp case/originals/supplied.bin case/work/
```

Record the hash, tool version, command, and output path for each step. A recovered string is stronger evidence when you can state where it came from: file offset, archive member, packet number, memory process, database row, or program branch. Avoid editing originals.

## Identify an unknown file

Start with `file sample.bin`, a hex view such as `xxd -l 64 sample.bin` if available, and `strings` when available. The user-provided Kali list includes `file`, `bvi`, `xxd` may be available from the separate Windows/WSL list, and Python 3.11 can always show bytes:

```bash
python3 -c "from pathlib import Path; print(Path('sample.bin').read_bytes()[:64].hex(' '))"
```

Common leading bytes: PNG `89 50 4E 47 0D 0A 1A 0A`; JPEG `FF D8 FF`; PDF `25 50 44 46 2D`; ZIP `50 4B 03 04`; gzip `1F 8B`; ELF `7F 45 4C 46`; PE `4D 5A`; SQLite starts with `SQLite format 3`. Extensions can be wrong or deliberately misleading. A hit at a later offset may indicate embedded content.

Next tools by clue:

| Clue | First tools | What to verify |
| --- | --- | --- |
| Archive/compressed bytes | 7z, unzip, unrar, unar, gzip, bzip2, lz4, lzip, lrzip, zstd | Listing, integrity test, extracted file type |
| Embedded file in a larger blob | foremost, bulk_extractor, file, Python | Exact offset, parser success, complete footer |
| Document/PDF | LibreOffice, Didier Stevens Suite, peepdf-3, mutool, oletools | Embedded objects, macros, attachments, visible versus hidden text |
| Image | pngcheck, Jpeginfo, ImageMagick, StegSolve, steghide, stegseek, OpenStego, AperiSolve | Format validity, metadata, bit planes, actual recovered bytes |
| Audio/video | MediaInfo, FFmpeg, Audacity, SoX, Sonic Visualiser, multimon-ng, sstv | Stream count, sample rate, spectrogram, decoded message |
| Database | sqlite3, DB Browser, SQLCipher, FQLite, DBeaver | Schema, WAL/journal files, row IDs, timezones |

## Work with archives and nested formats

List before extraction: `7z l file`, `unzip -l file.zip`, `tar -tf file.tar`, or `unrar l file.rar`. Test integrity where possible, then extract into a new empty directory. An archive can contain nested archives, absolute paths, symlinks, duplicate names, or a password-protected member. Inspect member paths before extraction and do not write recovered files over the evidence.

For compression, distinguish formats from bytes. `gzip`, `bzip2`, `lz4`, `lzip`, `lrzip`, and `zstd` are different. Decompress one layer, run `file` again, and repeat. A stream can have trailing data or multiple concatenated members; do not stop just because one layer opens.

## Image and document challenges

For a PNG, run `pngcheck -v image.png`, inspect visually, then use StegSolve for channels/bit planes. `steghide` and `stegseek` target particular hidden-data formats, not every image. For JPEG, validate with Jpeginfo; look for appended data or metadata as well as visual clues. If you use an online service such as AperiSolve, confirm contest rules permit sending the image to a third party.

For PDFs, begin with visual inspection and the Didier Stevens Suite's `pdfid.py` to count suspicious names, then inspect specific objects with `pdf-parser.py` or peepdf-3. A count of `/JavaScript` is only a lead; inspect the object and whether it is referenced. For Office documents, use oleid/olevba/oleobj before enabling anything in LibreOffice. Macros and external links can execute or fetch content.

For audio, run `mediainfo` or `soxi` to learn stream and sample properties. Listen and view spectrograms in Audacity or Sonic Visualiser. Use FFmpeg to extract a video frame sequence or separate audio stream. Use multimon-ng or sstv only when the waveform resembles a supported signal; decoding random audio often yields noise.

## Web and network challenges

Read the organizer's host/port and scope before scanning. Use `curl -i URL` to see status, headers, cookies, and response body. Change one input at a time. Use Nmap against specified hosts/ports; `-sV` probes services but can generate extra traffic. Ncat/socat provide direct TCP interaction. Use Feroxbuster, ffuf, Gobuster, or Katana to discover content only when scans are allowed; a small targeted wordlist and limited rate is easier to interpret.

An HTTP 200 is not automatically a real route: applications can return the same catch-all page for every path. Compare body length, title, headers, and one deliberately nonexistent path. Save raw requests and responses. `sqlmap`, `jwt_tool`, Hydra, Metasploit, and padding-oracle tools each require a specific vulnerability hypothesis and authorized target. Begin with a manual test and inspect the tool's assumptions.

`tcpdump` can read PCAPs offline or capture live. The Windows guide covers Wireshark/TShark if both environments are available. Passive subdomain tools often contact third-party sources, so their result may be unavailable or against offline-only rules.

## Reverse engineering

First decide what the file is: native ELF/PE, .NET assembly, Java JAR, Android APK/DEX, Python bytecode, Go binary, or Electron ASAR. A suggested path:

1. Use `file` and Detect It Easy to identify format/architecture/packer. `checksec` reports ELF mitigations.
2. Use a format-specific static tool: Cutter/radare2/Ghidra for native code; JADX/Apktool/dex2jar for Android; Fernflower/Bytecode Viewer for Java; pycdc/uncompyle6/unpyc3 for Python; GoReSym for Go; asar for Electron.
3. Search for input-reading and success/failure code. Track constants, byte order, transformations, and branch conditions. Decompiler output is a hypothesis; verify key operations in disassembly or bytecode.
4. If needed, debug in GDB with one of GEF/pwndbg/peda (one plugin at a time), or OllyDbg for old 32-bit Windows binaries. `ltrace` shows selected dynamic-library calls; `strace` shows Linux syscalls. Running the target executes it, so use a controlled lab.
5. Reproduce a pure transformation in Python, C, Go, Rust, or SageMath and test the actual candidate against the unmodified challenge.

Packed binaries may reveal more after UPX unpacking or runtime observation. capa/FLOSS can point toward capabilities or hidden strings, but rule hits require source-code confirmation. BinDiff helps compare two versions; a function match remains heuristic.

## Crypto and passwords

Identify the primitive before choosing a cracking tool. Hex and Base64 are encodings; gzip/zstd are compression; a hash is one-way; RSA/AES are encryption. Hash length alone does not uniquely identify a hash type. Use `hashid` as a lead, then determine format, salt, and algorithm from the challenge context. Use John/hashcat with the exact mode and a clue-based candidate list; rockyou and SecLists are fallback data sources, not universal solutions.

For RSA, write down `n`, `e`, ciphertext format, and padding. PARI/GP or SageMath can test small factors and algebraic weaknesses. FactorDB queries transmit `n` to an external service and may not be available offline. A secure-sized random RSA modulus will not yield to a generic factoring command. `crypto-attacks` contains specialized scripts whose mathematical assumptions must match the challenge.

A padding oracle exists only if the service reveals a distinguishable valid/invalid padding signal. Confirm that behavior manually before using an automation tool. A hash length extension applies to vulnerable `hash(secret || message)` constructions, not HMAC.

## Disk, memory, and app forensics

Know the container: raw image, E01, QCOW2, PST/OST, ESE, SQLite, Android backup, iOS backup, or memory image. Convert only when needed and keep the original. `ewfinfo`/`ewfverify` help with E01; `qemu-img info` identifies virtual disk dependencies. TestDisk works with partition/filesystem metadata; PhotoRec carves signatures and often loses names/paths. Plaso builds a cross-artifact timeline, while RegRipper, libesedb, pff-tools, ALEAPP, iLEAPP, mac_apt, Hindsight, Chainsaw, and Hayabusa target particular artifact families.

Volatility 2 and Volatility 3 use different commands and symbol/profile systems. The listed Kali extras include Volatility 2 community plugins/profiles and Volatility 3 community plugins; match them to the framework version. A memory plugin hit should be corroborated with other plugins, process trees, timestamps, or disk artifacts. Mimikatz/pypykatz findings are sensitive; keep output private.

## Choosing between similar tools

| Need | Begin with | Go deeper with |
| --- | --- | --- |
| Web page discovery | curl, small ffuf/Feroxbuster list | Gobuster/Katana; compare catch-all responses |
| ELF validation path | file, checksec, strings | Cutter/radare2, GDB + one extension |
| Java/Android validator | JADX or Bytecode Viewer | Apktool smali, dex2jar/Fernflower |
| Python packaged app | pyinstxtractor-ng | pycdc, uncompyle6, unpyc3 |
| Browser history | Hindsight | sqlite3/DB Browser, WAL inspection |
| Windows event logs | Chainsaw/Hayabusa | raw EVTX fields and timeline correlation |
| Corrupt/deleted files | TestDisk | PhotoRec, foremost, FQLite for SQLite |
| Hidden data in image | visual inspection, pngcheck/Jpeginfo | StegSolve, steghide/stegseek/OpenStego |

## Troubleshooting

- **Command not found:** check `command -v TOOL`, package location, capitalization, and whether the item is a GUI or data collection.
- **Help flag rejected:** try `-h`, `--help`, a bare subcommand, or the included README. Some tools in this list are project names rather than a single executable.
- **Empty result:** verify input format, correct mode/profile/symbols, extracted offsets, output directory, and whether data is compressed/encrypted.
- **Apparent flag appears:** verify exact bytes and source context. Automated decoders and carvers can produce plausible false positives.
- **Tool needs network:** offline copies, local caches, and contest rules determine whether it can run. The presence of a tool does not authorize internet access.

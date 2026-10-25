# Offline CTF primer for Windows

This companion explains concepts and repeatable workflows shared across the tool guides. It assumes you can use only the software on the competition's allowed list. Examples use only those tools plus ordinary shell built-ins. Verify the event's own rules before installing a package, accessing a target, or uploading data.

## 1. Know the shell you are typing into

**PowerShell** runs Windows executables and uses paths like `C:\CTF\case\file.bin`. Use single quotes around a literal path containing `$`, e.g. `'.\$MFT'`. Use `Get-Location`, `Get-ChildItem`, `Set-Location`, `Copy-Item`, and `Get-FileHash file.bin -Algorithm SHA256`. Call a program in the current directory with `.\program.exe`; just `program.exe` may search PATH instead. For a native executable with arguments, use the call operator `& 'C:\Program Files\Tool\tool.exe' --help`.

**WSL Bash** uses Linux paths. Windows drive C appears at `/mnt/c`. Use `pwd`, `ls -la`, `cd`, `cp`, `sha256sum file.bin`, `command -v tool`, and `man tool`. Quote paths with spaces: `'/mnt/c/Users/A Name/Downloads/file.bin'`. A Bash pipeline passes bytes/text between tools; for searching, PowerShell can use `strings file.bin | Select-String -Pattern 'flag|secret'`. `> output.bin` overwrites a file; `>>` appends. Be careful about shell redirection in PowerShell for binary output; use WSL or a program's explicit output-file option.

**Placeholder notation:** `<file>` or `OFFSET` means substitute a real value. Do not type angle brackets. A decimal offset is not the same as a hex offset. `0x100` is hex 256.

## 2. Preserve evidence and record observations

1. Create a case folder containing `originals`, `work`, `output`, and `notes`.
2. Copy each challenge file into `originals` and record SHA-256. Do analysis on a copy in `work`.
3. Record each transformation: input file/hash, command or GUI operation, output file/hash, and why you used it. A reproducible chain lets you backtrack when a decode path is wrong.
4. When a tool can repair, patch, mount, or execute content, make a fresh copy first. Examples: fsck.fat `-a`, HxD edits, x64dbg runs, qpdf rewrites, ExifTool tag writes.
5. Name output files for what they contain: `http_object_03.png`, `mft.csv`, `stream_12.txt`. Do not overwrite the input accidentally.

## 3. Identify a file from bytes, not its name

Start with `xxd -l 64 file.bin`, `strings -a -n 6 file.bin`, and `exiftool file.bin` when applicable. Common signatures:

| Format | Beginning bytes in hex | Next step |
| --- | --- | --- |
| PNG | `89 50 4E 47 0D 0A 1A 0A` | visual inspection, ExifTool, zsteg |
| JPEG | `FF D8 FF` | visual inspection, ExifTool, binwalk |
| GIF | `47 49 46 38 37 61` or `... 39 61` | frames and metadata |
| PDF | `25 50 44 46 2D` (text `%PDF-`) | viewer, pdftotext, qpdf |
| ZIP / Office Open XML | `50 4B 03 04` | inspect archive structure |
| XZ | `FD 37 7A 58 5A 00` | xz test/decompress |
| Gzip | `1F 8B` | Python gzip or CyberChef |
| ELF | `7F 45 4C 46` | objdump/Ghidra/gdb |
| Windows PE | `4D 5A` (text `MZ`) | Ghidra/x64dbg/dnSpyEx if .NET |
| SQLite | text `SQLite format 3` | SQLECmd or Python sqlite3 |
| PCAP | `D4 C3 B2 A1` or `A1 B2 C3 D4` | Wireshark/TShark/Zeek |
| PCAPNG | `0A 0D 0D 0A` | Wireshark/TShark/Zeek |

Headers can appear at nonzero offsets in a larger file. A signature hit is only a lead. Check sizes, checksums, parser behavior, and surrounding bytes. A renamed file may still be valid; a fake header may be deliberate.

## 4. Decode systematically

**Text encodings:** ASCII covers bytes 0–127. UTF-8 uses one to four bytes per code point. UTF-16LE often contains zero bytes after English letters (`66 00 6C 00 61 00 67 00`). Base64 uses letters, digits, `+`, `/` and padding `=`; URL-safe Base64 uses `-` and `_`. Hex uses two digits per byte; whitespace may separate bytes. URL encoding represents bytes as `%HH`. None of these is encryption.

**Compression:** A decompressor needs the right format and a complete stream. gzip, zlib, raw deflate, and XZ are different. A file can be encoded then compressed or vice versa; test one layer at a time and inspect output headers.

**XOR:** For bytewise XOR, `cipher[i] = plain[i] ^ key[i % len(key)]`. A one-byte key can be searched over 256 values in Python; evaluate output for a known file signature or challenge-specific structure, not merely readable fragments. An XOR key might be text bytes or hex-encoded bytes.

**Endianness:** The bytes `78 56 34 12` represent integer `0x12345678` if read as little-endian 32-bit. Windows/x86 data structures are commonly little-endian; network byte order is big-endian. In Python: `int.from_bytes(data[:4], 'little')`.

**Hashes:** SHA-256 and similar digests are one-way identifiers, not encoded plaintext. A matching file hash can establish that two copies are identical. A hex-looking string of length 32/40/64 may be a digest, but length alone does not prove the algorithm.

## 5. Image and document workflow

1. View the original image or PDF at normal and high zoom. Check all PDF pages, attachments, comments, layers, and properties.
2. Run ExifTool for metadata. Suspicious comments, thumbnails, or mismatched dates may matter.
3. For PNG/BMP, use zsteg and verify promising extracted data. For QR/barcodes, use zbarimg. For embedded files, use binwalk and inspect candidate offsets.
4. For PDF text, try pdftotext default and `-layout`; use qpdf for attachments/encryption/objects.
5. If a tool reports many hits, rank by evidence: valid file signature, plausible length, intact parser result, and fit to challenge prompt.

## 6. Network workflow

1. Confirm the capture type with file header, then inspect protocol hierarchy and conversations in Wireshark or TShark.
2. Identify relevant hosts, ports, and time interval. Apply display filters; never confuse these with capture filters.
3. Follow a TCP stream to reassemble application bytes. For HTTP, inspect requests/responses and export objects. For DNS, inspect query names, TXT records, and unusual repeated labels. For UDP, look for application framing and sequence numbers.
4. Use Zeek when a large capture needs an overview of hosts, connections, DNS, HTTP, and files. Return to packets to confirm a log finding.
5. If traffic is encrypted, find whether the challenge provides session secrets, endpoint memory, or plaintext artifacts. Do not assume a certificate or SSH host key decrypts a session.

**Useful TShark patterns:**

```bash
tshark -r capture.pcapng -q -z io,phs
tshark -r capture.pcapng -Y 'dns' -T fields -e frame.time -e dns.qry.name
tshark -r capture.pcapng -Y 'http.request' -T fields -e ip.src -e http.host -e http.request.uri
tshark -r capture.pcapng -Y 'tcp.stream == 7'
```

## 7. Reverse engineering workflow

1. Determine PE/.NET/ELF and architecture from the header, not the filename. Find strings, imports, resources, and obvious validation code with strings, objdump, Ghidra, or dnSpyEx.
2. Draw the input path: where input is read, transformed, and compared. Record constants and branch conditions.
3. Reproduce pure transforms in Python. Check a few known input/output pairs before searching a key or writing an inverse.
4. If static analysis is insufficient, debug a copied target with x64dbg (Windows) or gdb (WSL/Linux). Break near the compare, inspect registers and memory, and write down module-relative addresses.
5. Verify the actual accepted input by running the challenge in the intended environment. A patched binary succeeding is evidence about a branch, not necessarily the original valid input.

**Common mistakes:** treating decompiler pseudocode as exact, mixing signed and unsigned values, missing integer overflow (Python integers do not wrap automatically), reversing byte order, and reading a C string only up to the first NUL.

## 8. Disk and memory workflow

**Disk:** Determine whole disk versus partition image. For a whole disk, `mmls` gives partition start sectors. Use the same start with `fls -o START` and `icat -o START`. If an inode is marked deleted, recovered content may be partial. Autopsy provides a GUI over many of these operations. Use fsck.fat only to diagnose on the original and repair a copy.

**Windows artifacts:** Match artifact to Eric Zimmerman parser: EVTX → EvtxECmd, NTFS MFT → MFTECmd, Prefetch → PECmd, Jump Lists → JLECmd, LNK → LECmd, Registry → RECmd. Correlate multiple traces before asserting an action occurred.

**Memory:** For Volatility 3, first identify OS/build, then processes, process trees, command lines, network state, and targeted dumps. Preserve symbol files/tool version so results are reproducible. A process list is one view of memory; scan plugins may find unlinked or terminated remnants.

## 9. Troubleshooting checklist

- **Command not found:** Windows and WSL have different PATHs; use the full executable path or check `command -v`/`Get-Command`.
- **Permission denied:** check source file permissions, output folder, and whether a tool requires elevated access for live capture or physical devices.
- **Unexpected empty output:** wrong format, wrong offset, filter too narrow, compressed/encrypted bytes, missing dependency/symbols, or a file with no content of that type.
- **Bad decoded text:** wrong encoding, wrong operation order, truncated input, or data that is binary rather than text.
- **Different results across tools:** compare exact bytes, file hashes, versions, options, and timezones.
- **Tool option rejected:** run local `--help` or `-h`; installed version and operating system take precedence over examples here.

## 10. Keep findings defensible

The flag should be supported by a reproducible path from the provided challenge material. Record where it came from: file and offset, packet and stream, process/PID and memory address, PDF object, or program branch. If an output looks like a flag but the source is unclear, inspect its context before submitting.

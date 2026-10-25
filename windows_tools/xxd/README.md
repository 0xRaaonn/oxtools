# xxd

**Use:** make a hex dump or convert a hex dump back to bytes. Excellent for file signatures and offsets.

**Commands (WSL):** `xxd -l 64 file.bin` shows first 64 bytes; `xxd -s 0x100 -l 128 file.bin` starts at offset 0x100; `xxd -p file.bin` prints plain hex; `xxd -r -p hex.txt output.bin` converts plain hex to bytes; `xxd -g 1 file.bin` groups bytes individually.

**Reading output:** Left column is offset, middle is hex bytes, right is a printable approximation. Multi-byte integers may be little-endian or big-endian; the displayed byte order itself never changes.

**CTF workflow:** Check magic bytes, locate an embedded header, compare two files near a difference, or convert a provided hex string to binary. Use `xxd -r` only on a trusted hex dump and inspect the output.

**Pitfalls:** The right-hand text column replaces nonprintable bytes with dots. `-r` expects xxd-like formatting unless using `-p`. Never infer whole-file type from extension alone.

Source: [xxd manual](https://manpages.debian.org/unstable/xxd/xxd.1.en.html).

## Worked example: detect a wrong file extension

Run `xxd -l 16 mystery.jpg`. If the first bytes are `25 50 44 46 2D`, they spell `%PDF-`, so treat the file as a PDF despite its `.jpg` name. Open a copy in the PDF viewer and run qpdf/pdftotext. If the signature appears at a later offset, inspect whether a PDF is embedded inside another container.

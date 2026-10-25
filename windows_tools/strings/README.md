# strings

**Use:** find printable byte runs in binaries. This is a first pass, not a parser.

**Commands (GNU, WSL):** `strings -a -n 4 sample.bin` scans all bytes with minimum length 4. `strings -a -n 8 -t x sample.bin` prints hex offsets. `strings -a -el sample.bin` scans UTF-16LE; `-eb` scans UTF-16BE. Search results in PowerShell with `strings sample.bin | Select-String -Pattern 'flag|password|http'`.

**CTF workflow:** Look for URLs, messages, format strings, filenames, paths, and candidate secrets. Use an offset with `xxd -s 0xOFFSET -l 64 sample.bin` to inspect context. Windows programs often use UTF-16LE.

**Pitfalls:** Compressed/encrypted data will not look readable. Short strings create false positives. A string may be unused decoy data. Windows Sysinternals Strings has different options; check the installed version.

Source: [GNU strings manual](https://sourceware.org/binutils/docs/binutils/strings.html).

## Worked example: find an embedded URL

Run `strings -a -n 6 -t x suspect.exe` and suppose it prints `2a10 https://example.test/api`. The `2a10` value is a hexadecimal file offset. Run `xxd -s 0x2a10 -l 80 suspect.exe` to confirm the bytes and inspect neighboring data. The URL may be configuration or a decoy; trace its use in Ghidra before drawing a conclusion.

## More CTF scenario questions

### No password appears in a Windows binary, but the GUI visibly uses one. What now?

Try UTF-16LE scanning with `strings -a -el sample.exe`. Windows text often alternates ASCII-looking bytes with zero bytes; inspect any hit's offset in xxd.

### A flag-looking string appears at offset `0x200`. Is that the answer?

Check surrounding bytes with `xxd -s 0x200 -l 128` and trace code references if it is an executable. It could be an unused example, metadata, or a decoy.

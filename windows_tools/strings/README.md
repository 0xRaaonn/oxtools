# strings

**Use:** find printable byte runs in binaries. This is a first pass, not a parser.

**Commands (GNU, WSL):** `strings -a -n 4 sample.bin` scans all bytes with minimum length 4. `strings -a -n 8 -t x sample.bin` prints hex offsets. `strings -a -el sample.bin` scans UTF-16LE; `-eb` scans UTF-16BE. Search results in PowerShell with `strings sample.bin | Select-String -Pattern 'flag|password|http'`.

**CTF workflow:** Look for URLs, messages, format strings, filenames, paths, and candidate secrets. Use an offset with `xxd -s 0xOFFSET -l 64 sample.bin` to inspect context. Windows programs often use UTF-16LE.

**Pitfalls:** Compressed/encrypted data will not look readable. Short strings create false positives. A string may be unused decoy data. Windows Sysinternals Strings has different options; check the installed version.

Source: [GNU strings manual](https://sourceware.org/binutils/docs/binutils/strings.html).

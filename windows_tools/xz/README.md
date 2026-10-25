# xz

**Use:** compress/decompress XZ, LZMA, and sometimes raw LZMA streams.

**Commands:** `xz -l archive.xz` lists stream information; `xz -t archive.xz` tests integrity; `xz -dk archive.xz` decompresses and keeps original; `xz -dc archive.xz > output.bin` writes decompressed bytes to stdout. `unxz -k archive.xz` is another form. Use `xz --help` for filters and format selection.

**CTF workflow:** Confirm the magic bytes (XZ starts `FD 37 7A 58 5A 00`), test the stream, then decompress to a separate file. A file may contain concatenated streams or trailing data; inspect both output and original footer.

**Pitfalls:** Decompression may use substantial memory. Wrong file extension is common, so trust format bytes. Shell redirection must preserve binary output; WSL is safer than PowerShell for `-c >`.

Source: [XZ Utils documentation](https://tukaani.org/xz/).

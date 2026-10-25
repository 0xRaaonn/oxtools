# xz

**Use:** compress/decompress XZ, LZMA, and sometimes raw LZMA streams.

**Commands:** `xz -l archive.xz` lists stream information; `xz -t archive.xz` tests integrity; `xz -dk archive.xz` decompresses and keeps original; `xz -dc archive.xz > output.bin` writes decompressed bytes to stdout. `unxz -k archive.xz` is another form. Use `xz --help` for filters and format selection.

**CTF workflow:** Confirm the magic bytes (XZ starts `FD 37 7A 58 5A 00`), test the stream, then decompress to a separate file. A file may contain concatenated streams or trailing data; inspect both output and original footer.

**Pitfalls:** Decompression may use substantial memory. Wrong file extension is common, so trust format bytes. Shell redirection must preserve binary output; WSL is safer than PowerShell for `-c >`.

Source: [XZ Utils documentation](https://tukaani.org/xz/).

## Worked example: unpack a disguised XZ stream

Suppose `xxd -l 8 mystery.dat` begins `fd 37 7a 58 5a 00`. Run `xz -t mystery.dat` to test it, then `xz -dc mystery.dat > unpacked.bin` in WSL. Inspect `xxd -l 32 unpacked.bin` to identify the next format. If `xz -t` reports trailing garbage, inspect the original file for appended data instead of assuming the whole file is one XZ stream.

## More CTF scenario questions

### `xz -t mystery.bin` passes but decompression yields another compressed file. What next?

Inspect the new file's magic bytes, then decompress the next layer with its correct tool. Do not rename by guess alone; nested compression is common.

### A decompressed file has extra bytes after a valid image. Is that an error?

Compare the file's declared length/footer with total size, inspect trailing bytes in xxd, and test whether they form another file or message. Some containers allow trailing data.

# objdump

**Use:** inspect object/executable headers, sections, symbols, and disassembly without running the file. Usually GNU binutils in WSL.

**Commands:** `objdump -f chall` (format/architecture), `objdump -h chall` (sections), `objdump -t chall` (symbols), `objdump -d -M intel chall` (code), `objdump -s -j .rodata chall` (raw constants), `objdump -r object.o` (relocations). Narrow output with `objdump --start-address=0x401000 --stop-address=0x401100 -d chall`.

**CTF workflow:** Check architecture and entry point, inspect symbols and constants, then disassemble candidate routines. A call to `strcmp` or `memcmp` can locate a check, though the compared value may be built at runtime.

**Pitfalls:** `-D` disassembles data sections too and may produce false code. PIE/ASLR changes runtime addresses. Supported file formats vary; check `objdump --info`.

Source: [GNU objdump manual](https://sourceware.org/binutils/docs/binutils/objdump.html).

## Worked example: locate a string reference

Run `objdump -s -j .rodata chall` and find a message such as “Correct!”. Then run `objdump -d -M intel chall` and search the disassembly for code loading the string's address. Inspect the surrounding conditional jump to locate validation logic. For position-independent binaries, the disassembly may use RIP-relative addressing rather than an absolute address.

## More CTF scenario questions

### A stripped ELF has no useful function names. Can objdump still help?

Run `objdump -f` for architecture, `objdump -h` for sections, and `objdump -d -M intel` to inspect code. Start near entry and cross-reference string/constant addresses in Ghidra.

### Why does `objdump -D` show instructions inside a data section?

It linearly disassembles all sections and can interpret arbitrary bytes as code. Prefer `-d` for executable sections and validate suspicious regions against section flags and control flow.

# objdump

**Use:** inspect object/executable headers, sections, symbols, and disassembly without running the file. Usually GNU binutils in WSL.

**Commands:** `objdump -f chall` (format/architecture), `objdump -h chall` (sections), `objdump -t chall` (symbols), `objdump -d -M intel chall` (code), `objdump -s -j .rodata chall` (raw constants), `objdump -r object.o` (relocations). Narrow output with `objdump --start-address=0x401000 --stop-address=0x401100 -d chall`.

**CTF workflow:** Check architecture and entry point, inspect symbols and constants, then disassemble candidate routines. A call to `strcmp` or `memcmp` can locate a check, though the compared value may be built at runtime.

**Pitfalls:** `-D` disassembles data sections too and may produce false code. PIE/ASLR changes runtime addresses. Supported file formats vary; check `objdump --info`.

Source: [GNU objdump manual](https://sourceware.org/binutils/docs/binutils/objdump.html).

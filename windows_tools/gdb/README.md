# gdb

**Use:** debug native programs, mainly ELF/Linux binaries in WSL. Debugging executes the target.

**Session:** `gdb --args ./chall arg1`. Inside gdb: `start`, `info registers`, `x/16gx $rsp`, `x/20i $pc`, `break main`, `continue`, `next`, `step`, `finish`, `backtrace`, `quit`. `run` restarts; `break *0x401234` breaks at an address; `disassemble main` shows instructions. `x/s ADDRESS` prints a C string, `x/32xb ADDRESS` shows bytes, and `print/x EXPR` formats hex.

**CTF workflow:** Break before a comparison or decoder and inspect buffers and arguments. On x86-64 Linux, the first integer/pointer arguments usually enter via RDI, RSI, RDX, RCX, R8, R9. Use symbol-relative breakpoints for PIE binaries.

**Pitfalls:** Stripped or optimized binaries may lack readable symbols. ASLR changes runtime addresses. Windows x64 calling conventions differ from Linux. Programs may detect a debugger.

Source: [GDB manual](https://sourceware.org/gdb/current/onlinedocs/gdb.html).

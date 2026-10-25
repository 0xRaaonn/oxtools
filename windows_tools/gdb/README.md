# gdb

**Use:** debug native programs, mainly ELF/Linux binaries in WSL. Debugging executes the target.

**Session:** `gdb --args ./chall arg1`. Inside gdb: `start`, `info registers`, `x/16gx $rsp`, `x/20i $pc`, `break main`, `continue`, `next`, `step`, `finish`, `backtrace`, `quit`. `run` restarts; `break *0x401234` breaks at an address; `disassemble main` shows instructions. `x/s ADDRESS` prints a C string, `x/32xb ADDRESS` shows bytes, and `print/x EXPR` formats hex.

**CTF workflow:** Break before a comparison or decoder and inspect buffers and arguments. On x86-64 Linux, the first integer/pointer arguments usually enter via RDI, RSI, RDX, RCX, R8, R9. Use symbol-relative breakpoints for PIE binaries.

**Pitfalls:** Stripped or optimized binaries may lack readable symbols. ASLR changes runtime addresses. Windows x64 calling conventions differ from Linux. Programs may detect a debugger.

Source: [GDB manual](https://sourceware.org/gdb/current/onlinedocs/gdb.html).

## Worked example: inspect a comparison

For a Linux challenge binary, start `gdb --args ./chall AAAAA`. Set `break strcmp`, then `run`. On x86-64 Linux, inspect arguments with `x/s $rdi` and `x/s $rsi`; one may be your input and the other a comparison value. If a breakpoint in `strcmp` does not hit, the program may compare manually or use another library routine. Continue with `finish` and inspect the return value in `$rax`.

## More CTF scenario questions

### A breakpoint at `0x401000` works once but not after restart. Why?

The binary may be PIE with ASLR. Use a symbol-relative breakpoint such as `break main` or inspect mapped module addresses with `info proc mappings`, then calculate a runtime address from the module base.

### The program says Wrong even though the input string looks right. What should I inspect?

Break just before the compare, print both buffers as hex with `x/32xb ADDRESS` and check lengths, newline, and NUL terminator. `x/s` stops at NUL and can hide later bytes.

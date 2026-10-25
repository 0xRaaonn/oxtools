# x64dbg

**Use:** dynamically debug Windows x86/x64 executables. x64dbg handles 64-bit targets; x32dbg handles 32-bit targets. Running a target executes its code, so use a dedicated lab environment.

**Workflow:** Open a challenge executable. The CPU view shows disassembly, registers, stack, and hex data. Set a breakpoint with `F2` on an instruction; `F9` runs/continues; `F7` steps into; `F8` steps over. Follow addresses in Dump to inspect strings and buffers. Use the Symbols/Modules views for imports and DLLs, and the log for breakpoint events.

**CTF approach:** Locate input APIs and comparisons through imported functions or strings. Break near a check, enter a test input, and inspect buffers and flags just before a conditional jump. Note whether a branch checks ZF after `cmp`/`test`. Patch only a copy when testing a hypothesis.

**Pitfalls:** ASLR moves modules; use module-relative offsets. Debugger detection and packed code can change behavior. 32-bit and 64-bit calling conventions differ. Do not assume the GUI's comments are ground truth.

Source: [x64dbg documentation](https://help.x64dbg.com/).

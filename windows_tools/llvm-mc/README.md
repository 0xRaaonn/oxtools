# llvm-mc

**Use:** assemble or disassemble individual machine instructions to test architecture and encoding hypotheses. It is not a full binary reverse-engineering GUI.

**Commands:** `llvm-mc --version` lists targets; `llvm-mc -triple=x86_64 -show-encoding input.s` shows assembly encodings; `llvm-mc -triple=x86_64 -disassemble -show-inst` disassembles textual hex bytes from standard input; `llvm-mc -triple=aarch64 -filetype=obj input.s -o code.o` creates an object file. Consult `llvm-mc --help` and target-specific syntax.

**CTF workflow:** Verify a suspicious byte sequence or patch idea against the target architecture. Compare the result with Ghidra/objdump. x86 instructions have variable length; starting at the wrong byte can still produce valid-looking assembly.

**Pitfalls:** Triple, CPU, features, and syntax dialect affect interpretation. Input for disassembly is formatted byte text, not always a raw binary file. Generated objects are not standalone executables.

Source: [LLVM command guide](https://llvm.org/docs/CommandGuide/llvm-mc.html).

## Worked example: verify an x86-64 instruction

Create `test.s` containing `xor eax, eax` on one line and run `llvm-mc -triple=x86_64 -show-encoding test.s`. The output should show the instruction and its encoded bytes, often `31 c0` for this form. Compare those bytes with a target patch location in HxD or Ghidra. Equivalent assembly text may encode differently; test the exact form and target CPU you intend to use.

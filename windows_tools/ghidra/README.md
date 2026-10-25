# Ghidra

**Use:** statically analyze binaries with disassembly, decompilation, strings, references, and data types. It supports many architectures/formats.

**Workflow:** Create a project, import the binary, open in CodeBrowser, and accept analysis. Use Symbol Tree and Functions to navigate. Search → For Strings finds constants; double-click a string and inspect references to find code using it. Listing shows instructions; Decompiler shows approximate C-like code. Rename functions and variables as you learn their roles; set correct types to improve the decompiler.

**CTF approach:** Identify input-reading code, trace it to validation/transform routines, map loops and constants, and reproduce the algorithm in Python. Use Function Graph for branch structure and Data Type Manager for structs. Compare decompiled logic to assembly whenever behavior matters.

**Pitfalls:** Decompiler output is an interpretation, not original source. Wrong architecture, base address, or calling convention produces confusing results. Packed/encrypted code may require runtime analysis. Import as a copy and avoid executing unknown samples.

Source: [Ghidra documentation](https://ghidra-sre.org/).

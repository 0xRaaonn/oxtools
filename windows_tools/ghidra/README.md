# Ghidra

**Use:** statically analyze binaries with disassembly, decompilation, strings, references, and data types. It supports many architectures/formats.

**Workflow:** Create a project, import the binary, open in CodeBrowser, and accept analysis. Use Symbol Tree and Functions to navigate. Search → For Strings finds constants; double-click a string and inspect references to find code using it. Listing shows instructions; Decompiler shows approximate C-like code. Rename functions and variables as you learn their roles; set correct types to improve the decompiler.

**CTF approach:** Identify input-reading code, trace it to validation/transform routines, map loops and constants, and reproduce the algorithm in Python. Use Function Graph for branch structure and Data Type Manager for structs. Compare decompiled logic to assembly whenever behavior matters.

**Pitfalls:** Decompiler output is an interpretation, not original source. Wrong architecture, base address, or calling convention produces confusing results. Packed/encrypted code may require runtime analysis. Import as a copy and avoid executing unknown samples.

Source: [Ghidra documentation](https://ghidra-sre.org/).

## Worked example: trace a password check

Import a challenge executable and run auto-analysis. Search for the string “Wrong password”, open its references, and inspect the surrounding function in the Decompiler. If you see a loop XORing input bytes with `0x23` before `memcmp`, rename the function to reflect that and inspect the expected byte array. Reproduce the loop in Python, then test the candidate input on the unmodified challenge executable. Confirm key and lengths in Listing assembly.

## More CTF scenario questions

### A decompiler shows `if (x == 0)`, but the program accepts a nonzero input. What do I trust?

Inspect the Listing around the branch, operand sizes, signedness, and preceding flags. Correct data types or calling convention if needed; pseudocode can be misleading.

### The binary contains `flag{example}` but never prints it. Is it the answer?

Follow references to the string. If no reachable code uses it, treat it as possible decoy or test data. Trace the actual success path and test on the original executable.

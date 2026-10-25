# Cutter

## What it does

GUI reverse engineering built on Rizin/radare2 ecosystem.

## First steps

Open a binary, run analysis, inspect Functions, Graph, Strings, and Decompiler panes.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Open a PE, follow a “Correct” string reference to a validation function, and inspect the branch in disassembly.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Decompiler output is approximate; verify with instructions and target architecture.

# radare2

## What it does

CLI reverse-engineering suite for disassembly, analysis, and patching copies.

## First steps

Use `r2 -A binary`; inside, `afl` lists functions, `iz` strings, `pdf @ main` disassembles, `q` quits.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Find a “Correct” string in `iz`, follow its references, and inspect the surrounding branch.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Analysis heuristics and decompiler plugins vary; commands can modify files in write mode.

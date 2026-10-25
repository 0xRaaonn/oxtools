# BinDiff

## What it does

Compare functions between two binary versions using disassembler databases.

## First steps

Import both versions into supported disassemblers and run a BinDiff comparison.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Compare original and patched challenge binaries; inspect the one changed function and its control-flow difference.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Function matches are heuristic; verify changes in assembly and bytes.

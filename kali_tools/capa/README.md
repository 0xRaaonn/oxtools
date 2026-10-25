# capa

## What it does

Detect capabilities in programs from code patterns and rules.

## First steps

Run `capa sample.exe` and inspect `capa --help` for output formats.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Run capa on a challenge PE and see “decode data using XOR”; locate the matched function in Ghidra and confirm the loop.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Rules are heuristic and can miss packed code or overstate behavior; inspect the matched code.

# FLOSS (FLARE Obfuscated String Solver)

## What it does

Recover static and certain decoded/stack strings from binaries.

## First steps

Run `floss sample.exe` and inspect `floss -h` for filtering.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

FLOSS reports a decoded URL not seen by strings; trace the referenced function in Ghidra and confirm the decode logic.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

It may miss custom obfuscation or emit false positives; output is not proof of execution.

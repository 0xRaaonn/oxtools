# GoReSym

## What it does

Recover Go symbols, types, and build information from stripped binaries.

## First steps

Use `GoReSym -h` and run it against a copied Go executable.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Recover function names from a stripped Go challenge, then import or label those names in Ghidra to trace validation.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Packed or corrupted binaries may yield partial data; recovered names need code verification.

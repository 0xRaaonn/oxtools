# dwarf2json

## What it does

Generate Volatility 3 symbol JSON from DWARF and kernel debug files.

## First steps

Run `dwarf2json --help` and select Linux/macOS generation mode matching source symbols.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Given a Linux kernel debug ELF and System.map, generate a symbol JSON and place it in Volatility's symbol path; rerun `linux.pslist`.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Kernel build mismatch makes symbols unusable; architecture and debug data must match the memory image.

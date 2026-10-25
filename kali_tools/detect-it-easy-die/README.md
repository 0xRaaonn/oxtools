# Detect It Easy (DIE)

## What it does

Identify executable formats, compilers, packers, and protections.

## First steps

Open a copied binary in the GUI or use installed `diec` CLI if available.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

DIE reports UPX on `chall.exe`; confirm with UPX's test command and inspect the unpacked copy in Ghidra.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Signatures are heuristic; a packer label alone does not prove content or safety.

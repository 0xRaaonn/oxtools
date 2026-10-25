# OllyDbg

## What it does

Debug 32-bit Windows executables with a GUI.

## First steps

Open a copied 32-bit PE in an isolated Windows environment; use breakpoints and step controls.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Break near a password comparison, inspect stack arguments and conditional jump, then test a candidate in the original binary.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

OllyDbg is primarily 32-bit and older; modern 64-bit binaries need another debugger.

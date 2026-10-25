# pyinstxtractor-ng

## What it does

Extract bundled files from PyInstaller executables.

## First steps

Use `pyinstxtractor-ng app.exe` or the installed CLI's help syntax.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Extract a PyInstaller challenge PE, locate `.pyc` files, then inspect them with pycdc or uncompyle6.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Extracted bytecode may still be obfuscated; do not run unknown bundled programs.

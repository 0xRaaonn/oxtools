# pycdc (Decompyle++)

## What it does

Decompile Python bytecode files to approximate Python source.

## First steps

Use `pycdc module.pyc > recovered.py` and `pycdas module.pyc` if installed.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Recover a simple Python challenge validator from `.pyc`, then compare decompiled code with disassembly when syntax looks wrong.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Python bytecode versions matter; decompilation can fail or misrepresent control flow.

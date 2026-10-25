# uncompyle6

## What it does

Decompile supported Python bytecode versions to Python-like source.

## First steps

Use `uncompyle6 -o out module.pyc` and check version support with `--help`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Decompile a supplied Python 3.7 pyc validator, inspect its condition, and compare with a bytecode disassembler if output looks odd.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Not all Python versions are supported; decompiled source may differ semantically at edge cases.

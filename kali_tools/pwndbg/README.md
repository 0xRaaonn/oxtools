# pwndbg

## What it does

GDB plugin for exploit and reverse-engineering views.

## First steps

Start GDB with pwndbg loaded; use `context`, `vmmap`, and `telescope $rsp`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Break at a crash and inspect stack, mappings, and registers to understand the faulting address.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Plugin command names vary by version; do not load alongside conflicting GDB UI plugins.

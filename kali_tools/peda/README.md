# peda

## What it does

GDB extension for exploit-development convenience views.

## First steps

Start GDB after loading peda; use `help peda` or `peda help` depending on installation.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Break at main and inspect peda's register/stack context while the challenge processes input.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Plugin setup varies and can conflict with GEF/pwndbg; use one GDB extension at a time.

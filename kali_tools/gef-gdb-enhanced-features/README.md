# GEF (GDB Enhanced Features)

## What it does

Add reverse-engineering views and commands to GDB.

## First steps

Start `gdb ./chall`, run `gef help`, and use GEF's context and checksec commands.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Break at main; GEF's context shows registers, stack, and nearby instructions as the program reads input.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

GEF requires compatible GDB/Python; commands may differ by installed revision.

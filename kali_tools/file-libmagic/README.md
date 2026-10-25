# file (libmagic)

## What it does

Identify file formats from signatures and heuristics.

## First steps

Run `file sample.bin` and `file -k sample.bin` for multiple matches.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

A file named `photo.jpg` reports “PDF document”; inspect its first bytes with xxd and use PDF tools.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Heuristics can misidentify polyglots and corrupted files; verify magic and parser behavior.

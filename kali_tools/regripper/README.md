# RegRipper

## What it does

Extract Windows Registry artifact reports through plugins.

## First steps

Use `rip.pl -r NTUSER.DAT -p userassist` or `rip.pl -r SYSTEM -f system` with installed plugin names.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Parse a copied NTUSER.DAT, inspect UserAssist entries, and correlate candidate program activity with Prefetch.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Plugin output needs OS/version context; Registry LastWrite time is not always action time.

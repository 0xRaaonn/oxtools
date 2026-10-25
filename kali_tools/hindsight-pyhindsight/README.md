# Hindsight (pyhindsight)

## What it does

Parse browser history and related artifacts into a timeline.

## First steps

Run `hindsight.py --help` or GUI and point it at a copied browser profile.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Parse a provided Chrome profile and find a download URL near the challenge's event time; confirm against SQLite source records.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Browser profiles may be locked or have WAL files; preserve all related files and timezones.

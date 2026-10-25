# tar

## What it does

Create/list/extract tar archives.

## First steps

Use `tar -tf archive.tar` to list and `tar -xf archive.tar -C out` to extract.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

List a challenge TAR before extraction, then inspect a nested `notes.txt` in an empty output directory.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Archives may contain absolute paths, symlinks, or traversal entries; inspect names before extraction.

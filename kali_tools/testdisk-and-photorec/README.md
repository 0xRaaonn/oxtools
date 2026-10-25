# TestDisk and PhotoRec

## What it does

Recover partitions/filesystem metadata (TestDisk) and carve files by signatures (PhotoRec).

## First steps

Start `testdisk image.dd` or `photorec image.dd` and follow GUI menus on a copy.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Use TestDisk to inspect a missing FAT partition; if metadata is gone, use PhotoRec to carve JPEGs into a separate folder.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Recovery can be partial; PhotoRec usually loses filenames/paths. Never write recovered data onto source media.

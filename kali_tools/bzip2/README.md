# bzip2

## What it does

Compress/decompress bzip2 streams.

## First steps

Use `bzip2 -tv file.bz2` to test and `bzip2 -dk file.bz2` to keep the original.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

A file starting `BZh` tests cleanly; decompress it and inspect the new file's magic bytes.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Decompression can overwrite similarly named files; use a working copy.

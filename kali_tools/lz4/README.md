# lz4

## What it does

Compress/decompress LZ4 frames.

## First steps

Use `lz4 -t file.lz4` and `lz4 -d file.lz4 out.bin`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

A challenge file begins with LZ4 frame magic; test it, decompress, and identify the resulting bytes.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Raw LZ4 blocks may lack frame metadata and need known size; extension alone is insufficient.

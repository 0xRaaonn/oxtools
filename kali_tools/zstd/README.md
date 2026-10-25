# zstd

## What it does

Compress/decompress Zstandard streams.

## First steps

Use `zstd -t file.zst`, `zstd -d -k file.zst`, and `zstd -dc file.zst > out.bin`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

A file begins Zstandard magic `28 B5 2F FD`; test, decompress, then identify the next layer.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Frames can be concatenated; decompressed output may be much larger than input.

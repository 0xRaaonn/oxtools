# gzip

## What it does

Compress/decompress gzip streams.

## First steps

Use `gzip -t file.gz`, `gzip -dk file.gz`, or `gzip -dc file.gz > out.bin`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

A file starts `1f 8b`; test it, decompress to a copy, and inspect the next layer with file/xxd.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Output can overwrite a same-named file; gzip can contain concatenated members.

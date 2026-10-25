# lrzip

## What it does

Decompress large rzip/lrzip archives.

## First steps

Use `lrzip -t archive.lrz` and `lrzip -d -o output.bin archive.lrz` after checking local help.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Test a supplied LRZ archive, decompress a copy, then inspect the output header with file/xxd.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Decompression can require substantial memory/disk and should not overwrite source.

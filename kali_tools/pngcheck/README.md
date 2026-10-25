# pngcheck

## What it does

Validate PNG chunk structure and CRCs.

## First steps

Use `pngcheck -v image.png` or `pngcheck -t image.png`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

A copied PNG reports a bad IDAT CRC; locate the chunk offset and compare the bytes in HxD before attempting repair.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

A valid PNG can still hide data; a CRC error can be deliberate or accidental.

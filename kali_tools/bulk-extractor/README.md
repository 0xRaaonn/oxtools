# bulk_extractor

## What it does

Scan disk images/files for features such as emails, URLs, and card-like strings without filesystem parsing.

## First steps

Run `bulk_extractor -o bulk_out image.dd` on a copied image.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Inspect `email.txt` and `url.txt` in the output to locate a suspicious address, then confirm the byte offset with xxd.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Feature hits can be false positives or stale deleted data; correlate with filesystem context.

# Plaso (log2timeline, psort, pinfo)

## What it does

Build and query forensic timelines from many artifact sources.

## First steps

Use `log2timeline.py timeline.plaso image.dd`, `pinfo.py timeline.plaso`, and `psort.py -o l2tcsv timeline.plaso > timeline.csv`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Create a timeline from a challenge image, filter around a suspicious event time, and corroborate with raw files/EVTX.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Processing can be slow/storage-heavy; timezone and parser version affect output.

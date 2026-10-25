# peepdf-3

## What it does

Analyze PDF structure and suspicious objects interactively.

## First steps

Run `peepdf -h` or open `peepdf -i suspicious.pdf` if supported.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

List PDF objects, locate an object containing JavaScript, and inspect its stream bytes before deciding whether it is active.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

PDF object references/filters can obscure content; do not assume a suspicious token is executed.

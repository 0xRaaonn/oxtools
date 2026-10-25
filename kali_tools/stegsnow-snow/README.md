# stegsnow (SNOW)

## What it does

Hide/recover data in trailing spaces and tabs of text files.

## First steps

Use `stegsnow -h`; extraction commonly uses `stegsnow file.txt` or `stegsnow -C -p PASSWORD file.txt`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

A supplied text file looks normal, but SNOW extracts a short message from line-end whitespace; compare raw bytes before editing.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Editors may strip trailing whitespace; preserve the original file exactly.

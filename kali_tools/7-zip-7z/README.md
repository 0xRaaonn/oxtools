# 7-Zip (7z)

## What it does

List, test, and extract many archive formats.

## First steps

Use `7z l archive.zip`, `7z t archive.zip`, and `7z x archive.zip -oout`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Run `7z l puzzle.zip` to see member names, then `7z x puzzle.zip -oextracted`; inspect an extracted `note.txt` separately.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Extraction can overwrite files or traverse paths; use an empty output directory and inspect listings first.

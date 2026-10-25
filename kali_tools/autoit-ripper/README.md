# AutoIt-Ripper

## What it does

Extract scripts and resources from compiled AutoIt executables.

## First steps

Run the installed tool's `--help` and provide a copied AutoIt PE file.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Extract a challenge executable, inspect recovered script text for a decryption key, and cross-check it against runtime behavior.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Extraction can fail on protected/newer formats; a recovered script may be incomplete.

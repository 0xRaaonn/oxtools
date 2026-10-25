# bvi

## What it does

Edit binary files in a vi-like terminal interface.

## First steps

Open a copy with `bvi file.bin` and use its help for hex editing keys.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Open a copied file, navigate to offset 0, inspect its magic bytes, change one known corrupt byte, save under a new name, and verify with xxd.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Editing the original changes evidence; insert versus overwrite behavior matters.

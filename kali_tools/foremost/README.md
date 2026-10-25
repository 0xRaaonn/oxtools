# foremost

## What it does

Carve files from raw images by signature.

## First steps

Use `foremost -i disk.img -o carved_out` and inspect its audit file.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Carve a supplied image, inspect recovered PNG files, then compare offsets with filesystem metadata.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Carving can yield fragmented/partial files and duplicates; an extracted file may lack original path.

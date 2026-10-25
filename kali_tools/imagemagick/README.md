# ImageMagick

## What it does

Inspect and transform images from the CLI.

## First steps

Use `magick identify image.png` and `magick image.png -crop 100x100+0+0 crop.png` (older builds may use `identify`/`convert`).

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Crop a tiny QR code from a challenge image and enlarge a copy with nearest-neighbor scaling before ZBar.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Image transformations can alter hidden bits or metadata; keep the original.

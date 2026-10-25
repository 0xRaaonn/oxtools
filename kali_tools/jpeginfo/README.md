# Jpeginfo

## What it does

Validate JPEG structure and report corruption.

## First steps

Use `jpeginfo -c image.jpg` and inspect `jpeginfo --help`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

A suspicious JPEG fails structure validation near the end; inspect trailing bytes with xxd/binwalk for appended data.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

A clean structure does not rule out steganography; a corrupt structure does not identify the payload.

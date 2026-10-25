# steghide

## What it does

Embed/extract data in supported JPEG/BMP/WAV/AU carriers using a passphrase.

## First steps

Use `steghide info image.jpg` and `steghide extract -sf image.jpg -xf payload.bin`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Given an organizer-supplied passphrase, extract a payload from a JPEG and inspect its file signature.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Wrong passphrases and unsupported carriers produce failures; steghide does not detect every stego scheme.

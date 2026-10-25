# Volatility 2

## What it does

Analyze memory images with the older Volatility 2 plugin/profile model.

## First steps

Run `vol.py -f memory.raw imageinfo`, then `vol.py -f memory.raw --profile=PROFILE pslist` when applicable.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Identify a Windows memory image profile, enumerate processes, then use cmdline/netscan-style plugins appropriate to that profile.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Volatility 2 syntax differs from 3 and relies on exact profiles; old builds may require Python 2.

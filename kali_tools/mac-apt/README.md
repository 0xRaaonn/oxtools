# mac_apt

## What it does

Parse macOS forensic artifacts and timelines.

## First steps

Run `mac_apt.py -h` or installed entry point to choose image/input and plugins.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Process a supplied macOS filesystem image with selected plugins, then inspect a Safari/history or user activity CSV.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

APFS snapshots, OS versions, and timezones affect results; validate with raw artifacts.

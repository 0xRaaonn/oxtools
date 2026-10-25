# Didier Stevens Beta tools (onedump.py)

## What it does

Inspect and extract OLE or related embedded data with a beta script.

## First steps

Use `python onedump.py -h` from the local tool directory to identify options.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Run the script against a supplied Office container, list streams, and extract a suspicious stream to a separate file for inspection.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Beta flags can change; select stream IDs from actual output and preserve the original.

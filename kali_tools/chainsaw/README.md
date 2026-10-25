# Chainsaw

## What it does

Hunt Windows event logs using Sigma rules and other patterns.

## First steps

Use `chainsaw --help`; a common action is `chainsaw hunt logs/ -s sigma/ -o results.csv`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Hunt a supplied EVTX directory, inspect a matching PowerShell event, then open the original log entry to verify fields.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Rule matches are leads, not proof; Sigma fields and mappings vary by rule pack/version.

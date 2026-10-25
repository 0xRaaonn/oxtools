# Hayabusa

## What it does

Analyze Windows EVTX logs with built-in detection rules and timeline output.

## First steps

Run `hayabusa --help` and use the timeline command for a supplied log directory.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Generate a timeline from challenge EVTX files, inspect a suspicious logon event, then cross-check the original event fields.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Rule packs/versions affect findings; timestamps need timezone normalization.

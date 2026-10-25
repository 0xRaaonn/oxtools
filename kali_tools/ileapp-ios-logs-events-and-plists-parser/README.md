# iLEAPP (iOS Logs, Events, And Plists Parser)

## What it does

Parse iOS forensic extractions into artifact reports.

## First steps

Launch `ileapp` GUI or `ileapp --help` for installed CLI syntax.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Add a supplied iOS extraction, run relevant modules, and inspect a message artifact with its source database path.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

iOS versions and encrypted backups affect what is available; verify timestamps and raw source.

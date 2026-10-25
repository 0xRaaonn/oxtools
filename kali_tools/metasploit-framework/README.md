# Metasploit Framework

## What it does

Framework for lab exploitation, payloads, and auxiliary modules.

## First steps

Start `msfconsole`; use `search`, `info MODULE`, `show options`, `set RHOSTS`, and `check` where supported.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

For an organizer-provided vulnerable service, inspect module requirements, run `check`, then validate the finding manually before any exploit step.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Modules may alter targets or create sessions; only use within explicit competition scope.

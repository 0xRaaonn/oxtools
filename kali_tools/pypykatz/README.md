# pypykatz

## What it does

Parse Windows credential structures from memory/minidumps in authorized forensic labs.

## First steps

Use `pypykatz -h` and the relevant offline minidump subcommand.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Analyze a supplied LSASS minidump, record any account identifiers, and correlate with the case evidence without exposing secrets.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Results are sensitive and version-dependent; keep dumps and reports private.

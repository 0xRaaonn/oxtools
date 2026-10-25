# cabextract

## What it does

List and extract Microsoft CAB archives.

## First steps

Use `cabextract -l file.cab` and `cabextract -d out file.cab`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

List a supplied CAB, extract into an empty directory, and inspect a recovered DLL or text file.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

A CAB may contain nested cabinets or paths; inspect names and extraction output.

# ALEAPP (Android Logs Events And Protobuf Parser)

## What it does

Parse Android forensic extractions into artifact reports.

## First steps

Launch `aleapp` for the GUI or `aleapp --help` for installed CLI syntax.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Add a supplied Android extraction, select an output folder, run parsing, then inspect report entries for a suspicious app message and its source path.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Artifacts depend on Android/app versions; a parsed timestamp needs timezone and source verification.

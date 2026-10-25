# innoextract

## What it does

Extract files from Inno Setup installers without executing them.

## First steps

Use `innoextract -l installer.exe` and `innoextract -d out installer.exe`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

List a supplied installer, extract its payload, and inspect a bundled config file without running setup.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Not every installer is Inno Setup; extracted scripts/resources may still be active content.

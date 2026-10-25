# checksec

## What it does

Report binary mitigations such as NX, PIE, RELRO, and canaries.

## First steps

Run `checksec --file=./chall` or your installed build's equivalent.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Check an ELF and note `PIE enabled` and `NX enabled`; account for randomized addresses and non-executable stack in your analysis.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Mitigation reports are properties, not exploitability verdicts; verify architecture and runtime.

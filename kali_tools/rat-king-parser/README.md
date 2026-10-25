# rat-king-parser

## What it does

Parse configuration data from supported remote-access malware families for analysis.

## First steps

Read local README and invoke its supported sample input on a copied binary.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Run it on a known supported CTF sample, extract a candidate C2 host/config field, then confirm the bytes in the binary.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

It supports particular families/versions, not arbitrary RATs; configuration may be encrypted or absent.

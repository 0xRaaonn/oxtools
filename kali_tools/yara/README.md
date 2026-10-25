# YARA

## What it does

Match files against rules describing byte/text patterns and conditions.

## First steps

Use `yara rule.yar sample.bin` and `yara -r rule.yar folder`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Write a rule matching an exact challenge marker and a PE header condition, run it on supplied files, then inspect matched bytes in HxD.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

A rule match means its condition was true, not that a file is malicious; broad rules produce false positives.

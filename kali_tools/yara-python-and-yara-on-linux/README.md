# yara-python (and YARA on Linux)

## What it does

Apply YARA rules from Python or the Linux CLI.

## First steps

Use `yara.compile(filepath='rule.yar').match('sample.bin')` in Python or `yara rule.yar sample.bin`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Compile a rule matching a known 4-byte signature, scan a case directory, and print match filenames for manual validation.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Rules are user-supplied code-like patterns; API details and match object fields vary by version.

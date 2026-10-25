# mimikatz

## What it does

Inspect/recover Windows authentication material in authorized memory/lab scenarios.

## First steps

Use the installed tool's local help and an isolated Windows lab; avoid live systems outside scope.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Given a challenge memory artifact, identify which credential material is present and validate findings with timeline/process context rather than assuming plaintext passwords.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

It is highly sensitive and often needs elevation; recovered secrets must not be published.

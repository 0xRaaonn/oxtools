# FakeNet-NG

## What it does

Simulate network services and capture attempted connections from a sample in a lab.

## First steps

Run `fakenet --help` or launch its configured GUI/service in an isolated VM.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Start FakeNet in a lab, run a supplied sample, and inspect logs for DNS/HTTP hosts it attempts to contact.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

The sample still executes; isolation and network routing must be configured correctly.

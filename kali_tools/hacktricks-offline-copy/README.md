# HackTricks (offline copy)

## What it does

Search a local knowledge base of security techniques and reference commands.

## First steps

Use ripgrep against the copied Markdown/HTML: `rg -i 'topic' /path/to/HackTricks`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Find notes for a specific challenge protocol, check the version assumptions, and test a single hypothesis against the lab.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Reference pages may be stale, broad, or inapplicable; verify primary behavior.

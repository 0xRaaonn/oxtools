# sqlmap

## What it does

Test SQL injection in explicitly authorized web challenges.

## First steps

Use `sqlmap -u 'http://lab/item?id=1' -p id --batch` only within scope; inspect `-h` for risk/level options.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

On a local vulnerable training page, confirm a parameter behaves differently under a simple manual test, then let sqlmap test that one parameter and inspect its evidence.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

It can generate heavy traffic and modify data depending on options; constrain target and avoid destructive flags.

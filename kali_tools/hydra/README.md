# Hydra

## What it does

Test login credentials against an authorized service using wordlists.

## First steps

Run `hydra -h` and choose the exact service module and a tiny provided list.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

In a local CTF login lab, test two organizer-supplied candidate passwords, then manually verify any reported success.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Failure strings and lockouts can cause false results or disruption; respect rate limits and scope.

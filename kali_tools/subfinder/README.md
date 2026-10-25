# Subfinder

## What it does

Enumerate subdomains from passive sources for authorized domains.

## First steps

Use `subfinder -d example.test` and inspect `-h` for offline/source settings.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

For an organizer-authorized domain, collect candidate subdomains and verify only those in scope.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

It usually queries external services, so an offline-only event may make it unusable; passive results can be stale.

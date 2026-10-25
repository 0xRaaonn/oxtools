# rustscan

## What it does

Fast port discovery frontend often paired with Nmap.

## First steps

Use `rustscan -a TARGET -- -sV` and check `--help` for rate/batch limits.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Scan one organizer-provided lab host, note open ports, and verify services with Nmap/curl.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

High-speed scanning can overload targets; restrict rate, scope, and ports.

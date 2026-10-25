# Nmap (with Ncat / Nping)

## What it does

Discover hosts/services; Ncat connects/listens; Nping crafts test probes.

## First steps

Use `nmap -sV -p 1-1000 TARGET`, `ncat HOST PORT`, and `nping --help`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Scan one organizer-provided host for the stated ports, connect to a discovered banner with Ncat, and record exact response.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Scans can be noisy or disallowed; restrict hosts, ports, and rate.

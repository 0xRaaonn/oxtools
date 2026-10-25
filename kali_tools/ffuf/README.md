# ffuf

## What it does

Fuzz web paths, parameters, or headers against an authorized HTTP target.

## First steps

Use `ffuf -u http://target/FUZZ -w paths.txt`; inspect `-h` for filters and rate limits.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Scan a local challenge with three candidate paths, compare status/size, and verify a hit with curl.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

A 200 response can be a catch-all page; filter by size/content and limit traffic.

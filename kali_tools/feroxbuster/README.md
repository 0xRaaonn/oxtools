# Feroxbuster

## What it does

Discover web paths recursively in an authorized target.

## First steps

Use `feroxbuster -u http://target/ -w paths.txt` and inspect `--help` for rate/recursion limits.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Against a supplied local web challenge, scan a small wordlist and manually verify a reported `/backup/` path with curl.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Recursive scans can generate heavy traffic; constrain scope, rate, and target.

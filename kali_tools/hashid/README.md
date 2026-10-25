# hashid

## What it does

Guess possible hash types from digest shape.

## First steps

Run `hashid '5d41402abc4b2a76b9719d911017c592'`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

It suggests MD5 among other 32-hex formats; verify using context or known test values before choosing hashcat mode.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Length and alphabet do not uniquely identify a hash.

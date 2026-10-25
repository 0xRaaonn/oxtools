# John the Ripper (jumbo)

## What it does

Audit password hashes and protected-file formats with candidate lists.

## First steps

Use `john --help`, `john --wordlist=words.txt hashes.txt`, and `john --show hashes.txt`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Extract a challenge ZIP hash with the appropriate bundled `*2john` helper, test a small list, and validate by opening the archive.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

The extraction helper and format must match; a recovered candidate needs verification.

# hashcat

## What it does

Test candidate passwords against supported hash formats using CPU/GPU.

## First steps

Use `hashcat --help`, `hashcat --example-hashes`, and `hashcat -m MODE -a 0 hashes.txt words.txt`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Identify a provided hash type, run a small wordlist in the correct mode, and confirm a reported plaintext by rehashing it.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Wrong mode may produce misleading behavior; optimize only after identifying format and salt.

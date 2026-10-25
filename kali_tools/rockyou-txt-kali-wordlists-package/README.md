# rockyou.txt (Kali 'wordlists' package)

## What it does

Common password wordlist for offline candidate testing.

## First steps

Locate the file, often `/usr/share/wordlists/rockyou.txt.gz`, and decompress a working copy with gzip if needed.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Use a small relevant subset against a provided challenge hash with John/hashcat, then verify any recovered candidate.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Large generic lists waste time; wordlists contain sensitive/common passwords and are not proof of a hash type.

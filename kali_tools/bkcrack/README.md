# bkcrack

## What it does

Recover ZIP traditional-encryption keys from known plaintext.

## First steps

Use `bkcrack -h` and provide encrypted ZIP plus a known plaintext file/bytes as documented.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

If an encrypted ZIP contains a known PNG header, use that known plaintext at the correct offset to recover keys, then test extraction on a copy.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

It targets legacy ZipCrypto, not AES ZIP; incorrect plaintext or offset invalidates the attack.

# factordb-python

## What it does

Query FactorDB for known integer factorizations through a Python client.

## First steps

Inspect local module help/README and use its FactorDB API with an integer `n`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

For a small CTF RSA modulus, query whether `n` already has known factors and verify their product equals `n` before computing a key.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

An online query sends the modulus to a third party and may violate offline rules; use only if permitted.

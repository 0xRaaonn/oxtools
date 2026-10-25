# crypto-attacks

## What it does

Collection of cryptanalytic scripts, often Sage/Python, for CTF puzzles.

## First steps

Read the local README and select a script matching the known weakness.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

For an RSA challenge with known `n`, `e`, and ciphertext, choose the specific low-exponent or shared-factor script only after checking its assumptions.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

There is no single universal command; scripts may require SageMath and exact input formatting.

# padding-oracle-attacker

## What it does

Automate a CBC padding-oracle test against an explicitly vulnerable lab endpoint.

## First steps

Read installed README/§--help§ to define ciphertext, oracle request, and valid/invalid response condition.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

For a local challenge API returning distinguishable padding errors, confirm one-byte response behavior before asking the tool to recover more bytes.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Many false signals arise from authentication, rate limits, or response parsing; do not use on unrelated services.

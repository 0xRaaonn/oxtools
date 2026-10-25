# Python 2.7

## What it does

Run legacy scripts that require Python 2 syntax/runtime.

## First steps

Use `python2 --version` and `python2 legacy.py` only after inspecting the script.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

A challenge helper fails on Python 3 because of `print` syntax; run it in Python 2 and compare its output with a manual calculation.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Python 2 is end-of-life; avoid installing untrusted packages or using it for network-facing services.

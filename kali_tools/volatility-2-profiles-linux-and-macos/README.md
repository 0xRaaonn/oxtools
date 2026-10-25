# Volatility 2 profiles (Linux and macOS)

## What it does

Provide symbols/types required for Volatility 2 Linux/macOS images.

## First steps

Place the matching profile ZIP in the configured profile directory and inspect `vol.py --info`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

A Linux memory image fails without symbols; add the exact kernel-build profile and rerun `linux_pslist`.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

A profile from a similar but different kernel can yield wrong or empty results.

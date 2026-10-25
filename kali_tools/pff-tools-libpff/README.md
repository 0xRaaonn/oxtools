# pff-tools (libpff)

## What it does

Read/export Outlook PST/OST mail stores.

## First steps

Use `pffinfo mailbox.pst` and `pffexport -t out mailbox.pst` where installed.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Export a supplied PST, inspect a recovered mail attachment and correlate sender/time with headers.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Large stores and partial corruption can omit records; export into an empty directory.

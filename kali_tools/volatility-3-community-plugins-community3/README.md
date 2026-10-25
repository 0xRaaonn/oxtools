# Volatility 3 community plugins (community3)

## What it does

Add third-party plugins to Volatility 3.

## First steps

Use `vol -p /path/to/community3 -h` to list plugins, plus symbols if required.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Run an added artifact plugin on a supplied memory image and corroborate its output with core Volatility plugins.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Plugin API compatibility changes; third-party code executes locally, so inspect source and version.

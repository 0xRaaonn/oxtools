# Volatility 2 community plugins

## What it does

Extend Volatility 2 with third-party memory-analysis plugins.

## First steps

Use `vol.py --plugins=/path/to/plugins --info` to list compatible additions.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Load a supplied plugin, confirm it appears in `--info`, run it on a copied memory image, and verify any hit with core plugins.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Third-party code executes in your analysis environment and may target narrow versions; inspect source.

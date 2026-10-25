# libesedb tools

## What it does

Inspect Extensible Storage Engine databases such as Windows WebCache.

## First steps

Use `esedbinfo file.dat` and `esedbexport -t out file.dat` where installed.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Export a supplied WebCache ESE database, locate a URL record, and correlate its timestamp with browser artifacts.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Database files may require related logs for full recovery; exported values need schema interpretation.

# FQLite

## What it does

Recover SQLite records, including deleted/free-list remnants, through a GUI or Java tool.

## First steps

Open a copy of the SQLite database and inspect recovered tables/records.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

A normal query omits a deleted chat row; FQLite recovers a candidate row, which you validate against page bytes and timestamps.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Deleted record recovery is best-effort; WAL and page reuse affect results.

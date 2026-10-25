# sqlite3

## What it does

Query and inspect SQLite databases from the terminal.

## First steps

Use `sqlite3 database.db`; inside `.tables`, `.schema`, and `SELECT * FROM table LIMIT 10;`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Open a copied chat database, inspect schema, then select messages in timestamp order and verify source row IDs.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Copy WAL/SHM files too when present; opening databases may create journal files.

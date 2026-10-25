# DB Browser for SQLite

## What it does

Inspect and edit SQLite databases through a GUI.

## First steps

Open a copy; use Browse Data, Database Structure, and Execute SQL.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Open `app.db`, list tables, then query `SELECT * FROM users LIMIT 10;` to inspect challenge records.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Opening writable databases can alter journal state; keep a forensic copy and check WAL files.

# SQLCipher Community Edition — CLI

## What it does

Open SQLite databases encrypted with SQLCipher when the key is known or recovered.

## First steps

Use `sqlcipher encrypted.db`, then `PRAGMA key='known-key';` and `SELECT name FROM sqlite_master;`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

With a supplied key, open an encrypted app database and query a message table; verify decryption by a sane schema.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Wrong key often appears as “file is not a database”; cipher compatibility/settings can differ.

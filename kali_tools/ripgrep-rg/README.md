# ripgrep (rg)

## What it does

Fast recursive text search with regex and file filters.

## First steps

Use `rg -n -i 'flag|secret' folder`, `rg --files folder`, and `rg -g '*.py' 'password' .`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Search extracted source for a validation string, then open the exact reported file and line to trace code.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Binary files and hidden files may be skipped by default; add options when needed.

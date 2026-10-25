# Python 3.11 (via uv)

## What it does

Run modern Python scripts and standard-library analysis in a pinned interpreter.

## First steps

Use `uv python list`, `uv run --python 3.11 script.py`, or `uv venv --python 3.11 .venv`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Decode a hex challenge string with `python -c "print(bytes.fromhex('666c6167'))"` in the uv-managed environment; output is `b'flag'`.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Quote shell commands carefully; distinguish bytes from Unicode and record package versions.

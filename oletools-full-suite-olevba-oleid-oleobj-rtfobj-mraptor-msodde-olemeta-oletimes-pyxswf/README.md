# oletools (full suite: olevba, oleid, oleobj, rtfobj, mraptor,   msodde, olemeta, oletimes, pyxswf)

## What it does

Inspect Office/RTF documents for macros, objects, metadata, and suspicious content.

## First steps

Use `oleid sample.doc`, `olevba sample.doc`, and each tool's `-h`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Run oleid on a supplied DOC, then olevba to extract VBA; inspect an encoded string and confirm its decode in Python.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Macro indicators are not proof of execution; avoid enabling macros in Office.

# mupdf-tools (mutool)

## What it does

Inspect and transform PDF/XPS and related documents from the CLI.

## First steps

Use `mutool info file.pdf`, `mutool draw -o page-%d.png file.pdf`, and `mutool show file.pdf trailer`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Render PDF pages to images to inspect a hidden graphic, then use `mutool show` to locate an embedded object referenced by the page.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Rendering may differ from other viewers; preserve the original object structure.

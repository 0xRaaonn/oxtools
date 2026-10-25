# Didier Stevens Suite (pdfid.py, pdf-parser.py, oledump.py and   others)

## What it does

Analyze PDF, OLE, and document structures with focused Python scripts.

## First steps

Use `python pdfid.py suspicious.pdf`; then `python pdf-parser.py -h` or `python oledump.py -h`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Run pdfid to count `/JavaScript` and `/OpenAction` tokens, then use pdf-parser to inspect the referenced object rather than assuming it executes.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Token counts can be hidden/obfuscated or benign; parser versions and script names vary.

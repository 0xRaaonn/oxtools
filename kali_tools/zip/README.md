# zip

## What it does

Create and update ZIP archives.

## First steps

Use `zip output.zip file.txt` and `zip -r output.zip folder/`; use unzip to inspect.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Package extracted challenge artifacts for local organization, then `unzip -t output.zip` to verify integrity.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

ZIP password options often use weak ZipCrypto; do not rely on them for confidentiality.

# stegseek

## What it does

Test passphrase candidates for steghide payloads using a wordlist.

## First steps

Use `stegseek image.jpg words.txt` and inspect `--help` for output options.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

On a challenge JPEG known to contain steghide data, use a short clue-based list and verify the extracted file.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

It targets steghide format specifically; a failed wordlist does not prove no payload.

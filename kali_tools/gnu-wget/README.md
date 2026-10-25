# GNU Wget

## What it does

Download files and mirror permitted web content.

## First steps

Use `wget -O page.html URL` or `wget --spider URL` to test retrieval.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Fetch a challenge-hosted text file to a known path and compare its SHA-256 with the provided checksum.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Recursive mirroring can fetch much more than intended; restrict target and depth.

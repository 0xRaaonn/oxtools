# SecLists

## What it does

Collection of wordlists for discovery, fuzzing, and testing.

## First steps

Locate `/usr/share/seclists` and choose a short list appropriate to the target.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Use a small web-content list with ffuf against an authorized local site, then verify a discovered path manually.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Large lists create excessive traffic and false leads; select by task and rate limit.

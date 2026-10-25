# jwt_tool

## What it does

Inspect and test JSON Web Tokens in an authorized web lab.

## First steps

Run `jwt_tool -h` and provide a supplied token as documented.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Decode a lab JWT, compare header/payload with server behavior, and test only an organizer-intended weakness.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Payload contents are not trusted merely because Base64 decodes; signature validation controls authenticity.

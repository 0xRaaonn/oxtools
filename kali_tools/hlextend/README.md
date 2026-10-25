# hlextend

## What it does

Demonstrate hash length-extension attacks against vulnerable prefix-MAC constructions.

## First steps

Use `hlextend --help` or the Python library's local API.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

For a lab token using SHA-1(secret || message), test candidate secret lengths and append an authorized parameter, then verify against the lab endpoint.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

HMAC is not vulnerable to this attack; hash type, padding, and URL encoding must match.

# curl

## What it does

Send HTTP requests and inspect responses from the terminal.

## First steps

Use `curl -i https://target/`, `curl -sS -o page.html URL`, or `curl -X POST -d 'x=1' URL`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Request a challenge endpoint with `curl -i`, record status/headers, then alter one parameter and compare responses.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Shell quoting, redirects, cookies, and TLS options affect results; use only competition targets.

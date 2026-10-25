# Katana

## What it does

Crawl authorized web targets and extract discovered URLs.

## First steps

Run `katana -u http://target/ -d 1` and inspect `-h` for rate/scope controls.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Crawl a local challenge at depth 1, inspect a discovered API path, and verify it manually with curl.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

A crawler may follow links outside scope and generate load; constrain domains and depth.

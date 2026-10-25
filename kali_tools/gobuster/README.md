# Gobuster

## What it does

Discover HTTP paths, DNS names, or virtual hosts using wordlists.

## First steps

Use `gobuster dir -u http://target/ -w words.txt`; inspect `gobuster --help`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Against a local lab site, a small list finds `/admin`; verify the response with curl and distinguish it from catch-all 200 pages.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Limit concurrency and scope; DNS/vhost modes need different options and interpretation.

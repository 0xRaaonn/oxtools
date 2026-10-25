# Gitleaks

## What it does

Scan repositories and files for likely secrets.

## First steps

Run `gitleaks detect --source .` or installed version's `git`/`dir` subcommand; check `gitleaks --help`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Scan a provided Git repo; a finding points to a token-like string in a commit, which you inspect via `git show`.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Matches can be false positives; scanning history can expose private secrets in reports.

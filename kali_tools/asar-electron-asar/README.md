# asar (@electron/asar)

## What it does

List and extract Electron ASAR application bundles.

## First steps

Use `asar list app.asar` and `asar extract app.asar extracted` (or `npx asar` when packaged that way).

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

List a supplied `app.asar`, extract it, and inspect `package.json` and JavaScript for a local validation constant.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

ASAR is an archive, not encryption; extracted scripts may still be minified or obfuscated.

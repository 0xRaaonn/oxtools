# Node.js (with npm)

## What it does

Run JavaScript and manage packages.

## First steps

Use `node --version`, `node script.js`, `npm --version`, and `npm ci` in a trusted project.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Run a tiny script that decodes `Buffer.from('ZmxhZw==','base64').toString('utf8')` and prints `flag`.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

npm install scripts execute code and can use network; inspect package manifests.

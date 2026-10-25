# Frida

## What it does

Instrument running programs by injecting JavaScript hooks in an authorized lab.

## First steps

Use `frida-ps -U` for a connected device or `frida -f ./app -l hook.js` for a local program, matching platform setup.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Hook a local challenge's comparison function, print its arguments, and verify the observed bytes with static analysis.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Hooks alter timing/behavior and execute target code; attach only to your own lab process.

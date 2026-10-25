# hcxtools

## What it does

Convert and inspect Wi-Fi capture formats used in authorized password auditing.

## First steps

Use `hcxpcapngtool -h` and inspect a provided capture's output options.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Convert a supplied handshake capture to a hashcat-compatible file, then test only the provided small candidate list.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Conversion output is not proof a valid handshake exists; wireless capture and cracking must stay within contest scope.

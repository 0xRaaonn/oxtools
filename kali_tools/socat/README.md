# socat

## What it does

Relay data between sockets, files, and terminals.

## First steps

Use `socat -h`; e.g. `socat - TCP:127.0.0.1:9000` to interact with a lab service.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Connect to an organizer-provided TCP challenge and observe its prompt, then send test input from the terminal.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Bidirectional relays can hang or expose listeners; bind only to intended interfaces.

# Docker Engine and Compose plugin

## What it does

Run isolated containers and multi-service lab stacks.

## First steps

Use `docker version`, `docker compose version`, and `docker compose up` in a trusted challenge project.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Start an organizer-provided local web challenge with `docker compose up -d`, then inspect `docker compose ps` and logs before connecting.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Compose files can mount host paths, expose ports, and run arbitrary images; inspect before starting.

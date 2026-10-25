# strace

## What it does

Trace Linux system calls made by a process.

## First steps

Run `strace -o trace.txt ./chall` or `strace -e openat,read,write ./chall`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Run a challenge executable and see it attempts to open `secret.txt`; provide a controlled test file and observe changed behavior.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Tracing executes code and may perturb timing; filtered traces can omit relevant syscalls.

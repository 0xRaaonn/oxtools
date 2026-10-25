# angr

## What it does

Symbolically execute native binaries to solve path constraints.

## First steps

In Python, start with `import angr; p=angr.Project("chall", auto_load_libs=False)` and use SimulationManager.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

For a tiny binary with success/fail print paths, use `simgr.explore(find=success_addr, avoid=failure_addr)` and inspect the found stdin bytes.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Symbolic execution can explode in state count; addresses, input modeling, and external calls must be correct.

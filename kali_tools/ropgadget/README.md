# ROPgadget

## What it does

Search binaries for return-oriented programming instruction sequences.

## First steps

Use `ROPgadget --binary ./chall` and inspect `--help` for filtering.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Find a `pop rdi; ret` gadget in a lab ELF, then confirm its address and bytes in objdump/Ghidra.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Reported gadgets depend on architecture/offsets and may be unusable under PIE/ASLR or constraints.

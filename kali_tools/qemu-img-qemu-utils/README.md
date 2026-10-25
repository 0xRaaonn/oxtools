# qemu-img (qemu-utils)

## What it does

Inspect and convert virtual disk image formats without booting them.

## First steps

Use `qemu-img info disk.qcow2` and `qemu-img convert -O raw disk.qcow2 disk.raw`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Convert a supplied QCOW2 copy to raw, then analyze partitions with The Sleuth Kit.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Conversion needs free disk space; backing files/snapshots may be required for a complete image.

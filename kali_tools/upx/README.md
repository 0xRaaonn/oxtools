# UPX

## What it does

Pack/unpack executables using UPX format.

## First steps

Use `upx -t sample.exe` to test and `upx -d -o unpacked.exe sample.exe` to unpack a copy.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

DIE suggests UPX, UPX test passes, and the unpacked executable exposes readable strings for Ghidra.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Not all packers are UPX; a modified header can defeat normal unpacking, and unpacked code is still untrusted.

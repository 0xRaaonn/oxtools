# GCC, G++ and build tools (build-essential, make, CMake,   pkg-config)

## What it does

Compile C/C++ code and build challenge helpers.

## First steps

Use `gcc -Wall -O0 demo.c -o demo`, `g++ demo.cpp -o demo`, `make`, or `cmake -S . -B build`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Compile a tiny parser for a custom binary record and compare its output with Python's struct unpacking.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Makefiles/CMake scripts can execute arbitrary commands; inspect supplied build files first.

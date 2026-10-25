# SageMath

## What it does

Computer algebra system for crypto and number theory.

## First steps

Start `sage` or run `sage solve.sage`; use `factor`, modular rings, matrices, and polynomial methods.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

For toy RSA `n=55`, factor it and compute `inverse_mod(3,40)` to get a private exponent 27; verify `(m^3)^27 mod 55 == m` for valid messages.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Mathematical assumptions matter; Sage syntax and integer/ring types can change results.

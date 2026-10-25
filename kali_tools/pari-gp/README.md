# PARI/GP

## What it does

Interactive number theory and algebra system for crypto math.

## First steps

Start `gp`; use `factor(n)`, `isprime(n)`, `Mod(a,n)^e`, and `lift(...)`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

In a toy RSA challenge with `n=55`, `factor(55)` returns 5 and 11; derive φ=40 and solve for the inverse exponent.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Large secure RSA moduli are not tractable just because a factor command exists; integer types and modulus matter.

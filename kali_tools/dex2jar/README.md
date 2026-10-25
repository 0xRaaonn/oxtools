# dex2jar

## What it does

Convert Android DEX bytecode to Java JAR for inspection.

## First steps

Use `d2j-dex2jar classes.dex -o classes.jar` or installed script variant.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Extract `classes.dex` from an APK, convert it, and open the JAR in Bytecode Viewer to inspect a validator.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Conversion is lossy for some features/obfuscation; JADX or smali may be clearer.

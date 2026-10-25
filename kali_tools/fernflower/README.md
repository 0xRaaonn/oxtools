# Fernflower

## What it does

Decompile Java class/JAR bytecode to Java-like source.

## First steps

Run the installed Fernflower JAR with its documented syntax, usually `java -jar fernflower.jar input.jar output_dir`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Decompile a challenge JAR and inspect a string transformation in the resulting Java files, then compare with raw bytecode.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Decompiled Java is approximate and can misrepresent obfuscated control flow.

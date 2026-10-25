# Apktool

## What it does

Decode Android APK resources/smali and rebuild modified copies.

## First steps

Use `apktool d app.apk -o decoded` and `apktool b decoded -o rebuilt.apk`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Decode a challenge APK, read `AndroidManifest.xml` and search smali for a hard-coded URL; verify the same URL in JADX.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Rebuilt APKs need signing before installation; resource decoding is not equivalent to decompiling original Java source.

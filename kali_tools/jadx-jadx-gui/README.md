# jadx (jadx-gui)

## What it does

Decompile Android APK/DEX into Java-like source and inspect resources.

## First steps

Run `jadx-gui app.apk` or `jadx -d out app.apk`.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Open an APK, search for a flag-check method, inspect its string constants, and verify in smali if control flow is ambiguous.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Obfuscation and Kotlin lowering make output approximate; do not run the APK on your main device.

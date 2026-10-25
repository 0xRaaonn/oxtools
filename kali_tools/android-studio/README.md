# Android Studio

## What it does

Inspect and develop Android applications, APK projects, and emulator-based tests.

## First steps

Open a project or APK; use Logcat and Device Manager for authorized test devices.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Open a provided APK with APK Analyzer, inspect manifest permissions and bundled assets, then compare with jadx's decompiled code.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

Building/running an APK executes code; inspect statically first and use an isolated emulator.

# .NET SDK

## What it does

Build and inspect managed .NET projects and assemblies.

## First steps

Run `dotnet --info` and `dotnet new console -o Demo`; use `dotnet build` inside a project.

Use the installed program's help screen or local README to confirm option names before adapting a command. Keep supplied evidence unchanged and place outputs in a separate case folder.

## Worked example

Create a console project, set Program.cs to print `Convert.FromBase64String("ZmxhZw==")` as UTF-8, then `dotnet run`; output is `flag`.

## How to interpret it

Treat a reported hit, recovered file, or successful run as one observation. Check the output against the original input, record the exact command or GUI steps, and verify a candidate flag or finding with a second view where possible.

## Pitfalls

The SDK executes build scripts and package restore can use the network; inspect untrusted projects before building.

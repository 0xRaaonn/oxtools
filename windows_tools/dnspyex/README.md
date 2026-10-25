# dnSpyEx (dnSpy)

**Use:** inspect and debug managed .NET assemblies, including C#, VB.NET, and IL. It is the maintained continuation of dnSpy.

**Workflow:** Open an `.exe` or `.dll`. Assembly Explorer lists namespaces, classes, methods, fields, and resources. Select a method to view decompiled C# or IL. Search for strings, method names, and references. Inspect resources for embedded files. For dynamic work, start the assembly under the debugger, set breakpoints, and inspect locals and call stack.

**CTF approach:** Find entry point and input validation, trace transformations, and reproduce the logic in Python or a small test harness. If decompilation looks suspicious, compare IL with decompiled C#; obfuscation can mislead high-level output.

**Pitfalls:** Debugging executes the assembly. Native PE files are not .NET assemblies and need Ghidra/x64dbg instead. Mixed-mode or newer runtime features may need compatible .NET runtimes. Save modified assemblies under a new name.

Source: [dnSpyEx project](https://github.com/dnSpyEx/dnSpy).

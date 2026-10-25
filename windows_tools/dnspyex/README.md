# dnSpyEx (dnSpy)

**Use:** inspect and debug managed .NET assemblies, including C#, VB.NET, and IL. It is the maintained continuation of dnSpy.

**Workflow:** Open an `.exe` or `.dll`. Assembly Explorer lists namespaces, classes, methods, fields, and resources. Select a method to view decompiled C# or IL. Search for strings, method names, and references. Inspect resources for embedded files. For dynamic work, start the assembly under the debugger, set breakpoints, and inspect locals and call stack.

**CTF approach:** Find entry point and input validation, trace transformations, and reproduce the logic in Python or a small test harness. If decompilation looks suspicious, compare IL with decompiled C#; obfuscation can mislead high-level output.

**Pitfalls:** Debugging executes the assembly. Native PE files are not .NET assemblies and need Ghidra/x64dbg instead. Mixed-mode or newer runtime features may need compatible .NET runtimes. Save modified assemblies under a new name.

Source: [dnSpyEx project](https://github.com/dnSpyEx/dnSpy).

## Worked example: inspect a .NET validator

Open `Challenge.exe` in dnSpyEx. Find `Main`, follow the call handling user input, and view the validator in C# and IL. Suppose it checks `Convert.ToBase64String(Encoding.UTF8.GetBytes(input))` against a constant: decode that constant with CyberChef, then test the resulting candidate in the original executable. If decompiled C# looks inconsistent, use the IL instructions to confirm the exact call order.

## More CTF scenario questions

### A .NET program stores a Base64 constant. Is decoding it enough?

Trace how the decoded bytes are used in the validator. They might be an XOR key, salt, or decoy rather than the final answer; test the original assembly.

### dnSpyEx C# output has a strange branch. How can I confirm it?

Switch the method view to IL and inspect comparison and branch instructions, then debug with sample input if needed. Obfuscation can make decompiled C# unreliable.

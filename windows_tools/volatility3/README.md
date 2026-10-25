# Volatility 3

**Use:** analyze acquired RAM images for processes, command lines, network state, files, registry, and other OS artifacts.

**Commands:** `vol -h` lists options/plugins (some installs use `python vol.py`). Use `vol -f memory.raw windows.info`, `vol -f memory.raw windows.pslist`, `vol -f memory.raw windows.pstree`, `vol -f memory.raw windows.cmdline`, `vol -f memory.raw windows.netscan`. For a plugin's options, use `vol windows.pslist -h`. `-o outputdir` selects output for plugins that dump files; check exact plugin options before dumping. Linux/macOS plugins require suitable symbols and compatible images.

**CTF workflow:** Identify OS/build with info, enumerate process trees and command lines, correlate PIDs with network connections, then inspect suspicious process memory or file objects with targeted plugins. Record the image hash and plugin output.

**Pitfalls:** Volatility 3 plugin names and flags differ from Volatility 2. Symbols may need downloads or a local cache. A missing process in pslist does not prove absence; cross-check with scan-style plugins and acquisition timing. Memory images can contain sensitive data.

Sources: [Volatility 3 README](https://github.com/volatilityfoundation/volatility3), [documentation](https://volatility3.readthedocs.io/en/latest/).

## Worked example: suspicious process in RAM

Run `vol -f memory.raw windows.info` to identify the image, then `vol -f memory.raw windows.pstree`. Suppose `powershell.exe` appears under an unusual parent PID `4120`. Run `vol -f memory.raw windows.cmdline` and `vol -f memory.raw windows.netscan`, then correlate that PID with a command line and remote connection. A single plugin result is a lead; verify with timestamps and related artifacts.

## More CTF scenario questions

### `windows.pslist` misses a process mentioned in logs. Where else can I look?

Try process-tree and scan-style plugins available in your version, then correlate PIDs and timestamps. A terminated or unlinked process may not appear in the active list.

### `windows.netscan` shows an IP with no obvious owner. What next?

Compare PID/process tree, command line, handles or sockets where available, and packet/log evidence. Memory structures can be stale; do not assign the connection to a process from PID alone.

# Volatility 3

**Use:** analyze acquired RAM images for processes, command lines, network state, files, registry, and other OS artifacts.

**Commands:** `vol -h` lists options/plugins (some installs use `python vol.py`). Use `vol -f memory.raw windows.info`, `vol -f memory.raw windows.pslist`, `vol -f memory.raw windows.pstree`, `vol -f memory.raw windows.cmdline`, `vol -f memory.raw windows.netscan`. For a plugin's options, use `vol windows.pslist -h`. `-o outputdir` selects output for plugins that dump files; check exact plugin options before dumping. Linux/macOS plugins require suitable symbols and compatible images.

**CTF workflow:** Identify OS/build with info, enumerate process trees and command lines, correlate PIDs with network connections, then inspect suspicious process memory or file objects with targeted plugins. Record the image hash and plugin output.

**Pitfalls:** Volatility 3 plugin names and flags differ from Volatility 2. Symbols may need downloads or a local cache. A missing process in pslist does not prove absence; cross-check with scan-style plugins and acquisition timing. Memory images can contain sensitive data.

Sources: [Volatility 3 README](https://github.com/volatilityfoundation/volatility3), [documentation](https://volatility3.readthedocs.io/en/latest/).

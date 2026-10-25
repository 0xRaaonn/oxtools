# Eric Zimmerman's Tools

**Use:** a Windows forensic suite of separate parsers and viewers. Choose the tool by artifact type rather than treating the suite as one command.

| Artifact | Tool | What to look for |
| --- | --- | --- |
| `.evtx` event logs | EvtxECmd | event IDs, users, process/service activity |
| NTFS `$MFT` and USN journal | MFTECmd | filenames, timestamps, file activity |
| Prefetch `.pf` | PECmd | program execution traces |
| Shortcuts `.lnk` | LECmd | target paths, volumes, timestamps |
| Jump Lists | JLECmd | recent files/app activity |
| Registry hives | RECmd, Registry Explorer | persistence, settings, user activity |
| Amcache | AmcacheParser | program metadata/execution leads |
| SRUM | SrumECmd | application/network usage |
| ShellBags | SBECmd, ShellBags Explorer | folder browsing traces |
| Recycle Bin | RBCmd | deletion records |
| SQLite artifacts | SQLECmd | app/browser databases |
| CSV timelines | Timeline Explorer | filter/sort parser results |

**CLI pattern (PowerShell):** `.\EvtxECmd.exe -f .\Security.evtx --csv .\out`; `.\EvtxECmd.exe -d .\Logs --csv .\out`; `.\MFTECmd.exe -f '.\$MFT' --csv .\out`; `.\PECmd.exe -d .\Prefetch --csv .\out`. Use `<tool>.exe --help` for each parser; options vary. Quoting `$MFT` in single quotes matters in PowerShell because `$` starts a variable.

**Workflow:** Identify the artifact, run the matching parser against a copy, export CSV/JSON, then filter by time, user, path, or process. Correlate artifacts: Prefetch suggests execution, LNK/Jump Lists suggest file access, logs can confirm related events. Normalize timezones before building a timeline.

**Pitfalls:** Artifacts are incomplete and can be cleaned or overwritten. A Prefetch entry does not by itself prove user intent; a registry key's timestamp may reflect a container change rather than the exact action. Some tools need maps/config files kept next to the executable. Check installed tool versions and per-tool help.

Sources: [official tool catalog](https://ericzimmerman.github.io/), [EvtxECmd documentation](https://github.com/EricZimmerman/evtx).

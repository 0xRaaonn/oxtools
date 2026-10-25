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

## Worked example: correlate execution evidence

Given `Security.evtx` and a Prefetch folder, run `.\EvtxECmd.exe -f .\Security.evtx --csv .\out` and `.\PECmd.exe -d .\Prefetch --csv .\out` in PowerShell. Open the CSVs in Timeline Explorer or filter them with Python. If Prefetch shows `TOOL.EXE` and an event log shows a related process event near the same time, correlate timestamps, path, user, and host before concluding what ran. Prefetch alone is not a complete execution history.

## More CTF scenario questions

### A Prefetch file exists for a program. Does that prove a person opened it?

Use PECmd to parse path/run information, then correlate event logs, LNK/Jump Lists, and user context. Prefetch supports execution inference but does not establish user intent by itself.

### An EVTX event and MFT change occur at the same clock time. Can I join them directly?

Parse with EvtxECmd and MFTECmd, normalize timezone and timestamp precision, then compare host, path, user, and event meaning. Similar timestamps can be coincidental.

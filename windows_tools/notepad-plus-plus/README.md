# Notepad++

**Use:** inspect and edit text, logs, scripts, hex dumps, and encoded data on Windows. It is a text editor, not a binary editor.

**Workflow:** Open a copy. View → Show Symbol → Show All Characters reveals tabs, spaces, and line endings. Search → Find in Files searches a case directory; Search → Mark can highlight repeated terms. Encoding menu shows UTF-8, ANSI/code page, UTF-16, and conversion options. Language selection gives syntax highlighting, not execution. Compare plugins may or may not be installed.

**CTF examples:** Search a log for a flag format or suspicious URL; use regular expressions in Find with Search Mode → Regular expression; inspect JSON or scripts without executing them. Use Python/jq for structured transformations.

**Pitfalls:** Opening/saving a binary file can corrupt bytes. Converting encoding or line endings alters files. Huge logs may slow the editor. A displayed “ANSI” file depends on the system code page; verify byte encoding if characters look wrong.

Source: [Notepad++ user manual](https://npp-user-manual.org/).

## Worked example: identify invisible characters

Open `message.txt` in Notepad++, enable View → Show Symbol → Show All Characters, and inspect a suspicious line. If it contains tabs/spaces after an apparent flag, use Search → Find with a regular expression such as `[ \t]+$` to find trailing whitespace. Compare with the original bytes in HxD before editing; whitespace can be the payload in a CTF challenge.

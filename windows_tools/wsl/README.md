# Windows Subsystem for Linux (WSL)

**Use:** run Linux CLI tools on Windows.

**Basics:** From PowerShell: `wsl --list --verbose`, `wsl`, or `wsl --distribution Ubuntu`. From WSL: `pwd`, `ls -la`, `cd /mnt/c/Users/<you>/Downloads`. A Windows `C:\Users\...\file` becomes `/mnt/c/Users/.../file`. Run a Linux command from PowerShell with `wsl -- <command>`.

**CTF workflow:** Work in a dedicated case folder and quote paths containing spaces. Check installation with `command -v binwalk` and use `man <tool>` or `<tool> --help` for local help. WSL has its own PATH and packages; installing on Windows does not automatically install a Linux version.

**Pitfalls:** Windows and WSL can have different permissions, routes, line endings, and tool versions. WSL2 has a virtual network; test VPN connectivity from the environment you actually use. Large files under `/mnt/c` can be slower than in the Linux filesystem.

Source: [Microsoft WSL docs](https://learn.microsoft.com/windows/wsl/).

## Worked example: open a Windows file from Linux

If the file is `C:\Users\Ada\Downloads\sample.bin`, start WSL and run `xxd -l 32 '/mnt/c/Users/Ada/Downloads/sample.bin'`. The displayed hex bytes should match HxD on Windows. If the command says file not found, check the Windows username, drive letter, and exact capitalization/path; WSL paths use forward slashes.

# Windows CTF tool field guide

This is an offline first reference for the 39 tools on your allowed list. Each tool has its own `README.md` with purpose, first steps, examples, output interpretation, and mistakes to avoid. Examples assume you are analyzing files and systems supplied by your competition. Tool behavior can differ by installed version; run the tool's built in `--help`, `-h`, or GUI Help menu when an option differs.

Read the [offline CTF primer](OFFLINE_CTF_PRIMER.md) for shell syntax, file signatures, byte order, and complete workflows that combine tools.

Every tool guide ends with a **Worked example** showing sample input, a command or GUI action, and how to check the result.

Each guide also has **two additional CTF scenario questions**. For problems that use several tools, see the [practice scenarios](PRACTICE_SCENARIOS.md).

## Before you begin

- Keep originals untouched. Copy evidence into a working folder and save extracted data into a separate output folder. In PowerShell: `Copy-Item .\evidence.bin .\work\evidence.bin`; `Get-FileHash .\evidence.bin -Algorithm SHA256`.
- PowerShell uses `C:\path\file`; WSL uses `/mnt/c/path/file`. Quote paths containing spaces. Most examples below are in the shell named in their guide.
- PowerShell's `>` may change how native program output is encoded. For binary output use a tool's output-file option or `cmd /c` redirection. In WSL, shell redirection preserves raw bytes.
- For downloaded utilities, verify the publisher and hash before running. Do not open suspicious executables just to inspect them; use static tools first.
- Work through the file type: inspect bytes and metadata, identify embedded objects, extract copies, then decode or reverse. A plausible string is a lead, not proof; verify it against file structure or challenge context.
- Some listed tools require installation or dependencies not included in the allowlist (for example Ruby for zsteg). Use a provided copy if available and check competition rules before installing anything.

## Guides by task

| Task | Guides |
| --- | --- |
| Decode and inspect bytes | [CyberChef](cyberchef/README.md), [Python 3](python-3/README.md), [xxd](xxd/README.md), [HxD](hxd/README.md), [strings](strings/README.md), [jq](jq/README.md) |
| Images, PDFs, archives | [zsteg](zsteg/README.md), [binwalk](binwalk/README.md), [ExifTool](exiftool/README.md), [ZBar](zbar/README.md), [PDF viewer](pdf-viewer/README.md), [pdftotext](pdftotext/README.md), [qpdf](qpdf/README.md), [xz](xz/README.md) |
| Network and web | [Wireshark](wireshark/README.md), [TShark](tshark/README.md), [Zeek](zeek/README.md), [Burp Suite Community](burp-suite-community/README.md), [Chrome](google-chrome/README.md), [OpenVPN](openvpn-client/README.md), [can-utils](can-utils/README.md), [cannelloni](cannelloni/README.md) |
| Reversing and crypto | [Ghidra](ghidra/README.md), [gdb](gdb/README.md), [objdump](objdump/README.md), [llvm-mc](llvm-mc/README.md), [x64dbg](x64dbg/README.md), [dnSpyEx](dnspyex/README.md), [OpenSSL](openssl/README.md), [RsaCtfTool](rsactftool/README.md) |
| Disk and memory forensics | [The Sleuth Kit](the-sleuth-kit/README.md), [Autopsy](autopsy/README.md), [fsck.fat](fsck-fat/README.md), [Volatility 3](volatility3/README.md), [OpenSSH Session Key Recovery](openssh-session-key-recovery/README.md), [Eric Zimmerman's Tools](eric-zimmerman-tools/README.md) |
| Environment | [WSL](wsl/README.md), [uv](uv/README.md), [Notepad++](notepad-plus-plus/README.md) |

## Quick decision path

1. **Unknown file:** inspect extension, magic bytes with `xxd`, readable strings with `strings`, and metadata with `exiftool` where relevant.
2. **Image or document:** inspect visually; try `zsteg` only for PNG/BMP, `zbarimg` for barcode/QR, and PDF tools for text, attachments, and structure.
3. **PCAP:** start with Wireshark or TShark; inspect protocol conversations and exported objects. Use Zeek for broad connection and file logs.
4. **Executable:** identify architecture and format; examine with Ghidra/objdump/strings before dynamic debugging in x64dbg or gdb.
5. **Disk or memory image:** use forensic tools against a copy. Know whether you have a whole disk, a partition, or a raw memory dump before choosing offsets or plugins.

## Symbols used in commands

`<file>`, `<path>`, `<interface>`, and `<PID>` are placeholders. Do not type angle brackets. `#` at the start of a WSL line is a comment. Windows examples use PowerShell unless labeled otherwise. `--help` output from your installed version is the final authority for exact flags.

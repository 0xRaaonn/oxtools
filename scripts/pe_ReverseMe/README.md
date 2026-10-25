# PE reverse engineering helper

`pe_reversing_helper.py` is a terminal tool for examining Windows PE reverse engineering challenges. It reads an `.exe` directly or extracts one from a ZIP archive. It does **not** run the executable.

The automatic solver targets the pattern in `ReverseMe.zip`: renamed UPX sections, a key checked in separate pieces, and flag text decoded by XOR. For other challenges, the unpacked file and reported strings can still give you a starting point for manual analysis.

## Requirements

- Python 3
- The Python packages `pefile` and `capstone`
- The `upx` command for unpacking UPX files

Install the Python packages with:

```bash
python3 -m pip install pefile capstone
```

Install UPX with your system package manager, then check that it is available:

```bash
upx --version
```

UPX is optional for reading an already unpacked executable. If it is unavailable, the script analyzes the input as it is.

## Use it

Run the included challenge from the directory containing the script and ZIP:

```bash
python3 pe_reversing_helper.py ReverseMe.zip --password novirus
```

Analyze an executable directly:

```bash
python3 pe_reversing_helper.py challenge.exe
```

If a ZIP contains several executables, select one by its full path inside the archive:

```bash
python3 pe_reversing_helper.py challenge.zip --password YOUR_PASSWORD --member path/in/archive/challenge.exe
```

Choose where the unpacked executable is saved:

```bash
python3 pe_reversing_helper.py challenge.exe --output ./challenge_analysis
```

Run `python3 pe_reversing_helper.py --help` to see the command options.

## Read the results

The script prints relevant strings and their virtual addresses. When it recognizes the split key check, it prints each piece at its input offset and the assembled key. When it also recognizes the XOR output loop, it prints the decoded text and a possible flag.

For `ReverseMe.zip`, the key pieces assemble to `5c3b8a21d79e465f0c321b987a4e65f3`, and the flag is `CSG_FLAG{You_have_great_reversing_skills!}`.

If unpacking succeeds, the script saves `<name>_unpacked.exe` in `<name>_analysis/` next to the input file, unless you set `--output`. You can open that file in Ghidra or inspect it with a terminal disassembler such as radare2.

## Scope

Automatic key recovery currently supports 32 bit x86 PE files with hex text compared against copied input pieces. Automatic XOR decoding expects 16 byte constants copied to the stack before the XOR loop. Other key checks, packers, architectures, and encodings require manual analysis. A line starting with `[!]` tells you which automatic step did not match.

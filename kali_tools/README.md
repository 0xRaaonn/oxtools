# Kali CTF tool field guide

This directory has **161 individual tool guides**, one for every row in the supplied Kali tool list, plus a practical worked example in each guide. The guides cover CLI tools, GUIs, suites, wordlists, and offline reference collections. They are designed for quick offline lookup; exact flags can vary by installed version, so each guide points you to local help when appropriate.

## Start here

1. Preserve supplied files and note their SHA-256 hashes before editing, unpacking, or running them.
2. Choose a tool from the alphabetical index below or use the [workflow primer](WORKFLOWS.md) to choose by challenge type.
3. In each guide, read **What it does**, **First steps**, **Worked example**, and **Pitfalls**. Replace placeholders such as `TARGET` with organizer-provided values.
4. Run active scans and authentication tests only against competition-authorized targets. Keep rates modest and save tool output for reproducibility.

The [catalog.tsv](catalog.tsv) stores the original tool names and concise guide data. This is documentation, not a set of packages to install.

## Alphabetical index


### #

- [.NET SDK](dotnet-sdk/README.md)
- [7-Zip (7z)](7-zip-7z/README.md)

### A

- [aircrack-ng](aircrack-ng/README.md)
- [ALEAPP (Android Logs Events And Protobuf Parser)](aleapp-android-logs-events-and-protobuf-parser/README.md)
- [Android Studio](android-studio/README.md)
- [angr](angr/README.md)
- [AperiSolve](aperisolve/README.md)
- [Apktool](apktool/README.md)
- [asar (@electron/asar)](asar-electron-asar/README.md)
- [Audacity](audacity/README.md)
- [AutoIt-Ripper](autoit-ripper/README.md)

### B

- [BinDiff](bindiff/README.md)
- [bkcrack](bkcrack/README.md)
- [bulk_extractor](bulk-extractor/README.md)
- [bvi](bvi/README.md)
- [Bytecode Viewer](bytecode-viewer/README.md)
- [bzip2](bzip2/README.md)

### C

- [cabextract](cabextract/README.md)
- [capa](capa/README.md)
- [Chainsaw](chainsaw/README.md)
- [checksec](checksec/README.md)
- [crypto-attacks](crypto-attacks/README.md)
- [curl](curl/README.md)
- [Cutter](cutter/README.md)

### D

- [DB Browser for SQLite](db-browser-for-sqlite/README.md)
- [DBeaver Community Edition](dbeaver-community-edition/README.md)
- [Detect It Easy (DIE)](detect-it-easy-die/README.md)
- [dex2jar](dex2jar/README.md)
- [Didier Stevens Beta tools (onedump.py)](didier-stevens-beta-tools-onedump-py/README.md)
- [Didier Stevens Suite (pdfid.py, pdf-parser.py, oledump.py and   others)](didier-stevens-suite-pdfid-py-pdf-parser-py-oledump-py-and-others/README.md)
- [Docker Engine and Compose plugin](docker-engine-and-compose-plugin/README.md)
- [dwarf2json](dwarf2json/README.md)

### E

- [Eclipse Temurin JDK (OpenJDK)](eclipse-temurin-jdk-openjdk/README.md)
- [ewf-tools (libewf)](ewf-tools-libewf/README.md)
- [Exploit-DB / searchsploit (offline archive)](exploit-db-searchsploit-offline-archive/README.md)

### F

- [factordb-python](factordb-python/README.md)
- [FakeNet-NG](fakenet-ng/README.md)
- [Fernflower](fernflower/README.md)
- [Feroxbuster](feroxbuster/README.md)
- [FFmpeg](ffmpeg/README.md)
- [ffuf](ffuf/README.md)
- [file (libmagic)](file-libmagic/README.md)
- [FLOSS (FLARE Obfuscated String Solver)](floss-flare-obfuscated-string-solver/README.md)
- [foremost](foremost/README.md)
- [FQLite](fqlite/README.md)
- [Frida](frida/README.md)

### G

- [GCC, G++ and build tools (build-essential, make, CMake,   pkg-config)](gcc-g-and-build-tools-build-essential-make-cmake-pkg-config/README.md)
- [GEF (GDB Enhanced Features)](gef-gdb-enhanced-features/README.md)
- [Git](git/README.md)
- [Gitleaks](gitleaks/README.md)
- [G'MIC (gmic)](g-mic-gmic/README.md)
- [GNU Wget](gnu-wget/README.md)
- [Go](go/README.md)
- [Gobuster](gobuster/README.md)
- [GoReSym](goresym/README.md)
- [GTFOBins (offline copy)](gtfobins-offline-copy/README.md)
- [gzip](gzip/README.md)

### H

- [HackTricks (offline copy)](hacktricks-offline-copy/README.md)
- [hashcat](hashcat/README.md)
- [hashid](hashid/README.md)
- [Hayabusa](hayabusa/README.md)
- [hcxtools](hcxtools/README.md)
- [Hindsight (pyhindsight)](hindsight-pyhindsight/README.md)
- [hlextend](hlextend/README.md)
- [Hydra](hydra/README.md)

### I

- [iLEAPP (iOS Logs, Events, And Plists Parser)](ileapp-ios-logs-events-and-plists-parser/README.md)
- [ImageMagick](imagemagick/README.md)
- [Impacket](impacket/README.md)
- [innoextract](innoextract/README.md)
- [internet_detector](internet-detector/README.md)
- [IPython](ipython/README.md)

### J

- [jadx (jadx-gui)](jadx-jadx-gui/README.md)
- [John the Ripper (jumbo)](john-the-ripper-jumbo/README.md)
- [Jpeginfo](jpeginfo/README.md)
- [js-beautify](js-beautify/README.md)
- [js-deobfuscator](js-deobfuscator/README.md)
- [jwt_tool](jwt-tool/README.md)

### K

- [Katana](katana/README.md)

### L

- [legion](legion/README.md)
- [libesedb tools](libesedb-tools/README.md)
- [LibreOffice](libreoffice/README.md)
- [lrzip](lrzip/README.md)
- [ltrace](ltrace/README.md)
- [lz4](lz4/README.md)
- [lzip](lzip/README.md)

### M

- [mac_apt](mac-apt/README.md)
- [MediaInfo](mediainfo/README.md)
- [Metasploit Framework](metasploit-framework/README.md)
- [mimikatz](mimikatz/README.md)
- [Miniforge3 (conda)](miniforge3-conda/README.md)
- [multimon-ng](multimon-ng/README.md)
- [mupdf-tools (mutool)](mupdf-tools-mutool/README.md)

### N

- [NASM (Netwide Assembler)](nasm-netwide-assembler/README.md)
- [Nmap (with Ncat / Nping)](nmap-with-ncat-nping/README.md)
- [Node.js (with npm)](node-js-with-npm/README.md)

### O

- [obfuscator-io-deobfuscator](obfuscator-io-deobfuscator/README.md)
- [Obsidian](obsidian/README.md)
- [oletools (full suite: olevba, oleid, oleobj, rtfobj, mraptor,   msodde, olemeta, oletimes, pyxswf)](oletools-full-suite-olevba-oleid-oleobj-rtfobj-mraptor-msodde-olemeta-oletimes-pyxswf/README.md)
- [OllyDbg](ollydbg/README.md)
- [OpenStego](openstego/README.md)

### P

- [padding-oracle-attacker](padding-oracle-attacker/README.md)
- [PARI/GP](pari-gp/README.md)
- [PayloadsAllTheThings (offline copy)](payloadsallthethings-offline-copy/README.md)
- [peda](peda/README.md)
- [peepdf-3](peepdf-3/README.md)
- [pff-tools (libpff)](pff-tools-libpff/README.md)
- [Plaso (log2timeline, psort, pinfo)](plaso-log2timeline-psort-pinfo/README.md)
- [pngcheck](pngcheck/README.md)
- [pwndbg](pwndbg/README.md)
- [pycdc (Decompyle++)](pycdc-decompyle/README.md)
- [pyinstxtractor-ng](pyinstxtractor-ng/README.md)
- [pypykatz](pypykatz/README.md)
- [Python 2.7](python-2-7/README.md)
- [Python 3.11 (via uv)](python-3-11-via-uv/README.md)

### Q

- [qemu-img (qemu-utils)](qemu-img-qemu-utils/README.md)

### R

- [radare2](radare2/README.md)
- [rat-king-parser](rat-king-parser/README.md)
- [RegRipper](regripper/README.md)
- [ripgrep (rg)](ripgrep-rg/README.md)
- [rockyou.txt (Kali 'wordlists' package)](rockyou-txt-kali-wordlists-package/README.md)
- [ROPgadget](ropgadget/README.md)
- [rtptools (rtpdump, rtpplay and others)](rtptools-rtpdump-rtpplay-and-others/README.md)
- [Rust (rustup, rustc, cargo)](rust-rustup-rustc-cargo/README.md)
- [rustscan](rustscan/README.md)

### S

- [SageMath](sagemath/README.md)
- [SecLists](seclists/README.md)
- [socat](socat/README.md)
- [Sonic Visualiser](sonic-visualiser/README.md)
- [SoX (Sound eXchange)](sox-sound-exchange/README.md)
- [SQLCipher Community Edition — CLI](sqlcipher-community-edition-cli/README.md)
- [sqlite3](sqlite3/README.md)
- [sqlmap](sqlmap/README.md)
- [sstv (command-line SSTV decoder)](sstv-command-line-sstv-decoder/README.md)
- [steghide](steghide/README.md)
- [stegseek](stegseek/README.md)
- [stegsnow (SNOW)](stegsnow-snow/README.md)
- [StegSolve](stegsolve/README.md)
- [strace](strace/README.md)
- [Subfinder](subfinder/README.md)
- [Sublime Text](sublime-text/README.md)

### T

- [tar](tar/README.md)
- [tcpdump](tcpdump/README.md)
- [TestDisk and PhotoRec](testdisk-and-photorec/README.md)

### U

- [unar](unar/README.md)
- [uncompyle6](uncompyle6/README.md)
- [unpyc3 (unpyc37-3.10)](unpyc3-unpyc37-3-10/README.md)
- [unrar](unrar/README.md)
- [unzip](unzip/README.md)
- [UPX](upx/README.md)

### V

- [Visual Studio Code](visual-studio-code/README.md)
- [Volatility 2](volatility-2/README.md)
- [Volatility 2 community plugins](volatility-2-community-plugins/README.md)
- [Volatility 2 profiles (Linux and macOS)](volatility-2-profiles-linux-and-macos/README.md)
- [Volatility 3 community plugins (community3)](volatility-3-community-plugins-community3/README.md)
- [VS Code extension: C/C++ (ms-vscode.cpptools)](vs-code-extension-c-cpp-ms-vscode-cpptools/README.md)
- [VS Code extension: Python (ms-python.python)](vs-code-extension-python-ms-python-python/README.md)

### Y

- [YARA](yara/README.md)
- [yara-python (and YARA on Linux)](yara-python-and-yara-on-linux/README.md)

### Z

- [zip](zip/README.md)
- [zstd](zstd/README.md)
- [Zui (formerly Brim)](zui-formerly-brim/README.md)

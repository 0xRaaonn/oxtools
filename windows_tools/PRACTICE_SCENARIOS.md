# Windows CTF practice scenarios

These are **fictional practice questions**. The sample filenames, addresses, and flags illustrate a method; they are not answers to a live challenge. Read the question first, choose tools, then compare your plan with the walkthrough.

## 1. A PNG appears ordinary, but the prompt says “look beneath the colors”

**Question:** You receive `poster.png`. It displays a normal image. How would you search for a hidden text payload and distinguish a real hit from random LSB output?

**Walkthrough:** Preserve the original and inspect metadata with [ExifTool](exiftool/README.md). Run [zsteg](zsteg/README.md) against the PNG; if it reports a candidate like `1b,rgb,lsb,xy`, extract that exact descriptor to a new file. View raw bytes with [xxd](xxd/README.md), then try [CyberChef](cyberchef/README.md) only if the extracted bytes visibly use another encoding. A full coherent message or valid file structure is stronger than a short word. Re-encoding the PNG can destroy the evidence.

## 2. A PDF page is blank but the file is unusually large

**Question:** `memo.pdf` displays one blank page. Where could a hidden answer reside?

**Walkthrough:** In a [PDF viewer](pdf-viewer/README.md), select all page text and inspect comments, layers, forms, and attachments. Run `pdftotext -layout memo.pdf memo.txt` with [pdftotext](pdftotext/README.md). Run `qpdf --check memo.pdf` and `qpdf --list-attachments memo.pdf` with [qpdf](qpdf/README.md). If qpdf lists an attachment, extract by its exact key to a separate file and identify its bytes. If text extraction is empty, the page may be image-only; no OCR is implied by pdftotext. Keep the original because rewriting a PDF changes object layout.

## 3. A PCAP contains hundreds of oddly named DNS requests

**Question:** `traffic.pcapng` has many queries to `*.ctf.test`. The first labels vary. How do you decide whether they carry a message?

**Walkthrough:** Use [Wireshark](wireshark/README.md) Statistics to identify the source host and time range. Use [TShark](tshark/README.md): `tshark -r traffic.pcapng -Y 'dns.flags.response == 0' -T fields -e frame.number -e dns.qry.name`. Group by source, inspect order, and identify repeated labels caused by retransmission. Remove the constant suffix only after establishing a sequence. Decode variable labels in [CyberChef](cyberchef/README.md) or [Python](python-3/README.md). [Zeek](zeek/README.md) can summarize DNS records, but verify the exact packet bytes before accepting a decoded flag.

## 4. A website claims your answer is wrong, but the browser shows a different response

**Question:** A form at an organizer-provided lab URL displays “invalid” after submission. How do you find the actual server behavior?

**Walkthrough:** Open [Chrome DevTools](google-chrome/README.md) Network, enable Preserve log, submit one test value, and inspect request method, body, response status, body, and Set-Cookie. Send the same request to [Burp Repeater](burp-suite-community/README.md) and change one field at a time. If the server returns different JSON but the page still says invalid, the JavaScript may be reading another field or stale state. Check cookies and CSRF tokens when replayed requests fail. Record raw request/response pairs rather than relying on the visible page.

## 5. A Windows executable contains a tempting flag string

**Question:** `check.exe` contains `flag{demo}` in its strings, but entering that value fails. Is the string a decoy?

**Walkthrough:** Inspect the binary with [strings](strings/README.md), note the flag-looking string's offset, then open it in [Ghidra](ghidra/README.md). Follow references to the string and trace the actual input validator. If it is a .NET assembly, use [dnSpyEx](dnspyex/README.md). If static analysis is unclear, run a copied native executable under [x64dbg](x64dbg/README.md) and break before the compare. Inspect exact buffer bytes, length, and branch condition. A string in the binary is evidence of its presence, not evidence that it is accepted input.

## 6. A Linux binary accepts input, but address breakpoints move

**Question:** You can run a supplied ELF in WSL. A numeric GDB breakpoint works once and then misses. How can you continue analysis?

**Walkthrough:** Use [objdump](objdump/README.md) to check architecture and sections. In [gdb](gdb/README.md), set `break main` or a symbol-relative breakpoint rather than a fixed absolute address; PIE and ASLR can move the module base. Use `info proc mappings` to inspect runtime mappings. At the comparison, examine both operands as bytes, not only C strings. Reproduce the validation transform in [Python](python-3/README.md), then test the candidate on the original executable.

## 7. A disk image contains a deleted note

**Question:** `disk.img` is a full disk image. The prompt asks for the contents of a deleted note. How do you recover it without changing the source?

**Walkthrough:** Run `mmls disk.img` with [The Sleuth Kit](the-sleuth-kit/README.md) to find the partition's **sector** start, e.g. 2048. Then run `fls -rd -o 2048 disk.img`; identify a deleted metadata address and use `icat -o 2048 disk.img INODE > note.bin` in WSL. Inspect the output with [xxd](xxd/README.md). [Autopsy](autopsy/README.md) can provide a second view. If content is missing, metadata may survive after data clusters have been overwritten. Never repair the original image with [fsck.fat](fsck-fat/README.md).

## 8. A RAM image contains a suspicious network connection

**Question:** A Windows memory dump and a destination IP are supplied. How do you identify a likely process without overclaiming?

**Walkthrough:** In [Volatility 3](volatility3/README.md), run `windows.info`, `windows.pstree`, `windows.cmdline`, and `windows.netscan` with the image path. Match the connection's PID to process tree and command line, then inspect creation times and other artifacts. Cross-check with [Eric Zimmerman's Tools](eric-zimmerman-tools/README.md) if matching disk EVTX/Prefetch artifacts are provided. A stale socket or reused PID can mislead; report the connection and corroborating facts separately.

## 9. A public RSA key and ciphertext are supplied

**Question:** `pub.pem` and `cipher.bin` are provided. What should you establish before attempting decryption?

**Walkthrough:** Use [OpenSSL](openssl/README.md) to inspect the public modulus, exponent, and key format. Determine whether the ciphertext is raw binary, hex, or Base64 and whether the prompt specifies OAEP, PKCS#1 v1.5, or textbook RSA. Use [RsaCtfTool](rsactftool/README.md) only for a plausible weak-key attack and verify any recovered factors multiply to the public modulus. If a private key is supplied, use OpenSSL with the correct padding/digest. A Base64 decode is not RSA decryption, and a normal strong RSA key is not factorable by trying more tools.

## 10. A vehicle-bus capture shows a changing byte

**Question:** A candump log repeats CAN ID `123` every 100 ms, and one byte changes. What might that byte represent?

**Walkthrough:** With [can-utils](can-utils/README.md), group records by ID and timestamp. Compare the entire payload over time; the changing byte might be a counter, checksum, or sensor value. Test little-endian and big-endian interpretations and look for a consistent relationship to other frames or prompt clues. If the competition uses a [cannelloni](cannelloni/README.md) tunnel, first verify frames arrive on the expected local SocketCAN interface. Avoid transmitting frames unless the challenge explicitly requires it.

## 11. An SSH PCAP is encrypted, but a Linux memory snapshot is also provided

**Question:** Can you recover the SSH conversation text from a packet capture using only the server host key?

**Walkthrough:** The host key alone is insufficient for a modern SSH session. Analyze the snapshot with [Volatility 3](volatility3/README.md) and check whether an active OpenSSH process exists. The [OpenSSH Session Key Recovery](openssh-session-key-recovery/README.md) project may recover session material if the image, plugin, symbols, and OpenSSH version are compatible. Match recovered cipher/key direction and any rekey interval to the PCAP. If no session material is present, the capture remains encrypted.

## 12. A file opens as an image but has an archive appended

**Question:** `cover.jpg` displays normally, while [binwalk](binwalk/README.md) reports a ZIP at a later offset. How do you prove it is embedded content?

**Walkthrough:** Inspect the offset with [xxd](xxd/README.md) and look for ZIP magic `50 4B 03 04`. Carve a copy from that offset using [Python](python-3/README.md), then test the carved ZIP with a parser. Check whether its end record and member CRCs are valid. If it passes, inspect member names and extracted content. A mere magic-byte hit could be coincidental; validation makes the conclusion stronger.

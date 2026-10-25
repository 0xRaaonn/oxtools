# fsck.fat (dosfstools)

**Use:** inspect and repair FAT12/16/32 filesystem structures. Repair changes bytes, so work on a copy.

**Commands (WSL/Linux):** `fsck.fat -n image.img` checks without writing; `fsck.fat -v -n image.img` adds detail; `fsck.fat -a image-copy.img` automatically repairs the copy; `fsck.fat -r image-copy.img` asks before each repair. Some builds use `dosfsck` as the command name.

**CTF workflow:** Identify whether the image is a FAT filesystem image or an entire disk containing a partition. For a whole disk, find the FAT partition start with The Sleuth Kit and extract that partition into a separate copy before checking it. Compare pre/post hashes and save the repair report.

**Pitfalls:** A dirty filesystem is not automatically corrupt. Repair can alter directory entries and allocation chains, potentially removing evidence. `-n` may report issues it cannot fully resolve without writing; use it for triage only. It is not a file carving tool.

Source: [dosfstools project](https://github.com/dosfstools/dosfstools).

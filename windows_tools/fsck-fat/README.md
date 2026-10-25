# fsck.fat (dosfstools)

**Use:** inspect and repair FAT12/16/32 filesystem structures. Repair changes bytes, so work on a copy.

**Commands (WSL/Linux):** `fsck.fat -n image.img` checks without writing; `fsck.fat -v -n image.img` adds detail; `fsck.fat -a image-copy.img` automatically repairs the copy; `fsck.fat -r image-copy.img` asks before each repair. Some builds use `dosfsck` as the command name.

**CTF workflow:** Identify whether the image is a FAT filesystem image or an entire disk containing a partition. For a whole disk, find the FAT partition start with The Sleuth Kit and extract that partition into a separate copy before checking it. Compare pre/post hashes and save the repair report.

**Pitfalls:** A dirty filesystem is not automatically corrupt. Repair can alter directory entries and allocation chains, potentially removing evidence. `-n` may report issues it cannot fully resolve without writing; use it for triage only. It is not a file carving tool.

Source: [dosfstools project](https://github.com/dosfstools/dosfstools).

## Worked example: diagnose a FAT image safely

Copy `fat.img` to `fat-work.img`. Run `fsck.fat -n -v fat.img` and save the report. Suppose it reports an orphaned cluster chain. Run `fsck.fat -r fat-work.img` only on the copy to inspect proposed repairs interactively. Compare before/after hashes and recover files from both versions; a repair may make a directory mountable while also changing allocation evidence.

## More CTF scenario questions

### A FAT image fails to mount. Should I run automatic repair?

First run `fsck.fat -n -v image.img` for a read-only diagnosis and save the report. Repair only a copy with `-r` or `-a`, then compare both images and recovered files.

### fsck reports an orphaned chain. Is that the flag file?

It is only unreferenced allocated data. Recover/inspect it, identify its format, and compare with directory metadata and prompt. Do not assume every orphan is meaningful.

# The Sleuth Kit

**Use:** analyze disk images and filesystems without mounting or changing them. The tools work at different layers: disk partitions, filesystem metadata, and file content.

**Commands:** `mmls disk.img` shows partition start sectors. `fsstat -o START disk.img` shows filesystem details, where START is the partition start sector. `fls -r -o START disk.img` lists files recursively; `fls -rd -o START disk.img` includes deleted entries. `icat -o START disk.img INODE > recovered.bin` extracts a file by metadata address. `istat -o START disk.img INODE` shows file metadata; `blkls -o START disk.img > unallocated.bin` extracts unallocated space.

**CTF workflow:** Determine whether the file is a whole disk or one filesystem. If whole disk, find sector offset with mmls and pass `-o` consistently. List entries, identify inode, recover file, and hash it.

**Pitfalls:** Offsets for `-o` are usually sectors, not bytes. Deleted filenames and content may be partially overwritten. Output redirection should be binary-safe; WSL is simplest.

Source: [The Sleuth Kit manual](https://www.sleuthkit.org/sleuthkit/docs.php).

## Worked example: recover a deleted file

Suppose `mmls disk.img` shows a FAT/NTFS partition beginning at sector `2048`. Run `fls -rd -o 2048 disk.img` and find a deleted entry with metadata address `42`. Extract with `icat -o 2048 disk.img 42 > recovered.bin` in WSL. Inspect `recovered.bin` with `xxd` and hash it. If contents are damaged, the entry may have been overwritten; the listing alone does not guarantee recovery.

## More CTF scenario questions

### `mmls disk.img` shows a partition starting at sector 2048. How do I list its files?

Run `fls -r -o 2048 disk.img`. Keep `-o 2048` for `istat` and `icat`; using byte offset 2048 instead of sector 2048 points to the wrong location.

### A deleted filename appears but `icat` produces empty or damaged data. What happened?

The metadata entry may survive while clusters were reused. Inspect `istat`, compare Autopsy's view, and search unallocated space, but report partial recovery honestly.

# HxD

**Use:** Windows GUI hex editor for inspecting and changing raw bytes in files or disks. Work on a copy before editing.

**Workflow:** File → Open a binary; the left column shows offsets, middle hex bytes, right character view. Select bytes to see their length and interpretation. Use Search for text, hex values, or patterns; Go To for a known offset; compare files to locate differences. Set the correct text encoding when searching Unicode.

**CTF examples:** Confirm a magic signature, inspect bytes around a binwalk offset, fix a known corrupt header in a copied file, or compare before/after patches. Save modified files under a new name and record the original offset and changed bytes.

**Pitfalls:** Inserting bytes shifts every later offset; overwriting keeps file length. A hex editor does not understand all structure automatically. Opening a physical disk with write access can alter evidence; use a read-only image when possible.

Source: [HxD product documentation](https://mh-nexus.de/en/hxd/).

## Worked example: repair a known bad signature

Suppose a copied PNG has first bytes `00 50 4E 47 0D 0A 1A 0A` instead of the expected `89 50 4E 47 0D 0A 1A 0A`. In HxD, open the copy, select offset `0`, switch to overwrite mode, and replace `00` with `89`. Save as a new file and verify the eight-byte signature with xxd. If the image still fails, its chunks or checksums may also be damaged.

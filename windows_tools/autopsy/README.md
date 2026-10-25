# Autopsy

**Use:** GUI forensic analysis of disk images, filesystems, deleted files, timelines, web artifacts, and indexed text. It uses The Sleuth Kit and other ingest modules underneath.

**Workflow:** Create a case with a dedicated output location; add the disk image as a data source; choose ingest modules relevant to the challenge. Review data source tree, file metadata, deleted files, keyword hits, extracted content, and timeline. Tag findings and export individual artifacts rather than changing the source image.

**CTF path:** Confirm whether the supplied file is a whole disk or a logical image. Start with partitions/filesystems, then inspect user directories, browser data, recent files, and deleted entries. Use The Sleuth Kit CLI when you need precise offsets or inode-based extraction.

**Pitfalls:** Ingest can take time and substantial storage. Missing search hits may mean the module has not finished or the content was not indexed. Timestamps have timezone and source differences. Hash the original and case output separately.

Source: [Autopsy user documentation](https://www.autopsy.com/support/).

## Worked example: locate a deleted note

Create an Autopsy case and add `disk.img` as a data source. After ingest, browse **Deleted Files** and search for `notes.txt`. Inspect its metadata, content preview, and directory path; export it to the case output folder. Compare the recovered bytes with `icat` if you need an inode-level cross-check. An empty preview can mean missing clusters or an ingest limitation, not necessarily an empty original file.

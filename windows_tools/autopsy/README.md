# Autopsy

**Use:** GUI forensic analysis of disk images, filesystems, deleted files, timelines, web artifacts, and indexed text. It uses The Sleuth Kit and other ingest modules underneath.

**Workflow:** Create a case with a dedicated output location; add the disk image as a data source; choose ingest modules relevant to the challenge. Review data source tree, file metadata, deleted files, keyword hits, extracted content, and timeline. Tag findings and export individual artifacts rather than changing the source image.

**CTF path:** Confirm whether the supplied file is a whole disk or a logical image. Start with partitions/filesystems, then inspect user directories, browser data, recent files, and deleted entries. Use The Sleuth Kit CLI when you need precise offsets or inode-based extraction.

**Pitfalls:** Ingest can take time and substantial storage. Missing search hits may mean the module has not finished or the content was not indexed. Timestamps have timezone and source differences. Hash the original and case output separately.

Source: [Autopsy user documentation](https://www.autopsy.com/support/).

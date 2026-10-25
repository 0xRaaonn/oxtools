# ExifTool

**Use:** inspect metadata in images, PDFs, documents, audio, and many other formats. It can also write tags, so use read commands on originals.

**Commands:** `exiftool photo.jpg`, `exiftool -a -G1 -s photo.jpg` (duplicates, groups, tag names), `exiftool -time:all -a -G1 -s photo.jpg`, `exiftool -json photo.jpg`, and `exiftool -u photo.jpg` (unknown tags). `-b -ThumbnailImage` emits thumbnail bytes; use a binary-safe output method.

**CTF workflow:** Check comments, description, author, GPS, timestamps, thumbnails, and custom fields. Compare metadata with visible content. On Windows the file may initially be named `exiftool(-k).exe`.

**Pitfalls:** Metadata can be forged or stale. Writing tags changes the file and usually creates backups. Multiple tag locations can conflict. PowerShell redirection can affect binary output; prefer ExifTool's own output option or `cmd /c` redirection.

Source: [ExifTool documentation](https://exiftool.org/exiftool_pod.html).

# binwalk

**Use:** scan files for embedded signatures and compressed streams. Results are candidate offsets; confirm before extraction.

**Commands:** `binwalk sample.bin`, `binwalk --help`, and where supported `binwalk -e sample.bin`. Use `xxd -s 0xOFFSET -l 64 sample.bin` to inspect a hit. Carve a region with Python: `Path('part.bin').write_bytes(Path('sample.bin').read_bytes()[OFFSET:END])`.

**CTF workflow:** Scan a suspicious image, archive, or firmware file; identify a plausible embedded format, carve a copy, then validate with that format's own parser. Re-scan extracted nested containers.

**Pitfalls:** Signatures occur by chance. Automatic extraction can invoke external helpers and produce many files. Older Python and newer Rust binwalk versions differ in options; use local `--help`.

Source: [binwalk project](https://github.com/ReFirmLabs/binwalk).

## Worked example: embedded ZIP in a PNG

Run `binwalk picture.png` and suppose it reports a ZIP header at decimal offset 4096. Confirm with `xxd -s 4096 -l 16 picture.png`; it should begin `50 4B 03 04`. Carve and validate a copy with Python:

```python
from pathlib import Path
from zipfile import ZipFile
Path('embedded.zip').write_bytes(Path('picture.png').read_bytes()[4096:])
with ZipFile('embedded.zip') as archive:
    print(archive.namelist(), archive.testzip())
```

Use the actual reported offset. `testzip()` returning `None` means the member CRC checks passed.

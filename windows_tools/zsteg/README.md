# zsteg

**Use:** detect/extract data hidden in PNG or BMP pixel channels, especially least significant bits. It is a Ruby program; use a provided build if Ruby installation is outside the allowlist.

**Commands:** `zsteg image.png` scans common methods. `zsteg -a image.png` tries more. `zsteg -E '1b,rgb,lsb,xy' image.png > payload.bin` extracts a named result. The descriptor indicates bit count, channels, bit order, and pixel traversal. Check the exact descriptor from your scan.

**CTF workflow:** Confirm the file is PNG/BMP, inspect promising text or file signatures, extract the candidate, and validate it with `xxd`, `strings`, or `binwalk`. JPEG is generally unsuitable for this pixel LSB method.

**Pitfalls:** Many results are false positives. Re-encoding or resizing can destroy hidden bits; preserve the original.

Source: [zsteg README](https://github.com/zed-0xff/zsteg).

## Worked example: extract a pixel payload

Run `zsteg picture.png`. Suppose it reports `1b,rgb,lsb,xy .. text: "flag{pixel_bits}"`. Extract exactly that channel with `zsteg -E '1b,rgb,lsb,xy' picture.png > payload.bin`, then inspect with `xxd payload.bin`. A coherent flag in the extracted byte stream is stronger evidence than the detector's one-line guess.

## More CTF scenario questions

### zsteg prints a dozen English-looking fragments. Which one matters?

Extract each promising descriptor with `-E` and inspect the complete byte stream. Prefer a valid file signature, coherent length, or expected flag format over a short accidental word.

### The PNG has transparency. Could the alpha channel hold data?

Try descriptors involving `a` or an all-method scan with `zsteg -a image.png`. Confirm extracted bytes against the original image; converting the PNG can change channel data.

# ZBar

**Use:** read QR codes and other barcodes from images or a camera. The CLI is commonly `zbarimg`.

**Commands:** `zbarimg code.png` scans and prints type plus data; `zbarimg --raw code.png` prints payload only; `zbarimg -q --raw code.png` suppresses nonessential output. `zbarimg --help` lists symbology and scan options. On Windows, the installer may expose a GUI while the CLI resides in its install directory.

**CTF workflow:** Crop to the code, try contrast/rotation in an allowed image editor if the source is damaged, and inspect the returned payload as text or bytes. A QR code can hold a URL, binary content, or another encoding layer.

**Pitfalls:** Low resolution, perspective distortion, and quiet-zone removal cause scan failure. Do not automatically open URLs encoded in a barcode. A displayed string may contain control characters; view raw bytes when needed.

Source: [ZBar project](https://github.com/mchehab/zbar).

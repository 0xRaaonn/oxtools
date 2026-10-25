# pdftotext (Poppler)

**Use:** extract selectable text from PDFs. It does not perform OCR on scanned images.

**Commands:** `pdftotext document.pdf output.txt`; `pdftotext -layout document.pdf output.txt` preserves approximate columns; `pdftotext -raw document.pdf output.txt` follows content-stream order; `pdftotext -f 2 -l 4 document.pdf pages.txt` selects pages; `pdftotext -enc UTF-8 document.pdf -` writes text to stdout. Use `pdfinfo document.pdf` if the Poppler package includes it.

**CTF workflow:** Compare default, `-layout`, and `-raw` output when reading order is odd. Search for hidden-looking words, zero-width or unusual Unicode characters, and text outside the visible page. Check whether a page is actually an image if no text extracts.

**Pitfalls:** PDF drawing order need not match reading order. A password-protected file may need a supplied password. White or clipped text can appear in extraction despite being invisible.

Source: [Poppler pdftotext manual](https://manpages.debian.org/testing/poppler-utils/pdftotext.1.en.html).

## Worked example: text hidden by layout

Run `pdftotext -layout report.pdf report.txt` and inspect `report.txt`. Suppose a flag appears as characters spread across columns. Run `pdftotext -raw report.pdf raw.txt` and compare reading order. If neither produces text from a page, it may be scanned artwork; inspect it in a PDF viewer and look for embedded images or annotations.

## More CTF scenario questions

### `pdftotext` produces an empty file. Is the PDF empty?

Open the PDF visually. If the page is scanned artwork, there may be no text layer; inspect images/attachments with a viewer or qpdf. pdftotext does not perform OCR.

### A table extracts in a nonsensical order. What option helps?

Compare default output with `pdftotext -layout file.pdf layout.txt` and `-raw`. PDF text drawing order and visual reading order can differ; verify important values on the rendered page.

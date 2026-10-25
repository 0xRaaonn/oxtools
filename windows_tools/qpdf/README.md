# qpdf

**Use:** inspect, validate, and transform PDF structure, including encryption, objects, and attachments.

**Commands:** `qpdf --check document.pdf` validates structure; `qpdf --show-encryption document.pdf` shows encryption status; `qpdf --qdf --object-streams=disable document.pdf readable.pdf` makes a more inspectable PDF; `qpdf --json document.pdf` emits structured information on versions that support it; `qpdf --list-attachments document.pdf` lists embedded files; `qpdf --show-attachment=name document.pdf > attachment.bin` extracts one. Check `qpdf --help` for your version's exact attachment syntax.

**CTF workflow:** Run check, inspect metadata/encryption, list attachments, then make a QDF copy for searching object dictionaries or streams. Compare visible content with pdftotext output.

**Pitfalls:** Rewriting a PDF can change object numbers and discard malformed tricks, so keep the original. qpdf does not do OCR. Password-protected files need the provided password unless a weakness is part of the task.

Source: [qpdf manual](https://qpdf.readthedocs.io/en/stable/).

## Worked example: extract a PDF attachment

Run `qpdf --check puzzle.pdf` and `qpdf --list-attachments puzzle.pdf`. Suppose it lists an attachment key `payload.txt`. Run `qpdf --show-attachment=payload.txt puzzle.pdf > payload.txt` in WSL, then inspect the saved file. If the exact key includes unusual characters, copy it exactly from qpdf's listing. Preserve `puzzle.pdf` because rewriting PDFs can change object layout.

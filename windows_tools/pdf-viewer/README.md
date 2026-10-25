# PDF Viewer

**Use:** read pages and inspect visible annotations, attachments, layers, forms, and document properties. Exact menu names depend on the installed viewer.

**Workflow:** Open a copy. Check every page, thumbnails, bookmarks, properties, comments, attachment/paperclip panel, form fields, and optional layers. Search and select text; scanned pages may contain only images. Zoom in on faint text, and compare rendering with another permitted viewer if it looks unusual.

**CTF examples:** A blank-looking page may contain white text: select text or run pdftotext. An embedded file may appear under Attachments rather than on a page. A QR code can be exported or screenshotted and scanned with ZBar.

**Pitfalls:** PDFs may contain JavaScript, links, and embedded files. Avoid enabling scripts or following unknown links. Print-to-PDF can erase evidence, so preserve the original. Extracted text may differ from the visible page.

Related: [pdftotext](../pdftotext/README.md), [qpdf](../qpdf/README.md). Source: [PDF specification](https://pdfa.org/resource/iso-32000-pdf/).

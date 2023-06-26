---
date: "2006-12-13"
title: "PDF commands"
category: English
tags: CLI, Linux, pdf, GhostScript, pdfgrep
---

- Case-insensitive search of a string in a PDF, thanks to [`pdfgrep`](https://pdfgrep.org):

  ```shell-session
  $ pdfgrep --page-number --ignore-case 'my_string' ./document.pdf
  ```

- Convert a PDF to a JPEG file at 150 dpi:

  ```shell-session
  $ convert -density 150 ./document.pdf ./document.jpg
  ```

- Extract images from a PDF document:

  ```shell-session
  $ pdfimages -j document.pdf prefix
  ```

- Compile all JPEG files in the current folder into a single PDF at 150 dpi:

  ```shell-session
  $ convert -density 150 ./*.jpg ./document.pdf
  ```

- Remove password of a PDF:

  ```shell-session
  $ pdftk ./password-protected.pdf input_pw PROMPT output ./no-password.pdf
  ```

- Split a PDF into pages:

  ```shell-session
  $ pdftk doc.pdf burst
  ```

- Merge 2 PDF documents:

  ```shell-session
  $ pdftk doc1.pdf doc2.pdf cat output newdoc.pdf
  ```

- Same as above, but for all PDFs of the current folder. This also have the nice side effect of removing all DRMs :) :

  ```shell-session
  $ gs -sDEVICE=pdfwrite -dBATCH -dNOPAUSE -q -sOutputFile=bigfile.pdf ./*
  ```

- Reduce size of PDF (see [GhostScript `-dPDFSETTINGS` documentation](https://web.mit.edu/ghostscript/www/Ps2pdf.htm#Options)):

  ```shell-session
  $ gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -q -o small-output.pdf large-input.pdf
  ```

- Reduce a `big.pdf` file to a `smaller.pdf` file by limiting its images to 1000 pixels and convert them to grayscale:

  ```shell-session
  $ pdfimages -j ./big.pdf prefix
  $ convert -resize 1000x1000 -type Grayscale -density 150 ./prefix-*.jpg ./smaller.pdf
  $ rm prefix-*.jpg
  ```

## Additional References

- [Text, Date & Document processing commands](https://kevin.deldycke.com/2006/12/text-date-document-processing-commands/)
- [PDF processing and analysis with open-source tools](https://www.bitsgalore.org/2021/09/06/pdf-processing-and-analysis-with-open-source-tools)

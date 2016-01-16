---
date: 2006-12-13 22:10:13
title: Text, Date & Document processing commands
category: English
tags: calendar, CLI, date, epoch, find, Linux, pdf, recode, sed, VIM, Markdown, Perl, Regular expression
---

  * Convert a PDF to a JPEG file at 150 dpi:

        :::bash
        $ convert -density 150 ./document.pdf ./document.jpg

  * Extract images from a PDF document:

        :::bash
        $ pdfimages -j document.pdf prefix

  * Text replacement:

        :::bash
        $ sed 's/string to replace/replacement string/g' original-file.txt > new-file.txt

  * Replace all occurrences of `str1` by `str2` in all files below the `/folder` path:

        :::bash
        $ find /folder -type f -print -exec sed -i 's/str1/str2/g' "{}" \;

  * Same as above but ignore all content of `.svn` folders and `.zip` files:

        :::bash
        $ find /folder -type f -not -regex ".*\/\.svn\/.*" -not -iname "*\.zip" -print -exec sed -i 's/str1/str2/g' "{}" \;

  * Remove trailing spaces and tabs in every XML files:

        :::bash
        $ find /folder -iname "*.xml" -exec sed -i 's/[ \t]*$//' "{}" \;

  * Place a new `---` line at the start of each `.markdown` files ([see result](https://github.com/kdeldycke/kevin-deldycke-blog/commit/19d1b082e93966f82873ce9d8de238a889d371b7)):

        :::bash
        $ find ./folder -iname "*.markdown" -exec sed -i '1s/^/---\n/' "{}" \;

  * Place a new `---` line before the first empty line of each `.markdown` files ([see result](https://github.com/kdeldycke/kevin-deldycke-blog/commit/8628d53284e41917159e344ea45ad9e9d16b90b1)):

        :::bash
        $ find ./folder -iname "*.markdown" -exec sed -i '0,/^$/s//---\n/' "{}" \;

  * Remove lines starting with `prefix1:` or `prefix2:` in all `.markdown` files:

        :::bash
        $ find /folder -iname "*.markdown" -exec perl -p -i -e 's/(prefix1|prefix2): .*\n//sg' "{}" \;

  * In place charset transcoding:

        :::bash
        $ recode utf-8..latin-1 utf8text.txt

  * Remove all accented characters in a string (thanks to Matthieu for the tip):

        :::bash
        $ echo "éÈça-$" | iconv -t ASCII//translit

  * Get the date of last week:

        :::bash
        $ date +"%Y-%m-%d" -d last-week

  * Get the current date in english:

        :::bash
        $ env LC_TIME=en date +"%a %b %d %Y"

  * Get the number of seconds since [epoch](http://en.wikipedia.org/wiki/Epoch_%28reference_date%29#Notable_epoch_dates_in_computing):

        :::bash
        $ date +%s

  * Convert back epoch time to human-readable date:

        :::bash
        $ date --date=@1234567890

  * Split a PDF into pages:

        :::bash
        $ pdftk doc.pdf burst

  * Merge 2 PDF documents:

        :::bash
        $ pdftk doc1.pdf doc2.pdf cat output newdoc.pdf

  * Same as above, but for all PDFs of the current folder. This also have the nice side effect of removing all DRMs :) :

        :::bash
        $ gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=bigfile.pdf ./*

  * VIM: [no autoindent on paste](http://vim.wikia.com/wiki/How_to_stop_auto_indenting).

  * a list of [`sed` one-liners](http://sed.sourceforge.net/sed1line.txt).


---
date: 2006-12-13 22:10:13
title: Text, Date & Document processing commands
category: English
tags: calendar, CLI, date, epoch, find, Linux, pdf, recode, sed, VIM, Markdown, Perl, Regular expression, GhostScript, X.org
---

## Search

  * Count the number of lines with at least one occurrence of the `y` character:
  
        :::shell-session
        $ cat test.txt
        asd  dd :; > 
        y YYYyy  yyy 
         .
         
        asdkjlyes
            kjkjhkjhy
        $ grep -o '.*y.*' ./test.txt | wc -l
        3

## Replace

  * Text replacement:

        :::shell-session
        $ sed 's/string to replace/replacement string/g' original-file.txt > new-file.txt

  * Replace all occurrences of `str1` by `str2` in all files below the `/folder` path:

        :::shell-session
        $ find /folder -type f -print -exec sed -i 's/str1/str2/g' "{}" \;

  * Same as above but ignore all content of `.svn` folders and `.zip` files:

        :::shell-session
        $ find /folder -type f -not -regex ".*\/\.svn\/.*" -not -iname "*\.zip" -print -exec sed -i 's/str1/str2/g' "{}" \;

  * Remove trailing spaces and tabs in every XML files:

        :::shell-session
        $ find /folder -iname "*.xml" -exec sed -i 's/[ \t]*$//' "{}" \;

  * Place a new `---` line at the start of each `.markdown` files ([see result](https://github.com/kdeldycke/kevin-deldycke-blog/commit/19d1b082e93966f82873ce9d8de238a889d371b7)):

        :::shell-session
        $ find ./folder -iname "*.markdown" -exec sed -i '1s/^/---\n/' "{}" \;

  * Place a new `---` line before the first empty line of each `.markdown` files ([see result](https://github.com/kdeldycke/kevin-deldycke-blog/commit/8628d53284e41917159e344ea45ad9e9d16b90b1)):

        :::shell-session
        $ find ./folder -iname "*.markdown" -exec sed -i '0,/^$/s//---\n/' "{}" \;

  * Remove lines starting with `prefix1:` or `prefix2:` in all `.markdown` files:

        :::shell-session
        $ find /folder -iname "*.markdown" -exec perl -p -i -e 's/(prefix1|prefix2): .*\n//sg' "{}" \;

  * Remove lines matching a regex (encoding [particular markdown TOC entries](https://github.com/kdeldycke/awesome-iam/commit/295a4fa4229c5966ce4bc207704e32fb6f1491d6#diff-c81593a3651bf87f58345cd819edad71R24)), save the result in place and save a backup of the original content in a `.bak` file:

        :::shell-session
        $ gawk -i inplace -v INPLACE_SUFFIX=.bak '!/^- \[(Contribute|Contributing|Licence|License)\]\(#.+\)$/{print}' ./readme.md

  * Append the content of the `addendum.txt` file to all `.markdown` files:

        :::shell-session
        $ find ./folder -iname "*.markdown" -print -exec bash -c 'cat ./addendum.txt >> "{}"' \;

  * Replace all accentuated characters by their non-accentuated variants (thanks Matthieu for the tip):

        :::shell-session
        $ echo "éÈça-$" | iconv -t ASCII//translit


## Date & Time

  * Get the date of last week:

        :::shell-session
        $ date +"%Y-%m-%d" -d last-week

  * Get the current date in english:

        :::shell-session
        $ env LC_TIME=en date +"%a %b %d %Y"

  * Get the number of seconds since [epoch](https://en.wikipedia.org/wiki/Epoch_%28reference_date%29#Notable_epoch_dates_in_computing):

        :::shell-session
        $ date +%s

  * Convert back epoch time to human-readable date:

        :::shell-session
        $ date --date=@1234567890


## Transcoding

  * In place charset transcoding:

        :::shell-session
        $ recode utf-8..latin-1 utf8text.txt


## PDF

  * Convert a PDF to a JPEG file at 150 dpi:

        :::shell-session
        $ convert -density 150 ./document.pdf ./document.jpg

  * Extract images from a PDF document:

        :::shell-session
        $ pdfimages -j document.pdf prefix

  * Compile all JPEG files in the current folder into a single PDF at 150 dpi:

        :::shell-session
        $ convert -density 150 ./*.jpg ./document.pdf

  * Split a PDF into pages:

        :::shell-session
        $ pdftk doc.pdf burst

  * Merge 2 PDF documents:

        :::shell-session
        $ pdftk doc1.pdf doc2.pdf cat output newdoc.pdf

  * Same as above, but for all PDFs of the current folder. This also have the nice side effect of removing all DRMs :) :

        :::shell-session
        $ gs -sDEVICE=pdfwrite -dBATCH -dNOPAUSE -q -sOutputFile=bigfile.pdf ./*
        
  * Reduce size of PDF (see [GhostScript `-dPDFSETTINGS` documentation](https://web.mit.edu/ghostscript/www/Ps2pdf.htm#Options)):

        :::shell-session
        $ gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -q -o small-output.pdf large-input.pdf


## Edition

  * VIM: [no autoindent on paste](https://vim.wikia.com/wiki/How_to_stop_auto_indenting).
  
  * [Get rid of Non-Breaking space](https://hauweele.net/~gawen/blog/?p=32) on Linux systems by the way X.org's `~/.xmodmap` config file.


## Additional References

  * A list of [`sed` one-liners](http://sed.sourceforge.net/sed1line.txt).

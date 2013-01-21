comments: true
date: 2006-12-13 22:10:13
layout: post
slug: text-date-document-processing-commands
title: Text, Date & Document processing commands
wordpress_id: 89
category: English
tags: calendar, CLI, date, epoch, find, Linux, pdf, recode, sed, time, VIM




  * Extract images from a PDF document:

    
    :::console
    pdfimages -j document.pdf prefix
    






  * Text replacement:

    
    :::console
    sed 's/string to replace/replacement string/g' original-file.txt > new-file.txt
    






  * Replace all occurrences of `str1` by `str2` in all files below the `/folder` path:

    
    :::console
    find /folder -type f -print -exec sed -i 's/str1/str2/g' "{}" \;
    






  * Same as above but ignore all content of `.svn` folders and `.zip` files:

    
    :::console
    find /folder -type f -not -regex ".*\/\.svn\/.*" -not -iname "*\.zip" -print -exec sed -i 's/str1/str2/g' "{}" \;
    






  * Remove trailing spaces and tabs in every XML files:

    
    :::console
    find /folder -iname"*.xml" -exec sed -i 's/[ \t]*$//' "{}" \;
    






  * In place charset transcoding:

    
    :::console
    recode utf-8..latin-1 utf8text.txt
    






  * Remove all accented characters in a string (thanks to Matthieu for the tip):

    
    :::console
    echo "éÈça-$" | iconv -t ASCII//translit
    






  * Get the date of last week:

    
    :::console
    date +"%Y-%m-%d" -d last-week
    






  * Get the current date in english:

    
    :::console
    env LC_TIME=en date +"%a %b %d %Y"
    






  * Get the number of seconds since [epoch](http://en.wikipedia.org/wiki/Epoch_%28reference_date%29#Notable_epoch_dates_in_computing):

    
    :::console
    date +%s
    






  * Convert back epoch time to human-readable date:

    
    :::console
    date --date=@1234567890
    






  * Merge 2 PDF documents:

    
    :::console
    pdftk doc1.pdf doc2.pdf cat output newdoc.pdf
    






  * Same as above, but for all PDFs of the current folder. This also have the nice side effect of removing all DRMs :) :

    
    :::console
    gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=bigfile.pdf ./*
    






  * VIM: [no autoindent on paste](http://vim.wikia.com/wiki/How_to_stop_auto_indenting).



  * a list of [`sed` one-liners](http://sed.sourceforge.net/sed1line.txt).




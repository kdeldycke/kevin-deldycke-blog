comments: true
date: 2006-10-18 00:17:10
layout: post
slug: archives-commands
title: Archives commands
wordpress_id: 2654
category: English
tags: 7zip, bzip2, CLI, Linux, tar, tarball, zip



  * Extract `.tar.gz` file:


        :::console
        tar xvzf ./file.tar.gz






  * Extract only one subdirectory and all its sub-content:


        :::console
        tar -xvzf my-archive.tar.gz --wildcards "./directory/subdirectory*"






  * Create a `.tar.gz` file:


        :::console
        tar cvzf file.tar.gz ./subfolder






  * Extract `./path/in/archive*` subfolder content from all `.tar.bz2` archives available in the current folder. Place the extracted content of each archive in a folder prefixed with the `content-` string:


        :::console
        for ARCHIVE in `ls *.tar.bz2`; do DEST_FOLDER=content-`echo $ARCHIVE | cut -d '.' -f 1`; mkdir $DEST_FOLDER; tar -C $DEST_FOLDER -xvjf $ARCHIVE --wildcards "./path/in/archive*"; done






  * Extract all `.gz` files in the current folder:


        :::console
        gunzip ./*.gz






  * Extract `.tar.bz2` file:


        :::console
        tar xvjf ./file.tar.bz2






  * Check a `.bz2` file integrity:


        :::console
        bzip2 --test ./file.bz2






  * Create a `.zip` archive of current directory, including all sub-dirs:


        :::console
        zip -r archive.zip ./*






  * Create a 7-Zip archive (thanks to `p7zip`) of a folder, including all sub-directories:


        :::console
        7za a archive.7z ./folder






  * Do the same as above, but split the archive in 50 Mib volumes:


        :::console
        7za a -v50m archive.7z ./folder






  * Convert `.tar.gz` file to `.tar.bz2` file:


        :::console
        gzip -dc archive.tar.gz | bzip2 > archive.tar.bz2






  * Extract content from [self-extracting shell archives](http://en.wikipedia.org/wiki/Shar):


        :::console
        unshar archive.sh







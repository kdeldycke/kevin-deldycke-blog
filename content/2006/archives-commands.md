---
date: "2006-10-18"
title: "Archives commands"
category: English
tags: 7-Zip, bzip2, CLI, Linux, tarball, ZIP, wget, gzip, shar
---

## gzip

- Extract `.tar.gz` file:

  ```shell-session
  $ tar xvzf ./file.tar.gz
  ```

- Extract only one subdirectory and all its sub-content:

  ```shell-session
  $ tar -xvzf my-archive.tar.gz --wildcards "./directory/subdirectory*"
  ```

- Create a `.tar.gz` file:

  ```shell-session
  $ tar cvzf file.tar.gz ./subfolder
  ```

- Extract all `.gz` files in the current folder:

  ```shell-session
  $ gunzip ./*.gz
  ```

- Convert `.tar.gz` file to `.tar.bz2` file:

  ```shell-session
  $ gzip -dc archive.tar.gz | bzip2 > archive.tar.bz2
  ```

## bzip2

- Extract `.tar.bz2` file:

  ```shell-session
  $ tar xvjf ./file.tar.bz2
  ```

- Check a `.bz2` file integrity:

  ```shell-session
  $ bzip2 --test ./file.bz2
  ```

- Extract `./path/in/archive*` subfolder content from all `.tar.bz2` archives available in the current folder. Place the extracted content of each archive in a folder prefixed with the `content-` string:

  ```shell-session
  $ for ARCHIVE in `ls *.tar.bz2`; do DEST_FOLDER=content-`echo $ARCHIVE | cut -d '.' -f 1`; mkdir $DEST_FOLDER; tar -C $DEST_FOLDER -xvjf $ARCHIVE --wildcards "./path/in/archive*"; done
  ```

## ZIP

- Create a `.zip` archive of current directory, including all sub-dirs:

  ```shell-session
  $ zip -r archive.zip ./*
  ```

- One liner to download an archive and extract its content to a target folder:

  ```shell-session
  $ wget -O - "https://example.net/archive.zip" | tar -xz --directory /target-folder -f -
  ```

## 7-Zip

- Create a 7-Zip archive (thanks to `p7zip`) of a folder, including all sub-directories:

  ```shell-session
  $ 7za a archive.7z ./folder
  ```

- Do the same as above, but split the archive in 50 Mib volumes:

  ```shell-session
  $ 7za a -v50m archive.7z ./folder
  ```

## shar

- Extract content from [self-extracting shell archives](https://en.wikipedia.org/wiki/Shar):

  ```shell-session
  $ unshar archive.sh
  ```

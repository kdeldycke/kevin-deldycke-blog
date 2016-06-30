---
date: 2006-10-18 00:15:16
title: File Management commands
category: English
tags: CLI, find, grep, Linux, Python, rename, sort, tail, regular expression, Dropbox
---

  * Create several folder with a similar pattern:

        :::bash
        $ mkdir -p ./folder/subfolder{001,002,003}

  * Create a symbolic link ([source](http://news.ycombinator.com/item?id=1984792)):

        :::bash
        $ ln -s target link_name

  * List size in MiB of subfolders and files in the current folder and display them sorted by size:

        :::bash
        $ du -cm * | sort -nr

  * Count the number of files in a folder:

        :::bash
        $ find ./ -type f | wc -l

  * List number of files accross all subfolders sharing the same name, whatever their extension is:

        :::bash
        $ find . -type f -exec basename {} \; | sed 's/\(.*\)\..*/\1/' | sort | uniq -c | grep -v "^[ \t]*1 "

  * List all file extensions found in a folder:

        :::bash
        $ find ./ -type f | rev | cut -d "." -f 1 | sort | uniq | rev

  * Show the 10 biggest files in MiB found amoung the current directory and its subfolders:

        :::bash
        $ find . -type f -exec du -m "{}" \; | sort -nr | head -n 10

  * Case insensitive search from the current folder of all files that have the string `dummy` in their filename:

        :::bash
        $ find ./ -iname "*dummy*"

  * Recursive and case insensitive content search on non-binary files from the current folder:

        :::bash
        $ grep -RiI "string to search" ./*

  * Same as above but only search string in XML files:

        :::bash
        $ find ./* -iname "*.xml" -exec grep -Hi "string to search" "{}" \;

  * Find all Jpeg images in the system but exclude `/home` and `/var/lib` directory:

        :::bash
        $ find / -path "/home" -prune -or -path "/var/lib" -prune -or -iname "*.jpg" -print

  * Get the list of the latest 10 modified files in the current folder tree:

        :::bash
        $ find ./ -printf "%TY-%Tm-%Td %TT %p\n" | sort | tail -n10

  * Same as above but sorted by latest access time:

        :::bash
        $ find ./ -printf "%AY-%Am-%Ad %AT %p\n" | sort | tail -n10

  * Rename all mp3 files in the current folder by adding a "sub-extension":

        :::bash
        $ rename 's/\.mp3/\.my-sub-extension\.mp3/' *.mp3

  * Prefix all files in the current folder:

        :::bash
        $ rename 's/(.*)$/prefix-$1/' *

  * Convert all files in the current folder to lower case:

        :::bash
        $ rename 'y/A-Z/a-z/' *

  * Renaming based on regular expression, for files matching another regular expression. The particular example below was used to fix some Dropbox conflicting files:

        :::bash
        $ find ./Dropbox -type f -name "* (kev-laptop's conflicted copy 2013-02-01)*" -execdir rename -f -v "s/(.*) \(kev-laptop's conflicted copy 2013-02-01\)(.*)/\1\2/" {} \;

  * Display the total size used by all PNG files in sub-directories:

        :::bash
        $ find ./ -iname "*.png" -exec du -k "{}" \; | awk '{c+=$1} END {printf "%s KB\n", c}'

  * List all files sharing the same name within the sub folders:

        :::bash
        $ find . -type f -printf "%f\n" | sort | uniq --repeated --all-repeated=separate

  * Delete all empty files and folders (run this command several times to remove nested empty directories):

        :::bash
        $ find ./ -empty -print -exec rm -rf "{}" \;

  * Remove empty directories found in all subfolders starting with a dot:

        :::bash
        $ find ./ -type d -empty -ipath "./.*" -print -exec rm -rf "{}" \;

  * Delete files ending with `.thumbnail.jpg` or `.thumbnail.png` files (case insensitive):

        :::bash
        $ find ./ -iregex ".*\.thumbnail\.\(jpg\|png\)$" -delete

  * Same as above but instead for files ending with their dimensions, like `image-640x480.jpg` or `photo-2400x3200.png`:

        :::bash
        $ find ./ -iregex ".*-[0-9]+x[0-9]+\.\(jpg\|png\)$" -delete

  * I used those commands when I import big quantity of files from a window user:

        :::bash
        $ find ./ -name "desktop.ini" -print -delete
        $ find ./ -name "Thumbs.db" -print -delete

  * Delete all files and folders in the current directory except the `README.txt` file:

        :::bash
        $ ls ./ -I "README.txt" | xargs rm -rf

  * Search for `string` contained in all files named `MANIFEST.in`, and print their folder path:

        :::bash
        $ find . -name "MANIFEST.in" -exec bash -c 'grep --silent "string" "{}" && echo $(dirname "{}")' \;

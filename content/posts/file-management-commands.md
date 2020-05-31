---
date: 2006-10-18 00:15:16
title: File Management commands
category: English
tags: CLI, find, grep, Linux, Python, rename, sort, tail, regular expression, Dropbox, git, rmlint, fd, rsync
---

## Listing

  * Count the number of files in a folder:

        :::shell-session
        $ find ./ -type f | wc -l

  * List all file extensions found in a folder:

        :::shell-session
        $ find ./ -type f | rev | cut -d "." -f 1 | sort | uniq | rev

  * List all files sharing the same name within the sub folders:

        :::shell-session
        $ find . -type f -printf "%f\n" | sort | uniq --repeated --all-repeated=separate

  * List number of files accross all subfolders sharing the same name, whatever their extension is:

        :::shell-session
        $ find . -type f -exec basename {} \; | sed 's/\(.*\)\..*/\1/' | sort | uniq -c | grep -v "^[ \t]*1 "


## Size & Space

  * List size in MiB of subfolders and files in the current folder and display them sorted by size:

        :::shell-session
        $ du -cm * | sort -nr

  * Show the 10 biggest files in MiB found amoung the current directory and its subfolders:

        :::shell-session
        $ find . -type f -exec du -m "{}" \; | sort -nr | head -n 10

  * Display the total size used by all PNG files in sub-directories:

        :::shell-session
        $ find ./ -iname "*.png" -exec du -k "{}" \; | awk '{c+=$1} END {printf "%s KB\n", c}'


## Search

  * Case insensitive search from the current folder of all files that have the string `dummy` in their filename:

        :::shell-session
        $ find ./ -iname "*dummy*"

  * Recursive and case insensitive content search on non-binary files from the current folder:

        :::shell-session
        $ grep -RiI "string to search" ./*

  * Same as above but only search string in XML files:

        :::shell-session
        $ find ./* -iname "*.xml" -exec grep -Hi "string to search" "{}" \;

  * Find all Jpeg images in the system but exclude `/home` and `/var/lib` directory:

        :::shell-session
        $ find / -path "/home" -prune -or -path "/var/lib" -prune -or -iname "*.jpg" -print

  * Get the list of the latest 10 modified files in the current folder tree:

        :::shell-session
        $ find ./ -printf "%TY-%Tm-%Td %TT %p\n" | sort | tail -n10

  * Same as above but sorted by latest access time:

        :::shell-session
        $ find ./ -printf "%AY-%Am-%Ad %AT %p\n" | sort | tail -n10

  * Search for `string` contained in all files named `MANIFEST.in`, and print their folder path:

        :::shell-session
        $ find . -name "MANIFEST.in" -exec bash -c 'grep --silent "string" "{}" && echo $(dirname "{}")' \;

  * Search for 4+ characters long upper-cased strings with underscore, in all files but the `README.md`, `LICENSE` and Git metadata:

        :::shell-session
        $ grep --only-matching --no-filename --exclude=./{README.md,LICENSE,.git\*} -RIe '[A-Z_]\{4,\}' . | sort | uniq

  * Search all files starting with a dot, and ending with an extension composed of 6 alphanumeric characters. These are temporary files created by rsync:

        :::shell-session
        $ fd --type file --hidden --ignore-case "^\..+\.[0-9a-z]{6}$"


## Creation

  * Create several folder with a similar pattern:

        :::shell-session
        $ mkdir -p ./folder/subfolder{001,002,003}

  * Create a symbolic link ([source](https://news.ycombinator.com/item?id=1984792)):

        :::shell-session
        $ ln -s target link_name


## Renaming

  * Convert all files in the current folder to lower case:

        :::shell-session
        $ rename 'y/A-Z/a-z/' *

  * Prefix all files in the current folder:

        :::shell-session
        $ rename 's/(.*)$/prefix-$1/' *

  * Rename all mp3 files in the current folder by adding a "sub-extension":

        :::shell-session
        $ rename 's/\.mp3/\.my-sub-extension\.mp3/' *.mp3

  * Renaming based on regular expression, for files matching another regular expression. The particular example below was used to fix some Dropbox conflicting files:

        :::shell-session
        $ find ./Dropbox -type f -name "* (kev-laptop's conflicted copy 2013-02-01)*" -execdir rename -f -v "s/(.*) \(kev-laptop's conflicted copy 2013-02-01\)(.*)/\1\2/" {} \;

  * Strip filenames of their leading dot and extension composed of 6 alphanumeric characters. These are temporary files created by rsync:

        :::shell-session
        $ rename --force --dry-run 's/^\.(.+)\.[0-9a-zA-Z]{6}$/$1/' *


## Cleaning-up

  * Delete all empty files and folders (run this command several times to remove nested empty directories):

        :::shell-session
        $ find ./ -empty -print -delete

  * Remove empty directories found in all subfolders starting with `prefix`:

        :::shell-session
        $ find ./ -type d -empty -ipath "./prefix*" -print -delete

  * Delete files ending with `.thumbnail.jpg` or `.thumbnail.png` files (case insensitive):

        :::shell-session
        $ find ./ -iregex ".*\.thumbnail\.\(jpg\|png\)$" -print -delete

  * Same as above but instead for files ending with their dimensions, like `image-640x480.jpg` or `photo-2400x3200.png`:

        :::shell-session
        $ find ./ -iregex ".*-[0-9]+x[0-9]+\.\(jpg\|png\)$" -print -delete

  * I used those commands when I import big quantity of files from a window user:

        :::shell-session
        $ find ./ -name "desktop.ini" -print -delete
        $ find ./ -name "Thumbs.db" -print -delete

  * Delete all files and folders in the current directory except the `README.txt` file:

        :::shell-session
        $ ls ./ -I "README.txt" | xargs rm -rf

  * Remove all duplicates within the whole pool of files (including `--hidden` ones) build up from `folder-1`, `folder-2` and `folder-3` directories. In a set of duplicates, the first file in alphabeticcaly sorted named path is kept (`-S p` option).

        :::shell-session
        $ rmlint --progress --hidden -S p ./folder-1 ./folder-2 ./folder-3
        $ ./rmlint.sh

  * Remove all duplicates in `backup-set1` and `backup-set2` if and only if they're already present in `backup-set3` (i.e. the reference folder tagged after the `//` separator), but do not alter the latter in anyway (thanks to the `--keep-all-tagged` option). To make things extra-safe we use `--no-crossdev` to not jump to other physical file systems:

        :::shell-session
        $ rmlint --progress --hidden --no-crossdev --keep-all-tagged ./backup-set1/ ./backup-set2/ // ./backup-set3/
        $ ./rmlint.sh 

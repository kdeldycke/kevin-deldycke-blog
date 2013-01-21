comments: true
date: 2006-10-18 00:15:16
layout: post
slug: file-management-commands
title: File Management commands
wordpress_id: 70
category: English
tags: CLI, find, grep, Linux, Python, rename, sort, tail




  * Create several folder with a similar pattern:


        :::console
        mkdir -p ./folder/subfolder{001,002,003}







  * Create a symbolic link ([source](http://news.ycombinator.com/item?id=1984792)):


        :::console
        ln -s target link_name







  * List size in MiB of subfolders and files in the current folder and display them sorted by size:


        :::console
        du -cm * | sort -nr







  * Count the number of files in a folder:


        :::console
        find ./ -type f | wc -l







  * Show the 10 biggest files in MiB found amoung the current directory and its subfolders:


        :::console
        find . -type f -exec du -m "{}" \; | sort -nr | head -n 10







  * Case insensitive search from the current folder of all files that have the string `dummy` in their filename:


        :::console
        find ./ -iname "*dummy*"







  * Recursive and case insensitive content search on non-binary files from the current folder:


        :::console
        grep -RiI "string to search" ./*







  * Same as above but only search string in XML files:


        :::console
        find ./* -iname "*.xml" -exec grep -Hi "string to search" "{}" \;







  * Find all Jpeg images in the system but exclude `/home` and `/var/lib` directory:


        :::console
        find / -path "/home" -prune -or -path "/var/lib" -prune -or -iname "*.jpg" -print







  * Get the list of the latest 10 modified files in the current folder tree:


        :::console
        find ./ -printf "%TY-%Tm-%Td %TT %p\n" | sort | tail -n10







  * Same as above but sorted by latest access time:


        :::console
        find ./ -printf "%AY-%Am-%Ad %AT %p\n" | sort | tail -n10







  * Rename all mp3 files in the current folder by adding a "sub-extension":


        :::console
        rename "s/\.mp3/\.my-sub-extension\.mp3/g" *.mp3







  * Convert all files in the current folder to lower case:


        :::console
        rename 'y/A-Z/a-z/' *







  * Display the total size used by all PNG files in sub-directories:


        :::console
        find ./ -iname "*.png" -exec du -k "{}" \; | awk '{c+=$1} END {printf "%s KB\n", c}'







  * List all files sharing the same name within the sub folders:


        :::console
        find . -type f -printf "%f\n" | sort | uniq --repeated --all-repeated=separate











## Dangerous Commands








  * Delete all `.pyc` and `.pyo` files in the system:


        :::console
        find / -name "*.py[co]" | xargs rm







  * Delete all empty files and folders (run this command several times to remove nested empty directories):


        :::console
        find . -empty -print -exec rm -rf "{}" \;







  * Remove empty directories found in all subfolders starting with a dot:


        :::console
        find . -type d -empty -ipath "./.*" -print -exec rm -rf "{}" \;







  * I used those commands when I import big quantity of files from a window user:


        :::console
        find ./* -name "desktop.ini" -print -exec rm -f "{}" \;
        find ./* -name "Thumbs.db" -print -exec rm -f "{}" \;







  * Delete all files and folders in the current directory except the `README.txt` file:


        :::console
        ls ./ -I "README.txt" | xargs rm -rf








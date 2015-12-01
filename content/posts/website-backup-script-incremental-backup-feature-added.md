---
date: 2006-11-02 23:19:03
title: Website Backup script: Incremental Backup feature added.
category: English
tags: Backup, bzip2, CLI, FTP, lftp, Linux, Network, Python, Web
---

I've changed my backup strategy today, so I updated my [website-backup.py script](https://github.com/kdeldycke/scripts/blob/master/website-backup.py). You can find the latest version of the script on [my script page](http://kevin.deldycke.com/code/).

I now use [rdiff-backup](http://www.nongnu.org/rdiff-backup/) in this script to keep 32 days of incremental backups. Beside this the script do a monthly full archive of the website in bzip2 format. This new strategy has reduced the total size of my backups from 64 GB to 6.7 GB. Roughly 90% of free space gain thanks to rdiff-backup ! If rdiff-backup is so efficient in my case, this is due to the existence on my websites of large files that are rarely modified (Mp3s, Flacs, RPMs, images, etc...).

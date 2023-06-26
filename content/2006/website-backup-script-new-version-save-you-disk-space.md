---
date: "2006-10-30"
title: "Website Backup script: New Version Save you Disk Space."
category: English
tags: Backup, bzip2, CLI, FTP, lftp, Linux, Python, Web
---

I've updated [my `website-backup.py` script]({filename}/2006/script-to-automate-ftp-site-backup.md). I added a little optimization to delete the yesterday's backup if nothing was changed on the remote website. This let me save some megabytes on the hard drive for everyday backups of near-static websites. The optimization I added is simply based on checksum comparison. This is the context to the [previous script I wrote today]({filename}/2006/find-duplicate-files-in-a-folder.md): it was a tool to help me debug and experiment this new feature.

You can find the latest version of the `website-backup.py` script in my [Linux script page](https://github.com/kdeldycke/scripts). Here is the [direct link to today's version](https://github.com/kdeldycke/scripts/blob/master/website-backup.py).

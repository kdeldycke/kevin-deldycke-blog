date: 2006-12-25 12:54:43
slug: website-backup-script-updated-take-care-of-hidden-files-now
title: Website Backup Script Updated: Take Care of Hidden Files now.
tags: Backup, FTP, lftp, Linux, Python, rdiff-backup, Server, Web

I've [updated my website-backup python script](https://github.com/kdeldycke/scripts/blob/master/website-backup.py).

Change log:

  * Use `set ftp:list-options -a` command to force lftp to download hidden files (like `.htaccess` and so on).

  * Use `--force` parameter to allow auto-deletion of multiple outdated rdiff-backup increments.

  * Defensive incremental backup policy: keep 32 last backups instead of 32 days of backup.

I also added a debug mode as [suggested by Sacha](http://kevin.deldycke.com/2006/11/website-backup-script-incremental-backup-feature-added/#comment-957).

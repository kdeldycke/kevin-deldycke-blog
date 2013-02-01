date: 2007-04-09 07:01:35
slug: system-backup-on-unreliable-link-thanks-to-rdiff-backup-and-rsync
title: System Backup on Unreliable Link thanks to rdiff-backup and rsync
category: English
tags: Backup, CLI, Linux, Python, rdiff-backup, rsync, Script, SSH

I've just write a brand new script called [`system-backup.py`](https://github.com/kdeldycke/scripts/blob/master/system-backup.py). It's [similar to my `website-backup.py` script](http://kevin.deldycke.com/2007/03/website-backup-script-mysql-dumps-and-ssh-supported/) but instead of website and MySQL databases, it is designed to backup systems of several machines. This script is based on an idea from the "[Backup up on unreliable link](http://wiki.rdiff-backup.org/wiki/index.php/BackupUpOnUnreliableLink)" article from the [official rdiff-backup wiki](http://wiki.rdiff-backup.org). It use `rdiff-backup` to keep the last 20 backups and `rsync` to speed-up the backup process.

I run this script to backup all the local machines within my LAN. I start the backup process everyday thanks to a `cron` entry similar to this one:

    :::text
    0 20 * * * root /root/system-backup.py >> /mnt/backup-disk/backup.log

If you need more information about the `rsync` part the script, please have a look to my previous [Remote Backup with rsync](http://kevin.deldycke.com/2005/04/remote-backup-with-rsync/) article, which detail how-to setup key authentification with `ssh`.

---
date: 2006-04-30 23:14:46
title: Script to Automate FTP site Backup.
category: English
tags: Backup, bzip2, FTP, lftp, Linux, Python
---

Based on [my yesterday experimentations](https://kevin.deldycke.com/2006/04/bad-ftp-mirrors-with-fmirror-or-wget-use-lftp/), I've code today a little script to automate the backup of several websites of mine. This script use `lftp` to mirror file from a remote host to your local machine. Then it create a `bzip2` archive.

You can [download the script here](https://github.com/kdeldycke/scripts/blob/master/website-backup.py). To make it working, you need python on your system. To configure it, edit the `ftpsite_list` python list in the beginning of the file.

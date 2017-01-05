---
date: 2008-05-26 01:38:44
title: Website Backup Script: bug fix release
category: English
tags: Backup, CLI, FTP, lftp, Linux, MySQL, SQL, mysqldump, Network, Python, rdiff-backup, rsync, Script, Server, SSH, Web
---

[14 months after the last release](https://kevin.deldycke.com/2007/03/website-backup-script-mysql-dumps-and-ssh-supported/), here is a [new version of my website backup script](https://github.com/kdeldycke/scripts/blob/master/website-backup.py). As you can see in the changelog, this version is essentially released to fix some bugs.

Changelog:

  * Check version of Python (at least v2.4 is required)

  * Rename `--debug` option to `--verbose`

  * Add a `--dry-run` option for testing

  * Remove use of deprecated `pexpect` methods

  * Add and update some error messages


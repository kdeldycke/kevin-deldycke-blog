date: 2007-03-25 11:17:09
slug: website-backup-script-mysql-dumps-and-ssh-supported
title: Website Backup Script: MySQL dumps and SSH supported.
category: English
tags: Backup, CLI, FTP, lftp, Linux, MySQL, SQL, mysqldump, Network, Python, rdiff-backup, rsync, Script, Server, SSH, Web

[Three months after the last version](http://kevin.deldycke.com/2006/12/website-backup-script-updated-take-care-of-hidden-files-now/), here is a big update of [my backup scripts for websites](https://github.com/kdeldycke/scripts/blob/master/website-backup.py). The script was greatly improved and among new features, the most important is the support of backups over SSH and backups of MySQL databases.

Change log:

  * Each item of the user's `backup_list` must specify the `type` property (`FTP`, `FTPs`, `SSH`, `MySQLdump` or `MySQLdump+ssh`).

  * The property previously known as `site` is now `host`.

  * File system structure changed: `/ftp-mirror` folders renamed to `/mirror`.

  * Add SSH backups.

  * The script is able to detect if a SSH connexion can be initiated without a password. This was designed for people who don't like the idea of storing clear password in the script. Thanks to this feature, you can benefit public key authentication from OpenSSH.

  * Use of `rsync` whenever it's possible for bandwidth efficiency.

  * FTP and FTPs (aka FTP over SSL) are now handled separately: this suppress the default fall-back to FTP if FTPs is not supported by the remote server. This is safer as it doesn't let `lftp` make the decision for you to send your clear password on the net.

  * All ports are optionnal, no need to specify it you use default ports.

  * Add MySQL backups thanks to `mysqldump`.

  * Two mode of MySQL backups: through SSH or direct connection to server.

  * A particular database to backup can be specified. Else, all databases are backed up.

  * Much more detailed logs that include external command's output.

  * Auto-detect the existence of required external tools and commands at launch.

  * Use `pexpect` lib to simulate user password input.

  * Run all external commands in english for consistency.

  * Check that the script is running in a posix environnement.

  * Fix bug related to directory creation.

If you were using a previous version of my backup script and want to use this updated version, take care of changes, especially the ones describes in the first 3 items of the change log above.

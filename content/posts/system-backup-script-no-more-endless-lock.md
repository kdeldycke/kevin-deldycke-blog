comments: true
date: 2007-08-12 17:00:45
layout: post
slug: system-backup-script-no-more-endless-lock
title: System backup script: no more endless lock
wordpress_id: 200
tags: Backup, CLI, Linux, Python, rdiff-backup, rsync, Script, SSH, system

I've just released a [new version of my `system-backup.py` script](http://kevin.deldycke.com/static/scripts/system-backup-2007_08_12.py).

The main update is about the lock file, which I implemented in the [last version](http://kevin.deldycke.com/2007/04/system-backup-auto-clean-and-lock-added/) to keep the script to run twice (or more) in parallel. This is a nice feature to avoid overlapping processes that fight each other to use the same ressources. But in some extreme cases (reboot or power failure during backup, ...), the lock file will remain and so will prevent the script to start (until you notice the problem and remove the lock file manually). This new version take care of this problem and is now able to remove the lock automatically if a timeout is reached. It also kill all remaining child processes.

Here is the detailed changelog:




  * Auto-kill the script if the backup process take to much time. Timeout can be defined via a constant.


  * Clean kill: track all child processes to kill them safely before removing the lock file.


  * Require newer versions of python (>= v2.4), rsync (>= v2.6.7) and rdiff-backup (>= v1.1.0).


  * Use `--preserve-numerical-ids` option when adding rdiff-backup increment.


  * Keep 15 increments by default instead of 20. This value can be easily changed thanks to a defined constant.


  * Remove deleted file first during mirroring and delete outdated increments before adding a new one to gain space. This strategy is safer for target disk with low remaining free space.


  * Tell rsync to print human-readable values.



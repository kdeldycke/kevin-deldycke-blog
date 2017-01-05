---
date: 2007-04-27 20:41:51
title: System Backup: Auto-Clean and Lock added
category: English
tags: Backup, Linux, Python, rdiff-backup, rsync, system, cron
---

I've updated the [system backup script I've released 3 weeks ago](https://kevin.deldycke.com/2007/04/system-backup-on-unreliable-link-thanks-to-rdiff-backup-and-rsync/) to let it clean automatically `rdiff-backup` folders. This is mandatory because incremental backup process is transactionnal and a power failure or a reboot can break the consistency of the `rdiff-backup` data repository. So even if such a misfortune happened, the script will be able to revert backups to a previously consistent state.

I've also added a locking mechanism to prevent the script to be run twice on the same machine. I've added this feature because I start my script every day thanks to `cron` and some backups can take more than one day.

Finally, all `rsync` commands will now be run first to reduce the time-window during which all external machines are reached and, as mentionned above, because `rdiff-backup` can take lots of time to finish its job.

Here is a [direct link to the new version of the script](https://wordpress.org/extend/plugins/e107-importer/). You can also find it in [my page dedicated to various linux scripts](https://kevin.deldycke.com/code/).

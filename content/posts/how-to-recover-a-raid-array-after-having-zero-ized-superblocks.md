---
date: 2007-03-07 22:48:52
title: How-to Recover a RAID array after having Zero-ized Superblocks
category: English
tags: Backup, Hardware, Linux, mdadm, RAID, Server
---

Today `mdadm` send me a mail to warn that one of my hard drive (`/dev/hdd1`) was ejected from my RAID-5 array. After some manipulations (no writes, just reads on the file system to get informations) and reboots, I ended up with a file system in a strange state: the folder structure was totally messed up and lots of files disappeared.

Assuming that this situation was about an inconsistent file index, I decided to reset the superblocks of the remaining physical disks:

    :::bash
    $ mdadm --zero-superblock /dev/hdc1
    $ mdadm --zero-superblock /dev/hdb1

I don't know why I decided to do so, but it was the stupidest idea of the week. After such a violent treatment, my array refused to start:

    :::bash
    $ mdadm --assemble /dev/md0 --auto --scan --update=summaries --verbose
    mdadm: looking for devices for /dev/md0
    mdadm: no RAID superblock on /dev/hdc1
    mdadm: /dev/hdc1 has wrong raid level.
    mdadm: no RAID superblock on /dev/hdb1
    mdadm: /dev/hdb1 has wrong raid level.
    mdadm: no devices found for /dev/md0

At this moment I was sure that all my data assets were lost. I was desperate. My only alternative was to ask Google. So I did.

I spend several minutes browsing the web without hope. I finally found [someone in the same situation as mine](http://lists.debian.org/debian-user-french/2006/03/msg00602.html) (sorry, in french) on debian-user-french mailing list.

The solution was to recreate the RAID array. This sound counter-intuitive: if we recreate a raid array over an existing one, it will be erased! Right? Wrong! [As it is said on debian-user-french](http://lists.debian.org/debian-user-french/2006/03/msg00607.html), `mdadm` is smart enough to "see" that HDD of the new array were elements of a previous one. Knowing that, `mdadm` will try to do its best (i.e. if parameters match the previous array configuration) and rebuild the new array upon the previous one in a non-destructive way, by keeping HDD content.

So, here is how I finally recovered my RAID array:

    :::bash
    $ mdadm --create /dev/md0 --verbose --level=5 --raid-devices=3 /dev/hdc1 missing /dev/hdb1
    mdadm: layout defaults to left-symmetric
    mdadm: chunk size defaults to 64K
    mdadm: size set to 312568576K
    mdadm: array /dev/md0 started.

Of course this doesn't solve my initial problem about the `/dev/md0` file system: it is still in an altered state. Maybe it's too late to recover data. But at least I reverted all my today's mistakes, and the situation will not deteriorate until I power up my RAID! :)

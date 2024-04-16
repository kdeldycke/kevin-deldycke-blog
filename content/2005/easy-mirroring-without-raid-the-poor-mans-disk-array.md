---
date: '2005-07-24'
title: "Easy Mirroring Without RAID: the Poor Man's Disk Array"
category: English
tags: Backup, CLI, Hardware, kernel, Linux, openbrick, RAID, rsync, USB, XFS, cron
---

This howto explain how to use `rsync` to build a data mirroring mechanism on a local machine, with two hard drives, ala [RAID 1](https://en.wikipedia.org/wiki/RAID1), but without RAID 1 (!).

I had the [project to setup a RAID 5 array using 3\*120 Gb hard drives in USB enclosures]({filename}/2005/creer-un-espace-de-stockage-fiable-avec-raid-5-et-lvm-sous-linux.md). Unfortunately my project stalled due to instability in early 2.6.x kernels (I heard that 2.6.12 and upper are now useable for "RAID over USB").

Because of the urgency of reliable storage (and because I don't want to waste time compiling and fine-tuning kernels), I decided to do it using traditional IDE host. So I plugged two 120Gb HDD on my machine as master device, one on each IDE channel.

![Open Brick NG and RAID-1-like setup]({attach}photo_f3.jpg)

Then I made a big XFS partition on each, and update my `/etc/fstab`:

```text
/dev/sda1 /                auto  noatime   1 1
/dev/hda1 /mnt/hd1         xfs   defaults  1 2
/dev/hdc1 /mnt/hd1_mirror  xfs   defaults  1 2
```

At that moment I have to explain you that my machine is an [OpenBrick NG](https://web.archive.org/web/20060822232700/https://www.storever.com/product/openbrick/openbrick-ng), with a USB 2.0 512 Mb thumb drive (`/dev/sda1` in the fstab) on which all my linux system is installed. That explain why my two IDE channels are free for use.

The idea is now to use `/mnt/hd1` to store and manipulate my data, then `rsync` that drive with his alter-ego (`/mnt/hd1_mirror`) every night. To do that, I've just added the following command in a cron entry:

```shell-session
$ rsync -a --delete --delete-excluded --delete-after /mnt/hd1/ /mnt/hd1_mirror/
```

And voilà!

As you guess, this solution is far from perfect, and has major inconvenients regarding RAID 1:

- No immediate backup : the backuped data are 1-day old;
- Seek time is not reduce by half;
- Transfer rate is not doubled.

Oh, and by the way, be careful to not write files on `/mnt/hd1_mirror/` because they will be deleted each night during the mirroring process.

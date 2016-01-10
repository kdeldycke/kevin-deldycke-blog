---
date: 2006-12-06 23:18:55
title: Hardware commands
category: English
tags: CLI, gpart, Hardware, HDD, kernel, Linux, MBR, partitions, X.org, gphoto, DSLR, Canon EOS 7D
---

  * Get the number of shutter count of a DSLR (Canon EOS 7D in my case):

        :::bash
        $ gphoto2 --get-config /main/status/shuttercounter
        Label: Shutter Counter
        Type: TEXT
        Current: 49238

  * Change the keyboard layout in Debian (don't forget to logoff and logon to activate the new setting):

        :::bash
        $ dpkg-reconfigure keyboard-configuration

  * Low-level format of the `hda` device:

        :::bash
        $ dd if=/dev/zero of=/dev/hda

  * Same as above but for paranoïd, as random bits will be written 3 times before performing the "low-level format" (i.e. writting zeros):

        :::bash
        $ shred --verbose --force --iterations=3 --zero /dev/hda

  * Remove the MBR:

        :::bash
        $ dd if=/dev/null of=/dev/hda bs=446 count=1

  * Restore the original Windows MBR:

        :::bash
        $ apt-get install mbr
        $ install-mbr -i n -p D -t 0 /dev/hda

  * Guess the partition table of a device, including damaged ones:

        :::bash
        $ gpart -v /dev/md0

  * To add touchpad kernel support, add the following option to kernel at boot time:

        :::bash
        $ psmouse.proto=imps

  * Sometimes, depending of the laptop I use, the mouse pointer disappear from the screen when I plug a VGA cable to a projector. In this case, I do a `CTRL + ALT + F1`, then I login as a normal user and finally I start a new X session:

        :::bash
        $ startx -- :1


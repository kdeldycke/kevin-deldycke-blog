---
date: 2012-05-08 12:42:59
title: VirtualBox commands
category: English
tags: disk, image, VirtualBox, virtualization
---

  * Clone a virtual disk image:

        :::bash
        $ VBoxManage clonehd original-disk.vdi copy.vdi

  * Resize a virtual disk image to 20 Gb:

        :::bash
        $ VBoxManage modifyhd disk.vdi --resize 20000

  * Convert a VirtualBox image to a raw image:

        :::bash
        $ VBoxManage clonehd --format RAW disk.vdi disk.raw

  * Convert a raw image to a VirtualBox image:

        :::bash
        $ VBoxManage convertdd disk.raw disk.vdi --format VDI

  * List virtual machines:

        :::bash
        $ VBoxManage list vms

  * Fix broken NAT ([source](http://askubuntu.com/questions/216865/vitualbox-nat-stopped-working-after-ubuntu-upgrade-to-12-10)):

        :::bash
        $ VBoxManage modifyvm "name" --natdnshostresolver1 on
        $ VBoxManage modifyvm "name" --natdnsproxy1 on

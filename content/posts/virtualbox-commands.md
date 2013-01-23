comments: true
date: 2012-05-08 12:42:59
layout: post
slug: virtualbox-commands
title: VirtualBox commands
wordpress_id: 4570
category: English
tags: disk, image, VirtualBox, virtualization

  * Clone a virtual disk image:

        :::bash
        $ VBoxManage clonehd original-disk.vdi copy.vdi

  * Resize a virtual disk image to 20 Gb:

        :::bash
        $ VBoxManage modifyhd disk.vdi --resize 20000

  * List virtual machines:

        :::bash
        $ VBoxManage list vms


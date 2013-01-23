comments: true
date: 2007-04-08 16:10:56
layout: post
slug: how-to-grow-any-qemu-system-image
title: How-to grow any Qemu system image
wordpress_id: 151
category: English
tags: gparted, Linux, qcow, Qemu, system, windows

Qemu images can't be growed. In this example I will show you a little hack to grow a 6GiB `qcow` image to a 10GiB image. Beware: these operations can take a lot of time to perform and require lots of free space.

First, convert your `qcow` image to a plain raw file:

    :::bash
    $ qemu-img convert system.qcow -O raw system.raw

Then, create a dummy file (filled with zeros) of the size of extra space you want to add to your image. In this case, 4GiB (=10GiB - 6GiB):

    :::bash
    $ dd if=/dev/zero of=zeros.raw bs=1024k count=4096

Fearlessly, add your extra space to your raw system image:

    :::bash
    $ cat system.raw zeros.raw > big10G.raw

After that you can boot qemu to verify that added free space is available:

    :::bash
    $ qemu -hda big10G.raw

Here is an real case example of what you can see in a qemu image on which Windows XP was installed:
[![](http://kevin.deldycke.com/wp-content/uploads/2007/04/growed-image1-300x233.png)](http://kevin.deldycke.com/wp-content/uploads/2007/04/growed-image1.png)

Now, to grow your primary partition, I suggest you to download a Live CD like [gparted Live CD](http://gparted.sourceforge.net/livecd.php) or [System Rescue CD](http://www.sysresccd.org), and boot on the `.iso` file with qemu:

    :::bash
    $ qemu -hda big10G.raw -cdrom gparted-livecd-0.3.4-5.iso -boot d

This will allow you to grow and manipulate all your partitions safely thanks to [parted](http://www.gnu.org/software/parted/index.shtml) and other open source system tools.

Finally you can convert back your `raw` image to a `qcow` one to not waste space:

    :::bash
    $ qemu-img convert big10G.raw -O qcow growed-system.qcow

That's all !

By the way, I think it's possible to perform the second and third step of this how-to in a single operation using `dd` only.

_Update_: I missed it, but this issue is also described in the FAQ from the [unofficial #qemu wiki](http://kidsquid.com/cgi-bin/moin.cgi) (look at "[How do I resize a disk image?](http://kidsquid.com/cgi-bin/moin.cgi/FrequentlyAskedQuestions#head-b46370d3ad030e6c1712338f0e5112228c51212a)" question).

---
date: 2009-08-02 16:29:59
title: dmg2img for Mandriva 2009.1
category: English
tags: Apple, CLI, dm2img, dmg, HFS, Linux, Mandriva, RPM
---

![package](/uploads/2009/package.png)

I've just created a RPM of [dmg2img](https://vu1tur.eu.org/tools/) for the x86_64 version of Mandriva 2009.1. The package is [available in my RPM repository](https://github.com/kdeldycke/mandriva-specs).

`dmg2img` is a command line utility to extract the content of an [Apple Disk Image](https://en.wikipedia.org/wiki/Apple_Disk_Image) `.dmg` file. Here is how I use it to access content:

    :::shell-session
    $ dmg2img ./my-package.dmg
    $ mount -t hfsplus -o loop ./my-package.img /media/my-mount-point


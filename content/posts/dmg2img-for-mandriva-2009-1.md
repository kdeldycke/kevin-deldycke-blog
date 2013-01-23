comments: true
date: 2009-08-02 16:29:59
layout: post
slug: dmg2img-for-mandriva-2009-1
title: dmg2img for Mandriva 2009.1
wordpress_id: 790
category: English
tags: Apple, CLI, dm2img, dmg, HFS, Linux, Mandriva, RPM

![package](http://kevin.deldycke.com/wp-content/uploads/2009/08/package.png) I've just created a RPM of [dmg2img](http://vu1tur.eu.org/tools/) for the x86_64 version of Mandriva 2009.1. The package is [available in my RPM repository](http://kevin.deldycke.com/static/repository/mandriva/2009.1/x86_64/).

`dmg2img` is a command line utility to extract the content of an [Apple Disk Image](http://en.wikipedia.org/wiki/Apple_Disk_Image) `.dmg` file. Here is how I use it to access content:

    :::bash
    $ dmg2img ./my-package.dmg
    $ mount -t hfsplus -o loop ./my-package.img /media/my-mount-point


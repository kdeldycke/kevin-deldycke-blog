comments: true
date: 2006-07-28 23:39:19
layout: post
slug: why-kqemu-doesnt-do-its-job
title: Why kqemu doesn't do its job ?
wordpress_id: 27
tags: Linux, Qemu

I was using [qemu](http://fabrice.bellard.free.fr/qemu/) for more than 1 year, but I only noticed today that [kqemu](http://fabrice.bellard.free.fr/qemu/qemu-accel.html), which is supposed to speed qemu up, was not working on my machine: there was absolutely no differences with or without kqemu.

I finally found the reason on the qemu website FAQ: [Why has kqemu not improved the speed of qemu on my Linux system?](http://kidsquid.com/cgi-bin/moin.cgi/FrequentlyAskedQuestions#head-909015808a3a29b67ccbb65c8b089017d5cd97aa).

So, if you are using my kqemu RPM for Mandriva 2006, don't forget to add the following line in your `/etc/fstab` file:

    :::text
    tmpfs    /dev/shm    tmpfs    defaults    0  0

Then reboot your OS to enjoy the speed up !

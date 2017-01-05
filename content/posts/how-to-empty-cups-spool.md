---
date: 2005-04-04 22:16:55
title: How-to empty CUPS spool
category: English
tags: CUPS, Linux, printing, Script, Server, shell, cron
---

Here is a tiny helper script I call regularly by a `cron` job to flush the spool
of my [CUPS server](https://en.wikipedia.org/wiki/Common_Unix_Printing_System) as
after several weeks of usage my server end up full of unprinted documents junk:

    :::sh
    #/bin/sh!
    service cups stop
    rm -f /var/spool/cups/*
    rm -f /var/spool/cups/tmp/*
    service cups restart

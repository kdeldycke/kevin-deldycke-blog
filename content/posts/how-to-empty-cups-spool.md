comments: true
date: 2005-04-04 22:16:55
layout: post
slug: how-to-empty-cups-spool
title: How-to empty CUPS spool
wordpress_id: 276
category: English
tags: bash, CUPS, Linux, printing, Script, Server, shell, Snippet

Here is a tiny helper script I call regularly by a `cron` job to flush the spool of my [CUPS server](http://en.wikipedia.org/wiki/Common_Unix_Printing_System) as after several weeks of usage my server end up full of unprinted documents junk:

    
    :::console
    #/bin/sh!
    service cups stop
    rm -f /var/spool/cups/*
    rm -f /var/spool/cups/tmp/*
    service cups restart
    

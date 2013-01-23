comments: true
date: 2007-02-28 21:49:57
layout: post
slug: repository-moved-thanks-to-apache-and-301-redirections
title: Repository Moved thanks to Apache and 301 Redirections
wordpress_id: 142
category: English
tags: Apache, Blog, Hosting, htaccess, ISP, Linux, Mandriva, Repository, RPM, urpmi, Web

Since the creation of my personal Mandriva repository ([10 months ago](http://kevin.deldycke.com/2006/04/new-repository-for-mandriva-2006/)) the number of my RPMs did not cease to increase. Currently all RPMs and SRPMs from 2006.0 and 2007.0 take 383MiB of space.

So I decided to move the `http://kev.coolcavemen.com/static/repository` folder to `http://kevin.deldycke.free.fr/repository`, which is a 10GiB (yes, ten [gibibyte](http://en.wikipedia.org/wiki/Gibibyte), this is not a typo) free web space offered by [Free](http://free.fr), my ISP.

To do this smoothly, I've just set up a generic `301` redirection thanks to Apache. This is the only line I added to my root `.htaccess` file to enable this:

    :::apache
    Redirect permanent /static/repository http://kevin.deldycke.free.fr/repository

This move will normally be completely silent for you. So please, let me now if something bad happend while you play with my repository.

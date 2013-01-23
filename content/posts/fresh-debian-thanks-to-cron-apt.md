comments: true
date: 2011-05-24 12:18:08
layout: post
slug: fresh-debian-thanks-to-cron-apt
title: Keep a Debian fresh thanks to cron-apt
wordpress_id: 3171
category: English
tags: apt, aptitude, cron, cron-apt, Debian, Linux, sed

As I [mentioned in an old comment](http://kevin.deldycke.com/2008/12/dpkg-apt-aptitude-commands/comment-page-1/#comment-4726), I use `cron-apt` to keep my Debian servers fresh.

This post is just a quick reminder to my future self, about how I setup `cron-apt` on my machines.

First we install the package:

    :::bash
    $ aptitude install cron-apt

Then we configure it:

    :::bash
    $ sed -i 's/# MAILON="error"/MAILON="always"/g' /etc/cron-apt/config
    $ sed -i 's/# MAILTO="root"/MAILTO="user@example.com"/g' /etc/cron-apt/config

That's it !

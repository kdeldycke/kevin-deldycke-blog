comments: true
date: 2009-12-02 21:37:09
layout: post
slug: auto-saving-file-regular-intervals
title: Auto-saving a file at regular intervals
wordpress_id: 911
category: English
tags: Backup, cron, Linux, save

[![editing-cron-with-vi](http://kevin.deldycke.com/wp-content/uploads/2009/12/editing-cron-with-vi-150x150.jpg)](http://kevin.deldycke.com/wp-content/uploads/2009/12/editing-cron-with-vi.jpg) Here is a way to autosave a file at regular intervals: use `cron` !

The trick is to know that `cron` need percents to be escaped by a backslash in the command zone. For example, here is my crontab entry to create every 10 minutes a local backup of an important project file I currently work on:







    :::console
    */10 * * * * kevin cp "/home/kevin/Desktop/Projects/Very Important Project/project.file" "/home/kevin/Desktop/Projects/Very Important Project/project.file-backup-`date +\%s`"




Quick and dirty, but may saves you precious time on [unstable machines](http://twitter.com/kdeldycke/status/6158072244) ! ;)

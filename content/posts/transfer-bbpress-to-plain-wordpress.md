date: 2012-10-30 12:42:53
slug: transfer-bbpress-to-plain-wordpress
title: How-To transfer bbPress content to plain WordPress objects
category: English
tags: export, import, migration, MySQL, SQL, PHP, Python, WordPress, xml

I had two bbPress forums to archive for Cool Cavemen. The first one, which was private, was [exported as a mailing-list](http://kevin.deldycke.com/2012/10/converting-bbpress-forum-mailbox-archive/) last month.

For the second forum, which was public, I created a [Python script](https://github.com/kdeldycke/scripts/blob/master/bbpress-to-wordpress.py) to transform them into pure WordPress objects. This means transforming forums, topics and replies to pages & comments.

This script is in fact a fork of the one I created to [export Zenphoto content to WordPress](http://kevin.deldycke.com/2012/09/zenphoto-wordpress-migration/). Like the later, it reads data from MySQL then produce a WXR file.

A bbPress thread is imported as an empty page with the thread's title. All its replies are imported as comments of that page. A top-level page is then created for each forum, and all its threads are linked from that parent page.

The dependencies of that script can be installed with the following commands:

    :::bash
    $ sudo aptitude install python-pip python-lxml
    $ sudo pip install PyMySQL

My use case for this script is to be able to archive an hosted bbPress instance from a dedicated server to the free wordpress.org hosting.

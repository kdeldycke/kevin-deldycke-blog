date: 2012-09-18 12:38:05
slug: zenphoto-wordpress-migration
title: ZenPhoto to WordPress Migration
category: English
tags: Debian, migration, MySQL, SQL, Pip, Python, WordPress, xml, Zenphoto

For years I was using [ZenPhoto](http://www.zenphoto.org/) to host my photo galleries. Now [WordPress](http://wordpress.org) has made enough improvements in media management to make ZenPhoto redundant for my simple needs.

So I've just create a [Python script](https://github.com/kdeldycke/scripts/blob/master/zenphoto-to-wordpress.py) to transfer ZenPhoto content to WordPress.

It browse the MySQL database of a ZenPhoto instance and generate an XML file. The XML produced is a WXR file (WordPress eXtended RSS), which mean it can be imported into a WordPress site.

A ZenPhoto album is imported as a post with a `[gallery]` tag in it. All images of an album are imported as attachments and tied to the post it belongs to. The script currently doesn't take care of sub-albums, as I didn't had any to migrate.

The script has some dependencies on Python modules. These can easily be installed on Debian by running as `root`:

    :::bash
    $ sudo aptitude install python-pip python-lxml
    $ sudo pip install PyMySQL


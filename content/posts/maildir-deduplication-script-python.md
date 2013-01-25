comments: true
date: 2010-08-19 20:56:03
layout: post
slug: maildir-deduplication-script-python
title: Maildir deduplication script in Python
wordpress_id: 1712
category: English
tags: email, GitHub, Lotus Notes, Apple, Mac OS X, maildir, Python, Script

Some months ago I wrote a tiny Python script which scan all folders and sub-folders of a Maildir, then remove duplicate mails.

You can give the script a list of email headers to ignore while it compares mails between each others. This is particularly helpful to find duplicate mails having the exact same content but different headers/metadatas.

I created this script to clean up a Maildir folder I messed up after moving repeatedly tons of mails from a Lotus Notes database. As you can see below, the same mail imported twice contain a variable header based on the date and time the import was performed:
[![](http://kevin.deldycke.com/wp-content/uploads/2010/08/lotus-notes-x-mimetrack-mail-header-300x45.png)](http://kevin.deldycke.com/wp-content/uploads/2010/08/lotus-notes-x-mimetrack-mail-header.png)

This variable header make mails looks different from the point of view of the script. That's explain why I implemented the `HEADERS_TO_IGNORE` parameter with the default set to `X-MIMETrack`.

The [script is available on my GitHub](http://github.com/kdeldycke/scripts/blob/master/maildir-deduplicate.py) repository. It was tested on MacOS X 10.6 with python 2.6.2 but should work on other systems and versions as the code is really simple (and stupid).

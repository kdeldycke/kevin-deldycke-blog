---
date: '2010-08-19'
title: Maildir deduplication script in Python
category: English
tags: email, GitHub, Lotus Notes, Apple, macOS, maildir, Python, Mac OS X 10.6 Snow Leopard
---

Some months ago I wrote a tiny Python script which scan all folders and
sub-folders of a Maildir, then remove duplicate mails.

You can give the script a list of email headers to ignore while it compares
mails between each others. This is particularly helpful to find duplicate mails
having the exact same content but different headers/metadatas.

I created this script to clean up a Maildir folder I messed up after moving
repeatedly tons of mails from a Lotus Notes database. As you can see below, the
same mail imported twice contain a variable header based on the date and time
the import was performed:

![]({attach}lotus-notes-x-mimetrack-mail-header.png)

This variable header make mails looks different from the point of view of the
script. That's explain why I implemented the `HEADERS_TO_IGNORE` parameter with
the default set to `X-MIMETrack`.

The [script is available on GitHub
](https://github.com/kdeldycke/maildir-deduplicate). It was tested on Mac OS X
Snow Leopard with python 2.6.2 but should work on other systems and versions as
the code is really simple (and stupid).

---
date: '2012-09-04'
title: 'mail_ingestor.py : Ingest Raw Text Files and Produce a Mailbox'
category: English
tags: archive, Backup, email, import email, mailbox, Python, Web
---

I was late to the party. Me and the Internet only met in 2000, over a 36kbps phone-line modem.

It was the benefit of living in the dot-com bubble: Internet providers were created overnight and every one of them regularly offered dozens of free access hours.

Nothing is left of my first steps on the web, but an archive of mails I sent and received. I found it last month while cleaning my backups.

The archive contained all my mails in plain-text and was organized like this:

- friend-1

  - in

    - mail-1.txt

    - mail-2.txt

    - attachment-1.jpg

    - attachment-2.pdf

    - ...

  - out

    - mail-10.txt

    - mail-11.txt

    - attachment-10.jpg

    - attachment-11.pdf

    - ...

- friend-2

  - in

    - ...

  - out

    - ...

- ...

Now I want to consolidate all these mails to my Gmail account. But the plain-text files were in an inconsistent state, some with headers, some without, and others had headers translated in French...

So I wrote a quick and dirty script in Python.

The script ingest this strange structure and produce a clean and tidy mailbox file. The script is available on my [general-purpose Git repository](https://github.com/kdeldycke/scripts/) and is called [mail_ingestor.py](https://github.com/kdeldycke/scripts/blob/master/mail_ingestor.py).

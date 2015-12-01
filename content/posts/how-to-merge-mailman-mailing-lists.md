---
date: 2011-10-11 12:28:25
title: How-to merge Mailman mailing-lists
category: English
tags: archive, Linux, email, mailing list, mailman, merge, Python

Let's say I have an old inactive mailing list (which ID is `old-ml`) for which I want to merge its archives to another one (called `active-ml`).

To do so, I have to merge the two mbox files holding all mails since the creation of these mailing-lists. I first tried to use `cat` to concatenate the two mbox files be it didn't work.

Luckily, I found a [Python script to merge 2 mbox files](http://mail.python.org/pipermail/mailman-users/2008-March/060937.html) while sorting all mails by date. Here is how I uses it:

    :::bash
    $ cd /var/lib/mailman/archives/private
    $ wget http://mail.python.org/pipermail/mailman-users/attachments/20080322/80455064/attachment.txt --output-document=mbmerge.py
    $ python ./mbmerge.py ./old-ml.mbox/old-ml.mbox ./active-ml.mbox/active-ml.mbox > ./active-ml.mbox/active-ml.mbox.new

Then I switched the current mbox with the one generated above and asked mailman to regenerate the static HTML archives:

    :::bash
    $ cd /var/lib/mailman/archives/private/active-ml.mbox/
    $ mv active-ml.mbox active-ml.mbox.backup
    $ mv active-ml.mbox.new active-ml.mbox
    $ chown list:list active-ml.mbox*
    $ /usr/lib/mailman/bin/arch --wipe active-ml

Of course this will only merge mail archives. You still have to merge your old mailing lists parameters (including membership) manually.

At last, when everything is clean to you, you can safely remove your old mailing-list:

    :::bash
    $ rmlist -a old-ml
    $ /var/lib/mailman/bin/genaliases


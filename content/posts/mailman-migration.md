---
date: 2011-10-04 12:00:44
title: Mailman migration
category: English
tags: Debian, Debian Squeeze, dns, Exim, mailman, spf, Debian Lenny
---

Last week I detailed how I configured [Mailman with Exim and Nginx on a Debian Squeeze](https://kevin.deldycke.com/2011/09/setup-mailman-nginx-exim-debian-squeeze/). Here are some more notes on how I migrated my mailing lists from my old server (Lenny with Mailman 2.1.11) to the new Mailman installation (Squeeze with Mailman 2.1.13).

First, I remove the default `mailman` meta-list as I will retrieve the one from the old server:

    ```shell-session
    $ /etc/init.d/mailman stop
    $ rmlist -a mailman
    $ /var/lib/mailman/bin/genaliases
    ```

Then I copy mailing-list data from the old server to the new:

    ```shell-session
    $ rsync --progress -vrae "ssh -C" /var/lib/mailman/lists    root@new.example.com:/var/lib/mailman/
    $ rsync --progress -vrae "ssh -C" /var/lib/mailman/archives root@new.example.com:/var/lib/mailman/
    $ rsync --progress -vrae "ssh -C" /var/lib/mailman/data     root@new.example.com:/var/lib/mailman/
    ```

Back to our new server, fix some rights, check all lists are there, and run the automatic update:

    ```shell-session
    $ chown -R list:list /var/lib/mailman/
    $ /etc/init.d/mailman start
    $ list_lists
    $ /var/lib/mailman/bin/update
    ```

Now let Mailman check its databases and fix permission:

    ```shell-session
    $ check_db -a -v
    $ check_perms -f -v
    ```

At this point you may get this error in your `/var/log/exim4/mainlog`:

    ```text
    2011-09-13 10:06:09 failed to expand condition "${lookup{$local_part@$domain}lsearch{/var/lib/mailman/data/virtual-mailman}{1}{0}}" for mailman_router router: failed to open /var/lib/mailman/data/virtual-mailman for linear search: Permission denied (euid=101 egid=103)
    ```

This can be fixed with ([source](https://bugs.launchpad.net/ubuntu/+source/mailman/+bug/728879)):

    ```shell-session
    $ chgrp Debian-exim /var/lib/mailman/data/virtual-mailman
    ```

You may also encounter this error:

    ```text
    2011-09-13 10:06:09 H=mail-xxx-xxxx.google.com [209.85.000.000] F=<kevin@example.com> rejected RCPT <kev-test@lists.example.com>: Unrouteable address
    ```

In this case regenerating Mailman aliases should fix the issue:

    ```shell-session
    $ /var/lib/mailman/bin/genaliases
    ```

By the way, to test that Exim is routing mails as expected, your can use the following command:

    ```shell-session
    $ exim -bt kev-test@lists.example.com
    R: system_aliases for kev-test@lists.example.com
    R: mailman_router for kev-test@lists.example.com
    kev-test@lists.example.com
      router = mailman_router, transport = mailman_transport
    ```

Last problem I had was mails did not reached my server. Everytime I send something from Gmail to a list, I got back error mails saying this:

> Technical details of permanent failure:
> Google tried to deliver your message, but it was rejected by the recipient domain. We recommend contacting the other email provider for further information about the cause of this error. The error that the other server returned was: 550 550 relay not permitted (state 14).

I fixed this issue by updating my SPF record on the `example.com` domain from:

    ```text
    v=spf1 a mx ~all
    ```

to:

    ```text
    v=spf1 a mx ptr ~all
    ```


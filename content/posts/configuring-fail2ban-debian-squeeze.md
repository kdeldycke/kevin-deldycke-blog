---
date: 2011-06-21 12:25:16
title: Configuring Fail2Ban on Debian Squeeze
category: English
tags: Apache, Exim, fail2ban, security, Server, SSH, Web
---

This always start with a package installation:

    :::bash
    $ aptitude install fail2ban

Then I simply create a local configuration file where I'll put all my custom config:

    :::bash
    $ touch /etc/fail2ban/jail.local

Here is the content of that file:

    :::ini
    [DEFAULT]
    # Do not filter connexion from my apartment and from the server itself
    ignoreip  = 127.0.0.1 88.123.123.123 91.123.123.123
    # Ban for a week
    bantime   = 604800
    maxretry  = 3
    destemail = user@example.com
    banaction = iptables-allports
    action    = %(action_mwl)s

    [ssh]
    enabled  = true
    port     = 22
    maxretry = 2

    [ssh-ddos]
    enabled = true
    port     = 22

    [apache]
    # Apache basic auth
    enabled   = true
    maxretry  = 3
    # Ban for 1 hour
    bantime   = 3600

    [apache-noscript]
    enabled = true

    [apache-overflows]
    enabled = true

    [apache-badbots]
    enabled  = true
    filter   = apache-badbots
    port     = http,https
    action   = iptables-allports
    logpath  = /var/log/apache*/*access.log
    maxretry = 1

    [apache-nohome]
    enabled  = true
    filter   = apache-nohome
    port     = http,https
    action   = iptables-allports
    logpath  = /var/log/apache*/*access.log
    maxretry = 1

    [exim]
    enabled  = true
    filter   = exim
    port     = smtp,ssmtp
    action   = iptables-allports
    logpath  = /var/log/exim*/rejectlog
    maxretry = 1

    [exim-relay]
    enabled  = true
    filter   = exim-relay
    port     = smtp,ssmtp
    action   = iptables-allports
    logpath  = /var/log/exim*/rejectlog
    maxretry = 1

While adjusting Fail2Ban, I was surprised by how sensitive this software is. It can just refuse to start without any notice in the log or on the command line. Even if its `log_level` variable is set to `4` (= `DEBUG`) in `/etc/fail2ban/fail2ban.conf`.

In such a case, a sure way to find the culprit is to use a brute force debugging method: first set all the `enabled` variable of your `jail.local`'s sections to `false`. Then activate one section after another until Fail2Ban refuse to restart.

For me, the problem was that I forgot to add my custom `exim-relay` filter to Fail2Ban. So I fixed my issue by creating an empty file at `/etc/fail2ban/filter.d/exim-relay.conf` in which I pasted the following content:

    :::ini
    # Based on default exim.conf filter by Cyril Jaquier
    # Real life exemaple:
    # 2009-07-02 08:16:42 H=118-167-129-21.dynamic.hinet.net (91.121.198.84) [118.167.129.21] F=<titieueue@hotmail.com> rejected RCPT <s2288@mail2000.com.tw>: relay not permitted

    [Definition]

    # Option:  failregex
    # Notes.:  regex to match use of my exim mail server as a relay it does not
    #          allow.
    # Values:  TEXT
    #
    failregex = \[<HOST>\] .*(?:relay not permitted)

    # Option:  ignoreregex
    # Notes.:  regex to ignore. If this regex matches, the line is ignored.
    # Values:  TEXT
    #
    ignoreregex =

Speaking of custom filters, here is one to filter DFind scans (file located at `/etc/fail2ban/filter.d/apache-w00tw00t.conf`):

    :::ini
    # Based on https://howflow.com/tricks/block_w00tw00t_scan_hosts_with_fail2ban
    # Real life exemaple:
    # [Sat Jun 27 16:43:08 2009] [error] [client 94.23.57.77] client sent HTTP/1.1 request without hostname (see RFC2616 section 14.23): /w00tw00t.at.ISC.SANS.DFind:)

    [Definition]

    # Option:  failregex
    # Notes.:  regex to match the w00tw00t scan messages in the logfile.
    # Values:  TEXT
    failregex = ^.*\[client <HOST>\].*w00tw00t\.at\.ISC\.SANS\.DFind.*

    # Option:  ignoreregex
    # Notes.:  regex to ignore. If this regex matches, the line is ignored.
    # Values:  TEXT
    ignoreregex =

And here is the corresponding section from my `jail.local` file:

    :::ini
    [apache-w00tw00t]
    enabled  = true
    filter   = apache-w00tw00t
    action   = iptables-allports
    logpath  = /var/log/apache*/*error.log
    maxretry = 1


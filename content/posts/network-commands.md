---
date: 2011-04-11 16:25:54
title: Network commands
category: English
tags: bind, dig, dns, iwlist, Linux, lsof, netstat, Network, wifi, wireless, driftnet, images
---

## Interfaces

  * Get the list of all wireless networks reachable by the `wlan0` interface:

        :::shell-session
        $ iwlist wlan0 scanning | grep ESSID

  * Get some informations about open ports:

        :::shell-session
        $ netstat --taupen
        $ netstat --lapute

  * Watch network activity in real-time:

        :::shell-session
        $ watch -n 1 "lsof -i"

  * Reboot machine if the `192.168.0.254` host doesn't reply to ping after 15 attemps or 600 seconds:

        :::shell-session
        $ ping -c 15 -o -t 600 192.168.0.254 || shutdown -r now


## Domain names

  * Get the IP address where a domain points to:

        :::shell-session
        $ host kevin.deldycke.com

  * Get different kind of DNS records of the `example.com` domain:

        :::shell-session
        $ dig example.com CNAME
        $ dig example.com MX


## Content inspection

  * Save all images passing through `eth0`:

        :::shell-session
        $ driftnet -i eth0 -a -d ./http-pics

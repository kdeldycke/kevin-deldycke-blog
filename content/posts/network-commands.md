---
date: 2011-04-11 16:25:54
title: Network commands
category: English
tags: bind, dig, dns, iwlist, Linux, lsof, netstat, Network, wifi, wireless, driftnet, images

  * Get the list of all wireless networks reachable by the `wlan0` interface:

        :::bash
        $ iwlist wlan0 scanning | grep ESSID

  * Get the IP address where a domain points to:

        :::bash
        $ host kevin.deldycke.com

  * Get different kind of DNS records of the `example.com` domain:

        :::bash
        $ dig example.com CNAME
        $ dig example.com MX

  * Get some informations about open ports:

        :::bash
        $ netstat --taupen
        $ netstat --lapute

  * Watch network activity in real-time:

        :::bash
        $ watch -n 1 "lsof -i"

  * Save all images passing through `eth0`:

        :::bash
        $ driftnet -i eth0 -a -d ./http-pics

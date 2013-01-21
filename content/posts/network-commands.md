comments: true
date: 2011-04-11 16:25:54
layout: post
slug: network-commands
title: Network commands
wordpress_id: 2561
category: English
tags: bind, dig, dns, iwlist, Linux, lsof, netstat, Network, wifi, wireless




  * Get the list of all wireless networks reachable by the `wlan0` interface:


        :::console
        iwlist wlan0 scanning | grep ESSID







  * Get the IP address where a domain points to:


        :::console
        host kevin.deldycke.com







  * Get different kind of DNS records of the `example.com` domain:


        :::console
        dig example.com CNAME
        dig example.com MX







  * Get some informations about open ports:


        :::console
        netstat --taupen
        netstat --lapute







  * Watch network activity in real-time:


        :::console
        watch -n 1 "lsof -i"








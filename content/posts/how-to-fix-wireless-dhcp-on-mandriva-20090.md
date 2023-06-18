---
date: "2008-11-28"
title: "How-to fix wireless DHCP on Mandriva 2009.0"
category: English
tags: dhcp, Linux, Mandriva, Network, urpmi, wifi, wireless
---

In two words: `dhcp_client` sucks!

And now the long story...

Since the upgrade to Mandriva 2008.1, wifi stopped working on my laptop. I tried to install the 2008.1 on several machines. I tried to connect on different access points. I lowered security on the access point. I tried eveything. On desperation, I even tried to boot Windows to check that hardware was ok! And the only log I had was this:

    ```text
    SIOCETHTOOL: Operation not supported
    ```

After all these tests, I was convinced that the problem had something to do with the distribution itself. Maybe a firmware issue or a bad combination of packages...

Then came the 2009.0 release. I though that an upgrade will cure my malediction. Indeed. Nothing new on wireless side. My wifi was still broken. Until I came across a tip on a random forum (I don't remember which one) suggesting that `dhcp_client` could be the culprit.

So I replaced it by `dhcpcd`, and against all expectations, it worked!

![](/uploads/2008/mandriva-net-applet-wireless-dhcp.png)

And to not be annoyed by `dhcp_client` in the future, it's wise to definitely remove it:

    ```shell-session
    $ urpmi dhcp_client
    ```


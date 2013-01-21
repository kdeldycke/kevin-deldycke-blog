comments: true
date: 2011-08-09 12:15:36
layout: post
slug: entropy-debian-squeeze-server
title: Better Entropy on a Debian Squeeze server
wordpress_id: 3552
category: English
tags: Debian, entropy, haveged, Linux, random, security, squeeze

While generating a GPG key on my server, I got the following error:

    :::text
    Not enough random bytes available. Please do some other work to give the OS a chance to collect more entropy! (Need 283 more bytes)

That's a [well known issue](http://otrs.menandmice.com/otrs/public.pl?Action=PublicFAQ&ItemID=122) on headless servers. Thanks to a [comment on Hacker News](http://news.ycombinator.com/item?id=2703349), I knew there was a way to fix this thanks to software entropy generator, like the [havege deamon](http://www.issihosts.com/haveged/).

My server is running Debian Squeeze. Luckily, a [package is available](http://packages.debian.org/squeeze-backports/haveged) in the backport repository. All we have to do is to add the latter in our source list before installing `haveged`:

    :::console
    $ echo 'deb http://backports.debian.org/debian-backports squeeze-backports main' > /etc/apt/sources.list.d/squeeze-backports.list
    $ apt-get update
    $ apt-get -t squeeze-backports install haveged

Now you can get a proof that `haveged` is running by monitoring your entropy. Here is for example the Munin graph of my server, on which you can clearly see the big jump in available entropy:
[![](http://kevin.deldycke.com/wp-content/uploads/2011/07/increased-entropy-with-haveged-300x169.png)](http://kevin.deldycke.com/wp-content/uploads/2011/07/increased-entropy-with-haveged.png)

If I'm not sure about the quality of the [randomness it generate on virtual machines](http://jakob.engbloms.se/archives/1374), `haveged` is still a really practical solution for lack of entropy on a server.

comments: true
date: 2009-12-23 10:42:09
layout: post
slug: macosx-is-irritating
title: MacOS X really starts to get irritating...
wordpress_id: 932
category: English
tags: desktop, KDE, Mac OS X Leopard, Apple, Mac OS X, rant

First, [unstable machine](http://twitter.com/kdeldycke/status/6158072244).

Then, regular crashes of the Finder and Safari.

Now, weird font bugs:

![](http://kevin.deldycke.com/wp-content/uploads/2009/12/mac-osx-broken-menu-font.png)

![](http://kevin.deldycke.com/wp-content/uploads/2009/12/mac-osx-broken-shutdown-dialog.png)

This madness will never stop... :(

![](http://kevin.deldycke.com/wp-content/uploads/2009/12/mac-osx-leopard-display-bug.png)

Just found new species of bugs:

![](http://kevin.deldycke.com/wp-content/uploads/2009/12/mac-osx-black-top-menu-bug.png)

![](http://kevin.deldycke.com/wp-content/uploads/2009/12/mac-osx-black-drop-down-menu-bug.png)

My 6 months test period of Leopard is over. Time to switch back to a Linux/KDE desktop.

## Update (May 2010)

6 months later, I've:

  * updated MacOS X from Leopard to Snow Leopard,
  * upgraded Kubuntu from Karmic Koala (9.10) to Lucid Lynx (10.04),
  * changed my HDD to a SSD (a [160 Go Intel X25-M Postville](http://www.amazon.com/gp/product/B002IGT7IU/ref=as_li_ss_tl?ie=UTF8&tag=kevideld-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=B002IGT7IU)).

![](http://www.assoc-amazon.com/e/ir?t=kevideld-20&l=as2&o=1&a=B002IGT7IU)

Still, my machine crash hard. Here is the kind of kernel crashes I have on kubuntu with this machine:

![](http://kevin.deldycke.com/wp-content/uploads/2009/12/mac-book-pro-linux-kernel-crash.jpg)

I now suspect problems with the MacBook Pro's SATA controller. After all, my machine always freeze on high I/O load (disk backups, video transcoding, etc.). Wait. I remember of Apple pushing a new SATA firmware one year ago. Let me google this...

Bingo ! [This is a firmware issue](http://www.slashgear.com/macbook-pro-3-0gbps-sata-upgrade-breaking-third-party-drives-2648050/) ! I knew it ! So I just followed [these instructions](http://forums.macrumors.com/showpost.php?p=8414998&postcount=305) this afternoon to downgrade my firmware to EFI 1.6.

I can now check that it really set SATA bandwidth back to 1.5 Gbps:

    :::bash
    $ cat /var/log/dmesg | grep Gbps
    [    0.800530] ahci 0000:00:0b.0: AHCI 0001.0200 32 slots 6 ports 1.5 Gbps 0x3 impl IDE mode
    [    1.330097] ata1: SATA link up 1.5 Gbps (SStatus 113 SControl 300)
    [    1.330112] ata2: SATA link up 1.5 Gbps (SStatus 113 SControl 300)
    [    2.280096] ata1: SATA link up 1.5 Gbps (SStatus 113 SControl 300)
    [    2.290110] ata2: SATA link up 1.5 Gbps (SStatus 113 SControl 300)

But the firmware downgrade didn't solved my problems at all. It's really time to trash this MacBook Pro. [Anyone to suggest](http://twitter.com/kdeldycke/status/14657317476) a good laptop that works fine on Kubuntu ?

## Update (June 2010)

For the record, here is what my MacBook looked like at boot in the end of June 2010, two days after the end of the 1-year warranty:

![](http://kevin.deldycke.com/wp-content/uploads/2009/12/mac-book-pro-broken-boot.jpg)

At Paris' Genius Bar, I was told that my motherboard was dead, which cost 400€ to replace. And that's how I finally decided to [sell my MacBook Pro](http://twitter.com/#!/kdeldycke/status/29012034410) and get rid of all my Apple gear and proprietary software.

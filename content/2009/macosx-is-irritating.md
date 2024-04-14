---
date: '2009-12-23'
title: Mac OS X really starts to get irritating...
category: English
tags: desktop, KDE, Mac OS X 10.5 Leopard, Apple, macOS, rant
---

First, [unstable machine](https://twitter.com/kdeldycke/status/6158072244).

Then, regular crashes of the Finder and Safari.

Now, weird font bugs:

![]({attach}mac-osx-broken-menu-font.png)

![]({attach}mac-osx-broken-shutdown-dialog.png)

This madness will never stop... :(

![]({attach}mac-osx-leopard-display-bug.png)

Just found new species of bugs:

![]({attach}mac-osx-black-top-menu-bug.png)

![]({attach}mac-osx-black-drop-down-menu-bug.png)

My 6 months test period of Leopard is over. Time to switch back to a Linux/KDE
desktop.

## Update (May 2010)

6 months later, I've:

- updated Mac OS X from Leopard to Snow Leopard,
- upgraded Kubuntu from Karmic Koala (9.10) to Lucid Lynx (10.04),
- changed my HDD to a SSD (a [160 Go Intel X25-M Postville
  ](https://amzn.com/B002IGT7IU/?tag=kevideld-20)).

Still, my machine crash hard. Here is the kind of kernel crashes I have on
Kubuntu with this machine:

![]({attach}mac-book-pro-linux-kernel-crash.jpg)

I now suspect problems with the MacBook Pro's SATA controller. After all, my
machine always freeze on high I/O load (disk backups, video transcoding, etc.).
Wait. I remember of Apple pushing a new SATA firmware one year ago. Let me
google this...

Bingo! [This is a firmware issue
](https://www.slashgear.com/macbook-pro-3-0gbps-sata-upgrade-breaking-third-party-drives-2648050/)!
I knew it! So I just followed [these instructions
](https://forums.macrumors.com/showpost.php?p=8414998&postcount=305) this
afternoon to downgrade my firmware to EFI 1.6.

I can now check that it really set SATA bandwidth back to 1.5 Gbps:

```shell-session
$ cat /var/log/dmesg | grep Gbps
[    0.800530] ahci 0000:00:0b.0: AHCI 0001.0200 32 slots 6 ports 1.5 Gbps 0x3 impl IDE mode
[    1.330097] ata1: SATA link up 1.5 Gbps (SStatus 113 SControl 300)
[    1.330112] ata2: SATA link up 1.5 Gbps (SStatus 113 SControl 300)
[    2.280096] ata1: SATA link up 1.5 Gbps (SStatus 113 SControl 300)
[    2.290110] ata2: SATA link up 1.5 Gbps (SStatus 113 SControl 300)
```

But the firmware downgrade didn't solved my problems at all. It's really time
to trash this MacBook Pro. [Anyone to suggest
](https://twitter.com/kdeldycke/status/14657317476) a good laptop that works
fine on Kubuntu?

## Update (June 2010)

For the record, here is what my MacBook looked like at boot in the end of June
2010, two days after the end of the 1-year warranty:

![]({attach}mac-book-pro-broken-boot.jpg)

At Paris' Genius Bar, I was told that my motherboard was dead, which cost 400€
to replace. And that's how I finally decided to [sell my MacBook Pro
](https://twitter.com/#!/kdeldycke/status/29012034410) and get rid of all my
Apple gear and proprietary software.

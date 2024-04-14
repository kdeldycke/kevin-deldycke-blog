---
date: '2011-02-21'
title: Kubuntu 10.10 on Sony Vaio VPC-S12C5E
category: English
tags: grub, Kubuntu, Ubuntu, laptop, Linux, notebook, sony, touchpad, vaio
---

Here are some (old) notes regarding the installation of Kubuntu on my [Sony Vaio VPC](https://amzn.com/B004J1G57I/?tag=kevideld-20)-S12C5E.

First I have to tell you that everything is working fine and out of the box with Kubuntu 10.10. This include: Bluetooth, HDMI out (tested with a Full-HD monitor), Sound out, VGA, USB, CD Burning, WiFi, Networking, Keyboard backlight & SD Card reader.

The only annoying thing in 10.10 is the non-responding touchpad. But a [fix can be found on Ubuntu forums](https://ubuntuforums.org/showpost.php?p=9806445&postcount=9):

1. Edit `/etc/default/grub` to include `GRUB_CMDLINE_LINUX="i8042.nopnp"`

1. Run `sudo update-grub`

1. Reboot

Now about the laptop itself: construction quality is below my previous [MacBook](https://amzn.com/B002QQ8H8I/?tag=kevideld-20) (cheap plastic instead of aluminum) and battery autonomy is not impressive. A bios update seems to address the latter. Haven't done it yet as it requires to re-install Windows (*sigh*). But overall that's a good lightweight machine to get things done, especially with its 8 Gb of RAM, 4 cores and a SSD! :)

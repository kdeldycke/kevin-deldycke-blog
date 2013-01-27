comments: true
date: 2011-02-21 12:34:02
layout: post
slug: kubuntu-10-10-sony-vaio-vpcs12c5e
title: Kubuntu 10.10 on Sony Vaio VPC-S12C5E
wordpress_id: 2871
category: English
tags: grub, Kubuntu, Ubuntu, laptop, Linux, notebook, sony, touchpad, vaio

Here are some (old) notes regarding the installation of Kubuntu on my [Sony Vaio VPC](http://www.amazon.com/gp/product/B004J1G57I/ref=as_li_tf_tl?ie=UTF8&tag=kevideld-20&linkCode=as2&camp=217145&creative=399373&creativeASIN=B004J1G57I)-S12C5E.

![](http://www.assoc-amazon.com/e/ir?t=kevideld-20&l=as2&o=1&a=B004J1G57I&camp=217145&creative=399373)

First I have to tell you that everything is working fine and out of the box with Kubuntu 10.10. This include: Bluetooth, HDMI out (tested with a Full-HD monitor), Sound out, VGA, USB, CD Burning, WiFi, Networking, Keyboard backlight & SD Card reader.

The only annoying thing in 10.10 is the non-responding touchpad. But a [fix can be found on Ubuntu forums](http://ubuntuforums.org/showpost.php?p=9806445&postcount=9):

  1. Edit `/etc/default/grub` to include `GRUB_CMDLINE_LINUX="i8042.nopnp"`

  2. Run `sudo update-grub`

  3. Reboot

Now about the laptop itself: construction quality is below my previous [MacBook](http://www.amazon.com/gp/product/B002QQ8H8I/ref=as_li_tf_tl?ie=UTF8&tag=kevideld-20&linkCode=as2&camp=217145&creative=399373&creativeASIN=B002QQ8H8I) (cheap plastic instead of aluminum) and battery autonomy is not impressive. A bios update seems to address the latter. Haven't done it yet as it requires to re-install Windows (*sigh*). But overall that's a good lightweight machine to get things done, especially with its 8 Gb of RAM, 4 cores and a SSD ! :)

![](http://www.assoc-amazon.com/e/ir?t=kevideld-20&l=as2&o=1&a=B002QQ8H8I&camp=217145&creative=399373)

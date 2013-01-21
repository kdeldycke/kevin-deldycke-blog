comments: true
date: 2008-02-02 19:36:47
layout: post
slug: how-to-fix-samsung-q35-random-freeze
title: How to fix Samsung Q35 random freeze
wordpress_id: 216
category: English
tags: firmware, Hardware, optical drive

If like me you have a [Samsung Q35](http://kevin.deldycke.com/2006/10/samsung-q35-xic-5500-tiny-review-of-a-strong-compact-laptop/), do not forget to [update your optical drive firmware](https://bugs.launchpad.net/linux/+bug/75295/comments/97).

I've upgraded my `TSSTcorp CD/DVDW TS-L632D` drive from the `SC02` to `SC04` firmware revision and my laptop is stable now ! :)

By the way, to get the model name and revision of your optical drive under linux, use:

    :::console
    cdrdao scanbus


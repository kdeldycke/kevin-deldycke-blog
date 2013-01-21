comments: true
date: 2006-09-03 21:04:46
layout: post
slug: e107-to-wordpress-importer-v02-with-bbcode-support
title: e107 to Wordpress Importer: v0.2 with bbcode support
wordpress_id: 45
tags: Blog, CMS, e107, PHP, Web, WordPress

Here is the [second alpha release of my e107 to Wordpress import plug-in](http://kevin.deldycke.com/static/scripts/wordpress-e107-importer-0.2.zip). This release add [bbcode](http://en.wikipedia.org/wiki/BBCode) support to news content, based on original code from the e107 project. This mean that all your e107 news that use bbcode will be automattically transformed in pure html code to fit in Wordpress.

The tests I've done on my local machine showed me that there is still some problems with embedded URLs that use `[link]` bbcode and with image rendering (which are not rendered with `img` html tag). I hope to find some time soon to understand and fix this bad behaviour.

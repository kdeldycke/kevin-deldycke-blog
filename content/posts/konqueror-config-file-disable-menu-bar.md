comments: true
date: 2006-08-31 00:49:48
layout: post
slug: konqueror-config-file-disable-menu-bar
title: Konqueror config file: disable menu bar
wordpress_id: 44
category: English
tags: KDE, kmail, konqueror, Linux

To disable the menu bar in [konqueror](http://www.konqueror.org), you have a specific action in menus. If you want to do this by hand, just add the following directive in your `~/.kde/share/config/konquerorrc` file:

    
    :::text
    [KonqMainWindow]
    MenuBar=Disabled
    



This tip is interresting because you can also apply it for any KDE application that doesn't support this feature.

For exemple, in [kmail](http://kmail.kde.org), you can add the "`MenuBar=Disabled`" statement in "`[Main Window]`" section: this will have the same effect as in konqueror.

comments: true
date: 2006-11-15 00:57:50
layout: post
slug: cvs-commands
title: CVS commands
wordpress_id: 74
category: English
tags: CLI, CVS, KDE, Linux

  * Download to your machine the `kdetoys` module from the KDE CVS:

        :::bash
        $ cvs -d:pserver:anonymous@anoncvs.kde.org:/home/kde checkout kdetoys

  * Get the 22/09/2005 version of the kdetoys module source code:

        :::bash
        $ cvs -d:pserver:anonymous@anoncvs.kde.org:/home/kde co -D '22 Sep 2005' kdetoys

  * `-D` option used below is sticky. Use the following command when you no longer want to keep the dated version:

        :::bash
        $ cvs up -A kdetoys


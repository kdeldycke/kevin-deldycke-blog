comments: true
date: 2006-05-19 23:26:55
layout: post
slug: how-to-install-suns-java-for-firefox-on-your-mandriva-2006
title: How-to Install Sun's Java for Firefox on your Mandriva 2006
wordpress_id: 23
category: English
tags: firefox, Java, Linux, Mandriva, mozilla, RPM, Web

One week ago I succeed to install the Sun's Java Runtime Environment (JRE) on my Mandriva 2006. I avoid to use proprietary softwares as long as I can. Unfortunately I needed it to fill my annual tax form online...

So, here is how I achieve this:

  1. [Download the last JRE](http://jdl.sun.com/webapps/download/AutoDL?BundleId=10335) (v1.5.0-06 at that time) from [Sun official website](http://java.com/download).

  2. As root, lauch:

    :::console
    sh ./jre-1_5_0_06-linux-i586-rpm.bin

(name of the file can change depending of the version number).

  3. Accept the licence (tip: scroll down until the end of the text).

  4. Back to the console, run:

    :::console
    urpmi ./jre-1_5_0_06-linux-i586.rpm

  5. Go to mozilla system-wide plugin directory:

    :::console
    cd /usr/lib/mozilla/plugins

  6. Create a symlink to the java plugin file:

    :::console
    ln -s /usr/java/jre1.5.0_06/plugin/i386/ns7/libjavaplugin_oji.so

  7. Finished !

To check that java is well installed, type `about:plugins` in your Firefox browser URL field and check that java plug-in appear on the list.

Happy tax form filling !
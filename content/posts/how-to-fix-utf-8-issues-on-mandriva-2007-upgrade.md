date: 2006-12-11 00:37:35
title: How-To fix UTF-8 Issues on Mandriva 2007 Upgrade
category: English
tags: Linux, Mandriva

![bad-file-character-encoding-utf-81](/static/uploads/2006/bad-file-character-encoding-utf-81.png)

If you updated your Mandriva from 2006 to 2007 and you've done that manually, some of your files in your home directory may look like the one on the screenshot. This is due to the adoption of [UTF-8](http://en.wikipedia.org/wiki/UTF-8) as the default character encoding for file systems in Mandriva. Normally the conversion is done automatically at install, so if you've upgrade your Mandriva manually...

Well, to fix this, it's quite easy and explained on the following Mandriva wiki page: [UTF8 issue when reinstalling and keeping a previous /home that was not in UTF8](http://qa.mandriva.com/twiki/bin/view/Main/MandrivaLinux2007Errata#UTF8_issue_when_reinstalling_and). The `convert-filenames-to-utf8.pl` script will do everything for you !

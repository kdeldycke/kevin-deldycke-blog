---
date: 2013-08-08 12:00
title: Phorum 3.x to WordPress migration script
tags: Python, Linux, Phorum, WordPress, migration, script, GitHub, Cool Cavemen, Funky Storm, Debian, aptitude, pip, lxml, bbcode, PyMySQL, MySQL, PHP
---

Before <a href="http://coolcavemen.com">Cool Cavemen</a>, there was <a href="http://funky-storm.com/">Funky Storm</a>. The band is long gone but I still keep an online presence as a sort of web memorial. Recently I added there an old copy of <a href="http://funky-storm.com/forum/">the forum</a>.

The original forum was powered by a <a href="http://www.phorum.org">Phorum</a> 3.x instance. The current incarnation of the website runs on WordPress. So I produced some months ago a quick & dirty Python <a href="https://github.com/kdeldycke/scripts/blob/master/phorum-to-wordpress.py">script to migrate Phorum content to WordPress</a>.

The script browse Phorum's MySQL database and generate an XML file. The XML produced respect the WXR dialect (WordPress eXtended RSS), which means the file can be directly imported to a plain WordPress site.

A Phorum thread produces an empty page with the thread's title only. All thread's replies are then added as comments of that page. A top-level page is finally created, and all its threads are linked from that parent page.

The script requires the following python modules:

  * `lxml`
  * `PyMySQL`
  * `bbcode`

They can easely be installed on Debian with the following commands:

    :::bash
    $ aptitude install python-pip python-lxml
    $ pip install PyMySQL bbcode

The script is <a href="https://github.com/kdeldycke/scripts/blob/master/phorum-to-wordpress.py">available on GitHub</a> so feel free to send pull request! :)

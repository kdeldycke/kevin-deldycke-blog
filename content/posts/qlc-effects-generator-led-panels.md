comments: true
date: 2010-08-10 21:42:14
layout: post
slug: qlc-effects-generator-led-panels
title: QLC effects generator for LED panels
wordpress_id: 1562
category: English
tags: Canon EOS 7D, Cool Cavemen, dmx, light, lighting, Linux, Python, QLC, Qt, Script, xml

Here is another script I wrote some months ago. It's called [`qlc-effects-generator.py`](http://github.com/kdeldycke/scripts/blob/master/qlc-effects-generator.py). It's a quick and dirty hack that generate chasers, groups and scenes for [QLC (a QT-based DMX lighting software)](http://sourceforge.net/projects/qlc/). It just produce XML statements you copy'n'paste in your `.qxw` QLC workspace file.

I used it to create some effects for my 4 el-cheapo [Mac-Mah LED wider panels](http://fr.audiofanzine.com/projecteur-traditionnel-divers/mac-mah/WIDER-PANEL-RGB-648-LEDS-DMX/). This script helped me generate column and row presets of my 4x8 pixels LED matrix for some basic colors:
[![](http://kevin.deldycke.com/wp-content/uploads/2010/06/qlc-wider-panel-presets-300x187.png)](http://kevin.deldycke.com/wp-content/uploads/2010/06/qlc-wider-panel-presets.png)

Here are some photos of my preliminary tests at home:

[![](http://kevin.deldycke.com/wp-content/uploads/2010/08/4-mac-mah-wider-led-panel-fushia-150x150.jpg)](http://kevin.deldycke.com/wp-content/uploads/2010/08/4-mac-mah-wider-led-panel-fushia.jpg)

[![](http://kevin.deldycke.com/wp-content/uploads/2010/08/4-mac-mah-wider-led-panel-blue-150x150.jpg)](http://kevin.deldycke.com/wp-content/uploads/2010/08/4-mac-mah-wider-led-panel-blue.jpg)

[![](http://kevin.deldycke.com/wp-content/uploads/2010/08/4-mac-mah-wider-led-panel-red-150x150.jpg)](http://kevin.deldycke.com/wp-content/uploads/2010/08/4-mac-mah-wider-led-panel-red.jpg)

[![](http://kevin.deldycke.com/wp-content/uploads/2010/08/4-mac-mah-wider-led-panel-white-150x150.jpg)](http://kevin.deldycke.com/wp-content/uploads/2010/08/4-mac-mah-wider-led-panel-white.jpg)

And finally photos of the panels on stage ([taken by Toma Heroow](http://www.heroow.fr/2009/11/18/cool-cavemen/) during [Cool Cavemen's concert in last november](http://coolcavemen.com/2009/mametzik-mad-fest-chez-march/)):

[![](http://kevin.deldycke.com/wp-content/uploads/2010/08/img_0516-scaled-150x150.jpg)](http://kevin.deldycke.com/wp-content/uploads/2010/08/img_0516-scaled.jpg)

[![](http://kevin.deldycke.com/wp-content/uploads/2010/08/img_0583-scaled-150x150.jpg)](http://kevin.deldycke.com/wp-content/uploads/2010/08/img_0583-scaled.jpg)

[![](http://kevin.deldycke.com/wp-content/uploads/2010/08/img_0519-scaled-150x150.jpg)](http://kevin.deldycke.com/wp-content/uploads/2010/08/img_0519-scaled.jpg)

As usual, use and hack this script at you own risks, and feel free to send me bug reports and contributions ! :)

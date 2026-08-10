---
date: '2010-08-10'
title: QLC effects generator for LED panels
category: English
tags: Canon EOS 7D, Cool Cavemen, DMX, Stage lighting, Linux, Python, QLC, Qt, XML
---

Here is another script I wrote some months ago. It's called
[`qlc-effects-generator.py`](https://github.com/kdeldycke/scripts/blob/master/qlc-effects-generator.py).
It's a quick and dirty hack that generate chasers, groups and scenes for
[QLC (a QT-based DMX lighting software)](https://sourceforge.net/projects/qlc/).
It just produce XML statements you copy'n'paste in your `.qxw` QLC workspace
file.

I used it to create some effects for my 4 el-cheapo
[Mac-Mah LED wider panels](https://fr.audiofanzine.com/projecteur-traditionnel-divers/mac-mah/WIDER-PANEL-RGB-648-LEDS-DMX/).
This script helped me generate column and row presets of my 4x8 pixels LED
matrix for some basic colors:

![Q Light Controller workspace with four Wider Panels patched in the fixture manager, a long list of generated per-column colour functions on the right, and a console of 22 DMX faders below](qlc-wider-panel-presets.png)

Here are some photos of my preliminary tests at home:

![Four LED panels on microphone stands in a tiled hallway at home, all washing the room magenta](4-mac-mah-wider-led-panel-fushia.jpg)

![The same four panels running deep blue, the individual LEDs visible as a fine grid](4-mac-mah-wider-led-panel-blue.jpg)

![The same four panels in saturated red, spilling across the floor tiles](4-mac-mah-wider-led-panel-red.jpg)

![The same four panels at full white, showing the cold cast of the raw LEDs](4-mac-mah-wider-led-panel-white.jpg)

And finally photos of the panels on stage (
[taken by Toma Heroow](https://web.archive.org/web/20100605092334/https://www.heroow.fr/2009/11/18/cool-cavemen/)
during
[Cool Cavemen's concert in last november](https://coolcavemen.com/2009/mametzik-mad-fest-chez-march/)):

![The band playing under a marquee, two of the LED panels standing on end behind the drum kit as vertical red bars against blue wash](img_0516-scaled.jpg)

![Bass player and saxophonist lit from below in blue and cyan, shot from the front of the stage](img_0583-scaled.jpg)

![Guitarist and singer in near silhouette against a deep red stage, one LED panel glowing as a bright column between them](img_0519-scaled.jpg)

As usual, use and hack this script at you own risks, and feel free to send me
bug reports and contributions! :)

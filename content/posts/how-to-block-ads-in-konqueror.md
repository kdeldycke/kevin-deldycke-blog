date: 2007-04-17 19:07:57
slug: how-to-block-ads-in-konqueror
title: How-to Block Ads in Konqueror
category: English
tags: ad, KDE, konqueror, Linux

Starting from version 3.5, [Konqueror](http://www.konqueror.org) feature an ad blocker mechanism based on regular expressions. Here is a little how-to to help you install an efficient filter set.

![](/static/uploads/2007/04/konqueror-ad-block-filter1.png)

  1. Dowload the latest [Filterset.G](http://www.pierceive.com) regexp set. The file which contain all rules is located at [http://www.pierceive.com/filtersetg/](http://www.pierceive.com/filtersetg/) under the name `YYYY-MM-DD.txt`.

  2. Go to `Settings` > `Configure Konqueror...` menu.

  3. Then go to `AdBlock Filters` panel (the one on the screenshot).

  4. Check both `Enable filters` and `Hide filtered images` options.

  5. Use the `Import...` button to load the "Filterset.G" file you previoulsy downloaded

  6. Enjoy ad-free web sites !

By the way, I hope to see the [feature suggested by Andreas Frische](http://bugs.kde.org/show_bug.cgi?id=143495) to get some attention by the Konqueror community: it would be nice to have an integrated auto-updater of filter set in Konqueror (and make this how-to deprecated).

comments: true
date: 2010-09-16 21:24:45
layout: post
slug: how-to-extract-data-trapped-iphone
title: How-to extract data trapped into an iPhone
wordpress_id: 1913
category: English
tags: Android, Apple, Backup, csv, iphone, ITunes, OSX, Smartphones, sqlite

After 2 years using an [iPhone 3G](http://www.amazon.com/gp/product/B001AXA056/ref=as_li_tf_tl?ie=UTF8&tag=kevideld-20&linkCode=as2&camp=217145&creative=399373&creativeASIN=B001AXA056), it's time for me to [switch to the Android world](http://twitter.com/kdeldycke/status/24219289221). [My Apple era is over](http://twitter.com/kdeldycke/status/22007247873), I need a plateform that is more linux and open-source friendly.![](http://www.assoc-amazon.com/e/ir?t=kevideld-20&l=as2&o=1&a=B001AXA056&camp=217145&creative=399373)

Before erasing and [selling my iPhone](http://twitter.com/kdeldycke/status/24687160120), I want to backup and extract all the data I produced with it and that is still trapped inside. This mean photos, SMSs, voice messages, safari bookmarks, etc...

There is a nice OSX app simply called [iPhone Backup Extractor](http://supercrazyawesome.com) which let you get these data. Instead of getting data directly from the iPhone, it reads its backups made by iTunes.

So first thing you have to do is to backup your phone using iTunes:
[![](http://kevin.deldycke.com/wp-content/uploads/2010/09/iphone-itunes-sync-300x213.png)](http://kevin.deldycke.com/wp-content/uploads/2010/09/iphone-itunes-sync.png)

Then you can download and run the iPhone Backup Extractor app:
[![](http://kevin.deldycke.com/wp-content/uploads/2010/09/iphone-backup-extrator-300x220.png)](http://kevin.deldycke.com/wp-content/uploads/2010/09/iphone-backup-extrator.png)

Here you just have to click the _Read Backups_ button to get a list of all backups available on your machine. Then choose your latest backup:
[![](http://kevin.deldycke.com/wp-content/uploads/2010/09/list-of-iphone-backups-300x224.png)](http://kevin.deldycke.com/wp-content/uploads/2010/09/list-of-iphone-backups.png)

You'll get a list of all installed applications on your iPhone. As we are interested in "core" iPhone apps (SMSs, photos and so on), we'll choose the "iOS Files" item, then choose a place where to extract:
[![](http://kevin.deldycke.com/wp-content/uploads/2010/09/iphone-backup-content-300x300.png)](http://kevin.deldycke.com/wp-content/uploads/2010/09/iphone-backup-content.png)
[![](http://kevin.deldycke.com/wp-content/uploads/2010/09/iphone-backup-extraction-destination-300x213.png)](http://kevin.deldycke.com/wp-content/uploads/2010/09/iphone-backup-extraction-destination.png)

Then the extraction itself will take place:
[![](http://kevin.deldycke.com/wp-content/uploads/2010/09/iphone-backup-extraction-300x78.png)](http://kevin.deldycke.com/wp-content/uploads/2010/09/iphone-backup-extraction.png)

You've just finished the essential part of the process. You now have a nice folder structure containing all the important informations that was trapped in your phone:
[![](http://kevin.deldycke.com/wp-content/uploads/2010/09/iphone-backup-extraction-content-300x182.png)](http://kevin.deldycke.com/wp-content/uploads/2010/09/iphone-backup-extraction-content.png)

Let's browse the file structure that was just created. You can see photos are available as is, in the `/iOS Files/Media/DCIM/XXXAPPLE/`:
[![](http://kevin.deldycke.com/wp-content/uploads/2010/09/iphone-photo-location-300x111.png)](http://kevin.deldycke.com/wp-content/uploads/2010/09/iphone-photo-location.png)

Most of other datas are located in the `/iOS Files/Library/` folder. For example here are voice messages:
[![](http://kevin.deldycke.com/wp-content/uploads/2010/09/iphone-voicemessages-location-300x127.png)](http://kevin.deldycke.com/wp-content/uploads/2010/09/iphone-voicemessages-location.png)

Again, `.amr` files here are playable as-is, like [VLC](http://www.videolan.org/vlc/) or [mplayer](http://www.mplayerhq.hu).

Most, if not all, other kind of data and metadata are stored in SQLite databases (`.db` files). The best GUI I found to manipulate with these files under Mac OSX is [SQLite Database Browser](http://sourceforge.net/projects/sqlitebrowser/). See how I can easily extract to a CSV file all metadatas associated with my voice messages:
[![](http://kevin.deldycke.com/wp-content/uploads/2010/09/sqlite-database-browser-opening-300x199.png)](http://kevin.deldycke.com/wp-content/uploads/2010/09/sqlite-database-browser-opening.png)
[![](http://kevin.deldycke.com/wp-content/uploads/2010/09/iphone-voicemail-database-tables-300x202.png)](http://kevin.deldycke.com/wp-content/uploads/2010/09/iphone-voicemail-database-tables.png)
[![](http://kevin.deldycke.com/wp-content/uploads/2010/09/iphone-voicemail-table-content-300x202.png)](http://kevin.deldycke.com/wp-content/uploads/2010/09/iphone-voicemail-table-content.png)
[![](http://kevin.deldycke.com/wp-content/uploads/2010/09/sqlite-csv-table-export-300x129.png)](http://kevin.deldycke.com/wp-content/uploads/2010/09/sqlite-csv-table-export.png)

Finally, just in case you want to extract iPhones data from another backup than the default backup, like from a backup of the backup (isn't that clear ?), making a symlink is enough to trick iPhone Backup Extractor:

    :::console
    sh-3.2# pwd
    /Users/kevin/Library/Application Support/MobileSync
    sh-3.2# mv ./Backup ./Backup-copy
    sh-3.2# ln -s "/Volumes/Untitled 1/laptop-kev-osx/mirror/Users/kevin/Library/Application Support/MobileSync/Backup" .
    sh-3.2# ls -lah
    total 8
    drwxr-xr-x   4 kevin  staff   136B Sep 16 21:56 .
    drwx------+ 11 kevin  staff   374B Sep 15 19:29 ..
    lrwxr-xr-x   1 root   staff    99B Sep 16 21:56 Backup -> /Volumes/Untitled 1/laptop-kev-osx/mirror/Users/kevin/Library/Application Support/MobileSync/Backup
    drwxr-xr-x   4 kevin  staff   136B Aug 30 13:20 Backup-copy
    sh-3.2#

That's how I was able to extract my iPhone data from an old backup, and get back most of the [data I lost after my last iOS update](http://twitter.com/kdeldycke/status/22516008513):
[![](http://kevin.deldycke.com/wp-content/uploads/2010/09/iphone-backup-extractor-from-old-backup-300x298.png)](http://kevin.deldycke.com/wp-content/uploads/2010/09/iphone-backup-extractor-from-old-backup.png)

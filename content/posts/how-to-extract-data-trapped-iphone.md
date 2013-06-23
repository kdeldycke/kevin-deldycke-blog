date: 2010-09-16 21:24:45
title: How-to extract data trapped into an iPhone
category: English
tags: Android, Apple, Backup, CSV, iPhone, iTunes, Apple, Mac OS X, Smartphones, SQLite, SQL, VLC

After 2 years using an [iPhone 3G](http://www.amazon.com/gp/product/B001AXA056/ref=as_li_tf_tl?ie=UTF8&tag=kevideld-20&linkCode=as2&camp=217145&creative=399373&creativeASIN=B001AXA056), it's time for me to [switch to the Android world](http://twitter.com/kdeldycke/status/24219289221). [My Apple era is over](http://twitter.com/kdeldycke/status/22007247873), I need a plateform that is more linux and open-source friendly.



Before erasing and [selling my iPhone](http://twitter.com/kdeldycke/status/24687160120), I want to backup and extract all the data I produced with it and that is still trapped inside. This mean photos, SMSs, voice messages, safari bookmarks, etc...

There is a nice OSX app simply called [iPhone Backup Extractor](http://supercrazyawesome.com) which let you get these data. Instead of getting data directly from the iPhone, it reads its backups made by iTunes.

So first thing you have to do is to backup your phone using iTunes:

![](/static/uploads/2010/iphone-itunes-sync.png)

Then you can download and run the iPhone Backup Extractor app:

![](/static/uploads/2010/iphone-backup-extrator.png)

Here you just have to click the _Read Backups_ button to get a list of all backups available on your machine. Then choose your latest backup:

![](/static/uploads/2010/list-of-iphone-backups.png)

You'll get a list of all installed applications on your iPhone. As we are interested in "core" iPhone apps (SMSs, photos and so on), we'll choose the "iOS Files" item, then choose a place where to extract:

![](/static/uploads/2010/iphone-backup-content.png)

![](/static/uploads/2010/iphone-backup-extraction-destination.png)

Then the extraction itself will take place:

![](/static/uploads/2010/iphone-backup-extraction.png)

You've just finished the essential part of the process. You now have a nice folder structure containing all the important informations that was trapped in your phone:

![](/static/uploads/2010/iphone-backup-extraction-content.png)

Let's browse the file structure that was just created. You can see photos are available as is, in the `/iOS Files/Media/DCIM/XXXAPPLE/`:

![](/static/uploads/2010/iphone-photo-location.png)

Most of other datas are located in the `/iOS Files/Library/` folder. For example here are voice messages:

![](/static/uploads/2010/iphone-voicemessages-location.png)

Again, `.amr` files here are playable as-is, like [VLC](http://www.videolan.org/vlc/) or [mplayer](http://www.mplayerhq.hu).

Most, if not all, other kind of data and metadata are stored in SQLite databases (`.db` files). The best GUI I found to manipulate with these files under Mac OSX is [SQLite Database Browser](http://sourceforge.net/projects/sqlitebrowser/). See how I can easily extract to a CSV file all metadatas associated with my voice messages:

![](/static/uploads/2010/sqlite-database-browser-opening.png)

![](/static/uploads/2010/iphone-voicemail-database-tables.png)

![](/static/uploads/2010/iphone-voicemail-table-content.png)

![](/static/uploads/2010/sqlite-csv-table-export.png)

Finally, just in case you want to extract iPhones data from another backup than the default backup, like from a backup of the backup (isn't that clear ?), making a symlink is enough to trick iPhone Backup Extractor:

    :::sh
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

![](/static/uploads/2010/iphone-backup-extractor-from-old-backup.png)


---
date: '2010-06-25'
title: How-to export/backup Lotus Notes mails
category: English
tags: Backup, Databases, email, export, Lotus Notes, Windows
---

You are using Lotus Notes as your mail platform. Unfortunately your mailbox has a quota you've already reached and you need space. A solution consist in exporting regularly your mails on your local machine to free up your inbox. Here is a little article documenting the export procedure using the fat desktop client.

If screenshots were taken with a french version, instructions given here are for the english one. This will give you enough clues to perform the export whatever the localisation is. The Lotus Notes version I used was the 7.0.2 release.

So first, let's start Notes and open your mailbox. You should be on a screen similar to this one:

![French Lotus Notes inbox with every sender and subject blurred out, the quota gauge in the lower left reading 83% of 90 MB](lotus-notes-mail-main-screen.png)

Then, go to the `File` › `Database` › `New Copy` menu:

![File menu drilled into the database submenu with the new-copy entry highlighted](lotus-notes-database-export-menu.png)

And you'll get an export screen that'll let you choose where to create a local copy of your database:

![Database copy dialog set to the local server, titled Kevin's july 2010 archives and writing out to kevin-mails-2010-07.nsf, copying both design and documents](export-screen.png)

This will generate a `.nsf` file containing all your current mail.

Now that you have a backup, you are free to delete all your mails in Lotus Notes. By following this procedure regularly, you can create yearly or monthly archives of you mails without reaching the mailbox quota! For example, this is how my local archive folder looks like:

![Explorer listing of the resulting archives, one .nsf file per month from December 2009 through June 2010](lotus-notes-exported-mail-archives.png)

---
date: 2012-05-15 12:24:12
title: How-To Backup Gmail with OfflineImap
category: English
tags: Backup, email, Gmail, IMAP, Linux, maildir, Python, SSL

Gmail's content can be retrieved via IMAP, and we'll use this way to backup all our mails thanks to [OfflineImap](http://offlineimap.org), a generic IMAP synchronization utility.

Let's start by creating a dedicated configuration file in your home directory. Its content is quite straight-forward, as you can see in my `/home/kevin/.offlineimaprc`, which backup two Gmail accounts:

    :::ini
    [general]
    accounts = gmail_account1, gmail_account2
    maxsyncaccounts = 3
    ui = Noninteractive.Basic

    [Account gmail_account1]
    localrepository = gmail_account1_local
    remoterepository = gmail_account1_remote

    [Repository gmail_account1_local]
    type = Maildir
    localfolders = ~/gmail-backup-account1

    [Repository gmail_account1_remote]
    type = IMAP
    remotehost = imap.gmail.com
    remoteport = 993
    remoteuser = account1@gmail.com
    remotepass = XXXXXXXX
    ssl = yes
    maxconnections = 1
    realdelete = no
    folderfilter = lambda foldername: foldername not in ['[Gmail]/%s' % f for f in ['All Mail', 'Trash', 'Spam', 'Starred', 'Important']]

    [Account gmail_account2]
    localrepository = gmail_account2_local
    remoterepository = gmail_account2_remote

    [Repository gmail_account2_local]
    type = Maildir
    localfolders = ~/gmail-backup-account2

    [Repository gmail_account2_remote]
    type = IMAP
    remotehost = imap.gmail.com
    remoteport = 993
    remoteuser = account2@gmail.com
    remotepass = XXXXXXXX
    ssl = yes
    maxconnections = 1
    realdelete = no
    folderfilter = lambda foldername: foldername not in ['[Gmail]/%s' % f for f in ['All Mail', 'Trash', 'Spam', 'Starred', 'Important']]

Notice how we use a Python lambda expressions to [filter out](http://readthedocs.org/docs/offlineimap/en/latest/nametrans.html#folderfilter) some Gmail's virtual folders.

Then all you have to do is to launch the `offlineimap` command-line itself with the right user, for example in a `cron` job:

    :::text
    00 20 * * * kevin offlineimap

A final warning: OfflineImap is fully bi-directional. This mean local deletion propagates to the remote server. This is can be quite dangerous so be careful not touching your local folders. If for any reason you'd like to reset your backups, stop OfflineImap processes first, then remove its cache folder (`~/.offlineimap/`) before removing the local folders themselves  (`~/gmail-backup-account*`).

Also, intensively playing with OfflineImap to adjust its configuration may trigger the infamous Gmail's "Temporary Error 500". In this case don't panic: it seems to be a common Gmail's auto-immune response against suspect activity. It happened to me and in the end my account and mails were safe: I just had to wait a few hours to let it resume normal operations.

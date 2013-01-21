comments: true
date: 2012-08-07 12:26:27
layout: post
slug: gmail-backup-mbsync
title: Keep a Local Backup of Gmail thanks to mbsync
wordpress_id: 5063
category: English
tags: Backup, gmail, Google, IMAP, isync, Linux, mail, mbsync

I used to keep a [local backup of my Gmail mails with OfflineImap](http://kevin.deldycke.com/2012/05/backup-gmail-offlineimap/). But I never felt comfortable with this solution because of OfflineImap being fully bidirectional. Which means my mails in the cloud are not protected from me messing with their local versions.

In the mean time I found out about [mbsync](http://isync.sourceforge.net/mbsync.html) (from the [isync project](https://sourceforge.net/projects/isync/)). It particularly features fine-grained options to let you defined which source is authoritative, thus restricting the synchronization to one direction.

Let's install mbsync and its dependencies !



    :::console
    $ sudo aptitude install isync ca-certificates




Just in case, don't forget to [enable IMAP access to you Gmail account](http://support.google.com/mail/bin/answer.py?hl=en&answer=77695).

Create a new destination directory and an empty configuration file:



    :::console
    $ mkdir -p ~/gmail-backup
    $ touch ~/.mbsyncrc




Then add the following parameters in `~/.mbsyncrc`:



    :::text
    IMAPAccount      gmail
    Host             imap.gmail.com
    User             kevin@gmail.com
    Pass             xxxxxxxxxxxxxx
    UseIMAPS         yes
    CertificateFile  ~/gmail-backup/gmail.crt
    CertificateFile  ~/gmail-backup/google.crt
    CertificateFile  /usr/share/ca-certificates/mozilla/Equifax_Secure_CA.crt

    IMAPStore  gmail-cloud
    Account    gmail

    MaildirStore  gmail-backup
    Path          ~/gmail-backup/
    Inbox         ~/gmail-backup/Inbox

    Channel   gmail
    Master    :gmail-cloud:
    Slave     :gmail-backup:
    Create    Slave
    Expunge   Slave
    Sync      Pull
    # Exclude everything under the internal [Gmail] folder, except archived mails
    Patterns  * ![Gmail]* "[Gmail]/All Mail"




Before going further we need to fetch Gmail's certificates:



    :::console
    $ openssl s_client -connect imap.gmail.com:993 -showcerts 2>&1 < /dev/null | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' | sed -ne '1,/-END CERTIFICATE-/p' > ~/gmail-backup/gmail.crt
    $ openssl s_client -connect imap.gmail.com:993 -showcerts 2>&1 < /dev/null | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' | tac | sed -ne '1,/-BEGIN CERTIFICATE-/p' | tac > ~/gmail-backup/google.crt




Then all you have to do is to launch mbsync itself:



    :::console
    $ mbsync gmail
    Reading configuration file ~/.mbsyncrc
    Resolving imap.gmail.com... ok
    Connecting to 173.194.78.108:993... ok
    Connection is now encrypted
    Logging in...
    Channel gmail
    Selecting slave MyLabel... Maildir notice: cannot read UIDVALIDITY, creating new.
    0 messages, 0 recent
    Selecting master MyLabel... 77 messages, 0 recent
    Synchronizing
    Pulling new messages........................................................




Now to keep your local backup fresh don't forget to launch mbsync regularly in the background.

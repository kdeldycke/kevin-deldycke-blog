date: 2005-04-21 14:20:43
title: Remote Backup with rsync
category: English
tags: Backup, CLI, Linux, Mandriva, rsync, SSH, RSA

This little article describe how to setup an automatic backup procedure to a remote machine via the rsync tool.

## Prerequisites

  * A distant server, where backup will be stored (`homeserver.com` in this case),

  * A user account on this server (mine was `kevin`),

  * A ssh deamon running on the server that allow the user to log in.

## Setup rsync

First, install rsync on the client and on the server using:

    :::bash
    $ urpmi rsync

## Synchronization

Then, to synchronise from the local machine to the distant server, just do:

    :::bash
    $ rsync -avz -e ssh /home/client_user/Documents kevin@homeserver.com:/mnt/raid2/

  * `/home/client_user/Documents` is the local folder we want to save (located in the home folder of the client user `client_user`),
  * `homeserver.com` is the distant server name (could be en IP address),
  * `kevin` is the distant user,
  * `/mnt/raid2/` is the distant folder where we want to save the local one.

## Croned synchronization

First, create a pair of cryptographic keys (public, private):

    :::bash
    $ ssh-keygen -t rsa

Then, from the local machine as user `client_user`, register you on the distant server:

    :::bash
    $ ssh-copy-id -i ~/.ssh/id_rsa.pub kevin@homeserver.com

In case your distant machine's SSH server is running on another port than 22 (which is the default port), let's said 222, here is the command that emulate `ssh-copy-id` (as the later doesn't have a port parameter):

    :::bash
    $ cat ~/.ssh/id_rsa.pub | ssh -p 222 kevin@homeserver.com "cat >> ~/.ssh/authorized_keys"

Create a script named `rsync_data_backup.sh` that contain the command you've used previously to synchronize your data:

    :::bash
    $ rsync -avz -e ssh /home/client_user/Documents kevin@homeserver.com:/mnt/raid2/

To run this script with a cron entry, the (unsecure) solution found is to create a key without a passphrase. The cron entry could be something like:

    :::text
    15 13 * * 1-5 client_user /home/client_user/rsync_data_backup.sh > /home/client_user/rsync_data_backup.log

This crontab entry will automaticcaly synchronise our data each first-5 days of the week, at 13:15.

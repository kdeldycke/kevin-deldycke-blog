---
date: 2007-01-27 16:58:00
title: Quick How-To: Install NFS Server & Client
category: English
tags: CLI, Linux, Mandriva, Network, NFS, Server

![nfs.png](/uploads/2007/nfs.png)

In this tiny how-to I'll explain you how to setup a machine as a NFS server and an other one as a client. This example was written based on my experiences on Mandriva, but all commands should almost be the same for other distributions.

First, on the server, install `nfs-utils`:

    :::bash
    $ urpmi nfs-utils

The nfs-utils package provide a daemon for the kernel NFS server and related tools. It is a much higher level of performance than the traditional Linux NFS server used by most users.

Then edit the `/etc/exports` file to add the list of the local folders you wqnt to share:

    :::bash
    [root@localhost ~]# cat /etc/exports
    /mnt/hdd *(rw,insecure,all_squash)

Then, to apply change, restart the NFS server:

    :::bash
    $ /etc/init.d/nfs restart

In this example I simply wanted to share the `/mnt/big-disk` directory and all its sub-folders with anybody, with read and write access. I did this because the server was in a closed LAN, with only one client, that's why no security, authentification or credentials to manage.

By the way, on the server, the only required services to activate at startup are the following:

  * `nfs`
  * `nfslock`
  * `portmap`

On client side, you also need to install `nfs-utils`, in order to benefit `nfslock`:

    :::bash
    $ urpmi nfs-utils

The latter is absolutely not required, but if it's a good idea to have it on the client side.

Then to auto-mount the distant shared folder, add the following line to your `/etc/fstab` file:

    :::text
    192.168.1.22:/mnt/hdd /mnt/distant-hdd nfs user,noatime,rsize=8192,wsize=8192,soft 0 0

Important parameters of the line above are:

  * `192.168.1.22` = IP adress of the NFS server,
  * `/mnt/hdd` = path of the shared folder on the server,
  * `/mnt/distant-hdd` = local folder where the shared folder will be mounted.

Then, you have to modify services on the client to change their default activation state.

Following services must be started at boot:

  * `nfslock`
  * `netfs`
  * `rpcidmapd`

Services that must should be inactivated at boot:

  * `portmap`
  * `nfs`
  * `rpcsvcgssd`

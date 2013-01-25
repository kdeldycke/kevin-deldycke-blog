comments: true
date: 2009-09-07 21:11:03
layout: post
slug: fuse-sshfs-macosx-leopard
title: Fuse and sshfs on MacOSX Leopard
wordpress_id: 817
category: English
tags: Apple, automount, fuse, KDE, Mac OS X Leopard, Linux, MacBook, Apple, Mac OS X, mount, Network, sftp, SSH, sshfs, system

I'm used to access distant machine's file systems via ssh. My favorite environment, [KDE](http://www.kde.org), makes things easy thanks to the support of [`sftp://`](http://wikipedia.org/wiki/SSH_file_transfer_protocol) URLs via a [kio_slave](http://wikipedia.org/wiki/KIO). MacOSX is not as friendly and don't have any built-in mechanism of that kind.

To get similar features in Leopard, we have to rely on [MacFuse](http://code.google.com/p/macfuse/) and [sshfs](http://fuse.sourceforge.net/sshfs.html). I'll explain here how I've installed these components on [MacOSX 10.5](http://www.amazon.com/gp/product/B000FK88JK/ref=as_li_tf_tl?ie=UTF8&tag=kevideld-20&linkCode=as2&camp=217145&creative=399381&creativeASIN=B000FK88JK).![](http://www.assoc-amazon.com/e/ir?t=kevideld-20&l=as2&o=1&a=B000FK88JK&camp=217145&creative=399381)

[![MacFUSE_Banner](http://kevin.deldycke.com/wp-content/uploads/2009/09/MacFUSE_Banner-300x86.png)](http://kevin.deldycke.com/wp-content/uploads/2009/09/MacFUSE_Banner.png)

First, [download the latest MacFuse dmg](http://code.google.com/p/macfuse/downloads/list) and install it. FYI, the version I've got was MacFuse 2.0.3,2.

Then, download the sshfs executable for Leopard, either the [gzipped version](http://osxbook.com/download/sshfs/sshfs-static-leopard.gz) or the binary [from the SVN](http://macfuse.googlecode.com/svn/trunk/filesystems/sshfs/binary/) as [explained in the MacFuse wiki](http://code.google.com/p/macfuse/wiki/MACFUSE_FS_SSHFS).

From a terminal, rename the binary:

    :::bash
    $ sudo mv ./sshfs-static-leopard ./sshfs

Then allow the binary to be executed and place it in the system:

    :::bash
    $ sudo chmod +x sshfs
    $ sudo install sshfs /usr/local/bin

From now you can test sshfs mounting with the following command:

    :::bash
    $ sshfs user@myserver.net:/folder/ /Network/distant-folder -p 22

I personally had a problem here: sshfs complained about a missing library. I fixed this by downloading the required file from the [MacFusion project](http://www.macfusionapp.org) and copying it beside the sshfs binary:

    :::bash
    $ sudo wget http://www.macfusionapp.org/trac/export/86/trunk/SSHFS/sshnodelay.so
    $ sudo mv ./sshnodelay.so /usr/local/bin/
    $ sudo chmod +x /usr/local/bin/sshnodelay.so

If this fail you can also check:

  * that the current user you're logged with has access to the distant server with the `ssh user@myserver.net` command;
  * or that the local mount point exists (you can create it with `mkdir -p /Network/distant-folder`);
  * and finally, you can add the `-o debug` option to the sshfs command above to get additional clues.

Now we will automate the mounting of sshfs at every start.

At this point I recommend you to register the `root` user of your MacOSX system to the distant server:

    :::bash
    $ sudo cat ~/.ssh/id_rsa.pub | sudo ssh -p 22 user@myserver.net "cat >> ~/.ssh/authorized_keys"

If doesn't exists, we have to create the `/etc/fstab` to edit it:

    :::bash
    $ sudo touch /etc/fstab
    $ sudo vi /etc/fstab

And add the following directives:

    :::text
    dummy:user@myserver.net:/folder/ /Network/distant-folder sshfs allow_other,auto_cache,reconnect,port=22,follow_symlinks,volname="Distant folder" 0 0

As you can see I've added lots of options to accommodate my uses. You can get more informations about sshfs options through traditional help pages:

    :::bash
    $ sshfs --help

MacOSX's automount daemon will look for a script called `mount_sshfs` at start. Actually it doesn't exists on your system, but sshfs command line is compatible with what automount expect. So creating a symbolic link will do the trick:

    :::bash
    $ sudo ln -s /usr/local/bin/sshfs /sbin/mount_sshfs

Finally, we can tell automount to acknowledge all our modifications:

    :::bash
    $ sudo automount -vc


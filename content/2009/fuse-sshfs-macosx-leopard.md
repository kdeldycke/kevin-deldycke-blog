---
date: "2009-09-07"
title: "Fuse and sshfs on Mac OS X Leopard"
category: English
tags: Apple, automount, fuse, KDE, Mac OS X 10.5 Leopard, Linux, MacBook, macOS, mount, Network, sftp, SSH, sshfs, system, RSA
---

I'm used to access distant machine's file systems via SSH. My favorite
environment, [KDE](https://www.kde.org), makes things easy thanks to the support
of [`sftp://`](https://wikipedia.org/wiki/SSH_file_transfer_protocol) URLs via a
[KIO slave](https://wikipedia.org/wiki/KIO). Mac OS X is not as friendly and
don't have any built-in mechanism of that kind.

To get similar features in Leopard, we have to rely on [MacFuse
](https://code.google.com/p/macfuse/) and [sshfs
](https://fuse.sourceforge.net/sshfs.html). I'll explain here how I've installed
these components on [Mac OS X Leopard
](https://amzn.com/B000FK88JK/?tag=kevideld-20).

![MacFUSE_Banner]({attach}MacFUSE_Banner.png)

First, [download the latest MacFuse `dmg`
](https://code.google.com/p/macfuse/downloads/list) and install it. FYI, the
version I've got was `2.0.3,2`.

Then, download the sshfs executable for Leopard, either the [gzipped version
](https://osxbook.com/download/sshfs/sshfs-static-leopard.gz) or the binary
[from the SVN
](https://macfuse.googlecode.com/svn/trunk/filesystems/sshfs/binary/) as
[explained in the MacFuse wiki
](https://code.google.com/p/macfuse/wiki/MACFUSE_FS_SSHFS).

From a terminal, rename the binary:

```shell-session
$ sudo mv ./sshfs-static-leopard ./sshfs
```

Then allow the binary to be executed and place it in the system:

```shell-session
$ sudo chmod +x sshfs
$ sudo install sshfs /usr/local/bin
```

From now you can test `sshfs` mounting with the following command:

```shell-session
$ sshfs user@myserver.net:/folder/ /Network/distant-folder -p 22
```

I personally had a problem here: `sshfs` complained about a missing library. I
fixed this by downloading the required file from the [MacFusion project
](https://www.macfusionapp.org) and copying it beside the sshfs binary:

```shell-session
$ sudo wget https://www.macfusionapp.org/trac/export/86/trunk/SSHFS/sshnodelay.so
$ sudo mv ./sshnodelay.so /usr/local/bin/
$ sudo chmod +x /usr/local/bin/sshnodelay.so
```

If this fail you can also check:

  * that the current user you're logged with has access to the distant server
    with the `ssh user@myserver.net` command;
  * or that the local mount point exists (you can create it with
    `mkdir -p /Network/distant-folder`);
  * and finally, you can add the `-o debug` option to the `sshfs` command above
    to get additional clues.

Now we will automate the mounting of `sshfs` at every start.

At this point I recommend you to register the `root` user of your Mac OS X
system to the distant server:

```shell-session
$ sudo cat ~/.ssh/id_rsa.pub | sudo ssh -p 22 user@myserver.net "cat >> ~/.ssh/authorized_keys"
```

If doesn't exists, we have to create the `/etc/fstab` to edit it:

```shell-session
$ sudo touch /etc/fstab
$ sudo vi /etc/fstab
```

And add the following directives:

```text
dummy:user@myserver.net:/folder/ /Network/distant-folder sshfs allow_other,auto_cache,reconnect,port=22,follow_symlinks,volname="Distant folder" 0 0
```

As you can see I've added lots of options to accommodate my uses. You can get
more informations about `sshfs` options through traditional help pages:

```shell-session
$ sshfs --help
```

Mac OS X's `automount` daemon will look for a script called `mount_sshfs` at
start. Actually it doesn't exists on your system, but `sshfs` command line is
compatible with what `automount` expect. So creating a symbolic link will do
the trick:

```shell-session
$ sudo ln -s /usr/local/bin/sshfs /sbin/mount_sshfs
```

Finally, we can tell `automount` to acknowledge all our modifications:

```shell-session
$ sudo automount -vc
```

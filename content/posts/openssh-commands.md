---
date: 2010-03-26 11:29:01
title: OpenSSH commands
category: English
tags: CLI, Computer networking, find, Linux, openssh, proxy, rsync, scp, shell, SSH, tunnel, xargs
---

  * Here is the syntax that makes `scp` support spaces ([source](http://rasterweb.net/raster/2005/01/27/scp-and-spaces/)):

        :::bash
        $ scp foo.com:"/home/fubar/some\ folder/file.txt" ./

  * Copy a bunch of files to a remote server (or how to use `find` with `scp`):

        :::bash
        $ find /var/log/ -iname "*.log" -type f | xargs -i scp '{}' kevin@myserver:/media/backup/logs/

  * Redirect local `8081` port to `proxy.company.com:8080` via a SSH tunnel passing through the `authorized-server.company.com` machine:

        :::bash
        $ ssh -T -N -C -L 8081:proxy.company.com:8080 kevin@authorized-server.company.com

  * Use `rsync` over different SSH port ([source](http://lists.samba.org/archive/rsync/2001-November/000495.html)):

        :::bash
        $ rsync --progress -vrae 'ssh -p 8022' /home/user/docs/ bill@server:/home/user/docs/


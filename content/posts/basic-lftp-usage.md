---
date: 2006-08-18 23:15:49
title: Basic lftp Usage
category: English
tags: CLI, FTP, Hosting, lftp, Web
---

Here is a little log of a micro `lftp` session. I post it just to remind me some basic commands...

Connect to an ftp server and login as `myuser`:

    :::shell-session
    $ lftp ftp://ftp.my-domain.com
    lftp ftp.my-domain.com:~> user myuser
    Password:

Get a list of basic commands:

    :::console
    lftp myuser@ftp.my-domain.com:/www> help
            !<shell -command>                    (commands)
            alias [<name> [<value>]]            anon
            bookmark [SUBCMD]                   cache [SUBCMD]
            cat [-b] <files>                    cd <rdir>
            chmod [OPTS] mode file...           close [-a]
            [re]cls [opts] [path/][pattern]     debug [<level>|off] [-o <file>]
            du [options] <dirs>                 exit [<code>|bg]
            get [OPTS] <rfile> [-o <lfile>]     glob [OPTS] <cmd> <args>
            help [<cmd>]                        history -w file|-r file|-c|-l [cnt]
            jobs [-v]                           kill all|<job_no>
            lcd <ldir>                          lftp [OPTS] <site>
            ls [<args>]                         mget [OPTS] <files>
            mirror [OPTS] [remote [local]]      mkdir [-p] <dirs>
            module name [args]                  more <files>
            mput [OPTS] </files><files>                 mrm </files><files>
            mv <file1> <file2>                  [re]nlist [<args>]
            open [OPTS] <site>                  pget [OPTS] <rfile> [-o <lfile>]
            put [OPTS] </lfile><lfile> [-o <rfile>]     pwd [-p]
            queue [OPTS] [<cmd>]                quote </cmd><cmd>
            repeat [delay] [command]            rm [-r] [-f] <files>
            rmdir [-f] <dirs>                   scache [<session_no>]
            set [OPT] [<var> [<val>]]           site <site_cmd>
            source <file>                       user <user |URL> [<pass>]
            version                             wait [<jobno>]
            zcat <files>                        zmore

Navigate in the file structure:

    :::console
    lftp myuser@ftp.my-domain.com:~> ls
    drwx---r-x   2 myuser users         4096 Jan  9  2005 cgi-bin
    drwx---r-x   2 myuser users         4096 Jan  9  2005 sessions
    drwx---r-x  12 myuser users         4096 Jun  1 01:44 www
    lftp myuser@ftp.my-domain.com:/> cd www
    lftp myuser@ftp.my-domain.com:/www> ls
    -rwx---r-x   1 myuser users        32724 Aug 17 00:43 class.php
    -rwx---r-x   1 myuser users        17896 Jan 10  2005 download.php
    -rwx---r-x   1 myuser users          168 Jan 10  2005 .htaccess
    drwxr-xr-x   3 myuser users         4096 Jan 10  2005 main_admin
    drwxr-xr-x  39 myuser users         4096 Aug  6 01:02 main_plugins

Upload file from local machine to ftp server:

    :::console
    lftp myuser@ftp.my-domain.com:/www> put /home/kevin/class.php
    64714 bytes transferred in 8 seconds (7.9K/s)

Navigate, view, upload and exit:

    :::console
    lftp myuser@ftp.my-domain.com:/www> ls
    -rwx---r-x   1 myuser users        64714 Aug 17 00:56 class.php
    -rwx---r-x   1 myuser users        17896 Jan 10  2005 download.php
    -rwx---r-x   1 myuser users          168 Jan 10  2005 .htaccess
    drwxr-xr-x   3 myuser users         4096 Jan 10  2005 main_admin
    drwxr-xr-x  39 myuser users         4096 Aug  6 01:02 main_plugins
    lftp myuser@ftp.my-domain.com:/www> cd mai
    main_admin/  main_plugins/
    lftp myuser@ftp.my-domain.com:/www> cd main_admin/
    cd ok, cwd=/www/main_admin
    lftp myuser@ftp.my-domain.com:/www/main_admin> ls
    -rwx---r-x   1 myuser users        13449 Jan 10  2005 upload.php
    -rwx---r-x   1 myuser users          100 Aug 17 00:36 version.php
    -rwx---r-x   1 myuser users         4494 Jan 10  2005 message.php
    lftp myuser@ftp.my-domain.com:/www/main_admin> cat ./version.php
    < ?php

    $globinfo['main_version'] = "v 0.0.1 (alpha)";
    $globinfo['main_build'] = "20050815";

    100 bytes transferred
    lftp myuser@ftp.my-domain.com:/www/main_admin> put /home/kevin/
    .bash_history  .bash_logout  .bash_profile  .bashrc  .lftp/  .ssh/  .viminfo  class.php  main_admin/  tmp/
    lftp myuser@ftp.my-domain.com:/www/main_admin> put /home/kevin/main_admin/version.php
    100 bytes transferred
    lftp myuser@ftp.my-domain.com:/www/main_admin> ls
    -rwx---r-x   1 myuser users        13449 Jan 10  2005 upload.php
    -rwx---r-x   1 myuser users          100 Aug 17 00:58 version.php
    -rwx---r-x   1 myuser users         4494 Jan 10  2005 message.php
    lftp myuser@ftp.my-domain.com:/www/main_admin> exit
    $


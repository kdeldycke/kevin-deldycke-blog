comments: true
date: 2012-10-09 12:46:06
layout: post
slug: how-to-create-local-copy-svn-repository
title: How-to create a local copy of a remote SVN repository
wordpress_id: 5085
category: English
tags: Backup, code, Repository, SCM, Subversion, svk, svn

A long time ago, duplicating a remote Subversion repository required to have administration rights on the machine hosting the said repository. The only [solution back then was to use SVK](http://kevin.deldycke.com/2007/04/how-to-backup-mirror-a-public-svn-repository/), a defunct project that was adding a layer on top of SVN to make it a distributed [SCM](http://en.wikipedia.org/wiki/Revision_Control).

Today, to dump a repository you don't manage, all the tools you need are available with the standard Subversion distribution.

First, let's create an empty local SVN repository:

    :::bash
    $ rm -rf ./svn-repo
    $ svnadmin create ./svn-repo
    $ sed -i 's/# password-db = passwd/password-db = passwd/' ./svn-repo/conf/svnserve.conf
    $ echo "kevin = kevin" >> ./svn-repo/conf/passwd
    $ kill `ps -ef | grep svnserve | grep -v grep | awk '{print $2}'`
    $ svnserve --daemon --listen-port 3690 --root ./svn-repo

Now we have to make sure the synchronization utility is allowed to do anything it wants on our local repository:

    :::bash
    $ echo "#!/bin/sh" > ./svn-repo/hooks/pre-revprop-change
    $ chmod 755 ./svn-repo/hooks/pre-revprop-change

Then we have to initialize the synchronization between the remote SVN (`https://svn.example.com/svn/internal-project`) and the local SVN (`svn://localhost:3690`):

    :::bash
    $ svnsync init --sync-username "kevin" --sync-password "kevin" --source-username "kevin@example.com" --source-password "XXXXXX" svn://localhost:3690 https://svn.example.com/svn/internal-project

Once all of this configuration is done, we can start dumping the content of the remote repository to our local copy:

    :::bash
    $ svnsync --non-interactive --sync-username "kevin" --sync-password "kevin" --source-username "kevin@example.com" --source-password "XXXXXX" sync svn://localhost:3690


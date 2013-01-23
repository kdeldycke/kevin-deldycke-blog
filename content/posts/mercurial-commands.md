comments: true
date: 2010-10-07 13:26:53
layout: post
slug: mercurial-commands
title: Mercurial commands
wordpress_id: 2106
category: English
tags: CLI, hg, mercurial

  * Checkout a distant repository:

        :::bash
        $ hg clone http://bitbucket.org/mirror/django

  * Commit all changes locally:

        :::bash
        $ hg commit -m "Here is my commit fixing bugs."

  * Push local commits to the remote repository:

        :::bash
        $ hg push

  * Apply latest changes of the remote repository to our local working copy:

        :::bash
        $ hg pull

  * Align the current repository to a specific revision:

        :::bash
        $ hg update -r 502

  * Restore all changes and files to the state they are in the distant repository:

        :::bash
        $ hg update -C

  * My minimal `~/.hgrc` config file:

        :::ini
        [ui]
        username = Kevin Deldycke <kevin@deldycke.com>
        verbose = True

        [auth]
        # BitBucket creds
        bb.prefix = bitbucket.org
        bb.username = kdeldycke
        bb.password = XXXXXXXXXXX
        bb.schemes = https

  * Display the last 5 commits:

        :::bash
        $ hg log --limit 5

  * Display the local changes since last commit:

        :::bash
        $ hg diff

  * Undo the last local commit:

        :::bash
        $ hg rollback

  * Create a tag on a particular revision:

        :::bash
        $ hg tag -r 432 component-2.6.1

  * Create a bundle file containing all changes committed locally:

        :::bash
        $ hg bundle fix-bug.bundle


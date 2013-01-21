comments: true
date: 2010-10-07 13:26:53
layout: post
slug: mercurial-commands
title: Mercurial commands
wordpress_id: 2106
category: English
tags: CLI, hg, mercurial

  * Checkout a distant repository:

    :::console
    hg clone http://bitbucket.org/mirror/django

  * Commit all changes locally:

    :::console
    hg commit -m "Here is my commit fixing bugs."

  * Push local commits to the remote repository:

    :::console
    hg push

  * Apply latest changes of the remote repository to our local working copy:

    :::console
    hg pull

  * Align the current repository to a specific revision:

    :::console
    hg update -r 502

  * Restore all changes and files to the state they are in the distant repository:

    :::console
    hg update -C

  * My minimal `~/.hgrc` config file:

    :::text
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

    :::console
    hg log --limit 5

  * Display the local changes since last commit:

    :::console
    hg diff

  * Undo the last local commit:

    :::console
    hg rollback

  * Create a tag on a particular revision:

    :::console
    hg tag -r 432 component-2.6.1

  * Create a bundle file containing all changes committed locally:

    :::console
    hg bundle fix-bug.bundle


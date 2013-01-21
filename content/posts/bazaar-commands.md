comments: true
date: 2011-11-01 12:46:26
layout: post
slug: bazaar-commands
title: Bazaar commands
wordpress_id: 3638
category: English
tags: bazaar, CLI, development, Launchpad, Linux, OpenERP, programming, Version control




  * Check-out in the local `openerp-server` folder the `6.0` branch of the OpenERP server project from Launchpad:


        :::console
        bzr branch lp:openobject-server/6.0 openerp-server







  * Same command as above, but fetch a particular revision:


        :::console
        bzr branch lp:openobject-server/6.0 -r 3425 openerp-server







  * Get revision number of the local copy we sit in:


        :::console
        bzr revno ./







  * Change the repository to a previous revision:


        :::console
        bzr revert -r 1234







  * Remove lock file on the current repository:


        :::console
        bzr break-lock








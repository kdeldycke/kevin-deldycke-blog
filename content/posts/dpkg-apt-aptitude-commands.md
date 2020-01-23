---
date: 2008-12-28 19:25:36
title: dpkg, APT & Aptitude commands
category: English
tags: apt, aptitude, backport, CLI, Debian, dpkg, Linux, Ubuntu
---


## Search

  * List all installed packages:

        :::bash
        $ dpkg -l

  * List all recently installed packages:

        :::bash
        $ zcat -f /var/log/dpkg.log* | grep "\ install\ " | sort

  * Show the changelog of a package (here, the linux kernel of Ubuntu):

        :::bash
        $ aptitude changelog linux-generic

  * Which package contain a given file:

        :::bash
        $ apt-file search file_to_search

  * Get the list of files of a package:

        :::bash
        $ apt-file list package_name

  * Extract content of a package:

        :::bash
        $ ar vx mypackage.deb


## Install

  * Install a package from a lower-priority repository, like the backport repository:

        :::bash
        $ apt-get -t squeeze-backports install my-package

  * Force reinstallation of a package:

        :::bash
        $ apt-get -d --reinstall install my-package
        $ dpkg --install --force-confmiss /var/cache/apt/archives/my-package.deb


## Upgrade

  * Upgrade package listing and metadata:

        :::bash
        $ sudo apt update

  * Force `yes` so that package maintainer's version of config files always prevails:
  
        :::bash
        $ sudo apt upgrade -y --force-yes


## Holding

  * Hold a package with either `dpkg` or `aptitude`:

        :::bash
        $ echo "kdenlive hold" | dpkg --set-selections

    or:

        :::bash
        $ aptitude hold kdenlive

  * Unhold a package:

        :::bash
        $ echo "kdenlive install" | dpkg --set-selections

    or:

        :::bash
        $ aptitude unhold kdenlive

  * List holded packages:

        :::bash
        $ dpkg --get-selections | grep hold
        
       
 ## Uninstall

  * Uninstall a package throughly (both program files and configuration):

        :::bash
        $ apt-get remove --purge my_package

  * Force removal of a package while ignoring all dependencies:

        :::bash
        $ dpkg --remove --force-depends libsomething

  * Remove orphaned pakages:

        :::bash
        $ deborphan | xargs apt-get -y remove --purge


## Clean-up

  * Clean aptitude local cache:

        :::bash
        $ apt-get clean

  * Remove `dpkg` lock file:

        :::bash
        $ rm /var/lib/dpkg/lock

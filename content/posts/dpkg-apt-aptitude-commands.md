comments: true
date: 2008-12-28 19:25:36
layout: post
slug: dpkg-apt-aptitude-commands
title: dpkg, APT & Aptitude commands
wordpress_id: 460
category: English
tags: apt, aptitude, backport, CLI, Deb, Debian, dpkg, Linux, ubuntu




  * List all installed packages:

    
    :::console
    dpkg -l
    






  * Extract content of a package:

    
    :::console
    ar vx mypackage.deb
    






  * List all recently installed packages:

    
    :::console
    zcat -f /var/log/dpkg.log* | grep "\ install\ " | sort
    






  * Install a package from a lower-priority repository, like the backport repository:

    
    :::console
    apt-get -t squeeze-backports install my-package
    






  * Force reinstallation of a package:

    
    :::console
    apt-get -d --reinstall install my-package
    dpkg --install --force-confmiss /var/cache/apt/archives/my-package.deb
    






  * Clean aptitude local cache:

    
    :::console
    apt-get clean
    






  * Uninstall a package throughly (both program files and configuration):

    
    :::console
    apt-get remove --purge my_package
    






  * Force removal of a package while ignoring all dependencies:

    
    :::console
    dpkg --remove --force-depends libsomething
    






  * Remove orphaned pakages:

    
    :::console
    deborphan | xargs apt-get -y remove --purge
    






  * Show the changelog of a package (here, the linux kernel of Ubuntu):

    
    :::console
    aptitude changelog linux-generic
    






  * Which package contain a given file:

    
    :::console
    apt-file search file_to_search
    






  * Get the list of files of a package:

    
    :::console
    apt-file list package_name
    






  * Remove `dpkg` lock file:

    
    :::console
    rm /var/lib/dpkg/lock
    






  * Hold a package with either `dpkg` or `aptitude`:

    
    :::console
    echo "kdenlive hold" | dpkg --set-selections
    



    
    :::console
    aptitude hold kdenlive
    






  * Unhold a package:

    
    :::console
    echo "kdenlive install" | dpkg --set-selections
    



    
    :::console
    aptitude unhold kdenlive
    






  * List holded packages:

    
    :::console
    dpkg --get-selections | grep hold
    







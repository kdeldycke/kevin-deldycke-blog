---
date: 2006-11-29 01:01:55
title: RPM, Urpmi & Yum commands
category: English
tags: Archive formats, CLI, cpio, genhdlist, Linux, Mandriva, Red Hat, RPM, urpmi, yum
---

## RPM

  * List all installed packages:

        :::bash
        $ rpm -qa

  * Get the list of all installed packages and their architecture:

        :::bash
        $ rpm -qa --queryformat "%-40{NAME} %-8{ARCH}\n"

  * Same as above, but show `i586` packages only:

        :::bash
        $ rpm -qa --queryformat "%-40{NAME} %-8{ARCH}\n" | grep i586

  * Downgrade a package to an old version:

        :::bash
        $ wget ftp://ftp.repository.org/mandrakelinux/official/10.0/package-1.0-1mdk.i586.rpm
        $ rpm -Uvh --oldpackage package-1.0-1mdk.i586.rpm

  * Unpack/Deflate/Extract a RPM without installing it:

        :::bash
        $ rpm2cpio dummy.src.rpm | cpio -id

  * Evaluate `%mkrel 3` rpm macro:

        :::bash
        $ rpm --eval '%mkrel 3'

  * Force removal of a package that has problems with embedded "pre-" and/or "post-" scripts:

        :::bash
        $ rpm -e --noscripts packagename

## Urpmi

  * List all available packages with name containing `python`:

        :::bash
        $ urpmq --fuzzy python

  * Find which RPM contain the file named `dummy`:

        :::bash
        $ urpmf dummy

  * Get informations about the `dummy` RPM:

        :::bash
        $ urpmq -i dummy

  * Get the list of all RPMs that require `python-psyco` package:

        :::bash
        $ urpmf --requires python-psyco

  * Get the list of all RPMs that provide `python-psyco` package:

        :::bash
        $ urpmf --provides python-psyco

  * I use this command in a cron entry to update automatically and regularly my Mandriva:

        :::bash
        $ /usr/sbin/urpmi.update -a && /usr/sbin/urpmi --update --auto --auto-select

  * Generate urpmi repository index and metadata of the current folder:

        :::bash
        $ genhdlist ./

  * [APT/URPMI commands list](http://linux.ensimag.fr/urpmiapt.html)

## Yum

  * Install a new package:

        :::bash
        $ yum install subversion

  * Search for packages containing the `x11` string:

        :::bash
        $ yum search x11

  * Get the list of packages that provide Python's Subversion bindings:

        :::bash
        $ yum provides "*/svn/__init__.py"

  * Update repository index:

        :::bash
        $ yum update

  * Clear all caches (sometimes required to force a repository index update):

        :::bash
        $ yum clean all

  * Generate [Yum](http://yum.baseurl.org) repository index and metadata of the current folder:

        :::bash
        $ createrepo -v ./


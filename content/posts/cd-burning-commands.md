comments: true
date: 2006-10-25 00:49:46
layout: post
slug: cd-burning-commands
title: CD Burning commands
wordpress_id: 73
category: English
tags: burning, cd, cdrdao, cdrecord, CLI, dvd, Hardware, Linux, mkisofs

  * List all CD devices:

        :::console
        cdrdao scanbus

  * Blank a CD-RW:

        :::console
        cdrdao blank --device ATA:0,1,0 --driver generic-mmc

  * Burn an ISO:

        :::console
        cdrecord -v speed=8 dev=ATA:0,1,0 ./geexbox-0.98-fr.iso

  * Generate an ISO image of a CD-ROM:

        :::console
        dd if=/dev/cdrom of=/tmp/cdrom-image.iso

  * Create an ISO from a local directory:

        :::console
        mkisofs -R -r -l -J -V volid -o /tmp/cdrom-image.iso src

    `volid` is the volume ID to be written into the master block;

    `/tmp/cdrom-image.iso` is the destination filename of the newly created ISO image;

    `src` is the temporary ISO directory containing the files and file structure you wish to have included in the ISO image.

  * Mount a local ISO image as if it's a physical CD-Rom:

        :::console
        mount -t iso9660 -o loop /tmp/cdrom-image.iso /media/cd-image/

  * Mount an UDF file system image:

        :::console
        fuseiso -p dvd.img /media/dvd-image/

  * Convert a [Nero's proprietary `.nrg` CD image](http://en.wikipedia.org/wiki/NRG_(file_format)) to standard ISO file:

        :::console
        nrg2iso dvd-image.nrg dvd-image.iso


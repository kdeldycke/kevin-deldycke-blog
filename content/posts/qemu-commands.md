date: 2005-06-04 15:34:01
slug: qemu-commands
title: Qemu commands
category: English
tags: CLI, Linux, Qemu

Some useful command to help running and setup qemu...

  * Create an empty compressed 10 Go disk image (in `qcow2` format):

        :::bash
        $ qemu-img create -f qcow2 /home/kevin/qemu-disk-image.qcow 10G

  * Boot on your machine's CD-Rom in qemu with previous disk image as primary HDD:

        :::bash
        $ qemu -cdrom /dev/cdrom -hda /home/kevin/qemu-disk-image.qcow -boot d

  * Same as above but with a CD-Rom `iso` image:

        :::bash
        $ qemu -cdrom /home/kevin/ubuntu.iso -hda /home/kevin/qemu-disk-image.qcow -boot d

  * Boot the previously created disk image:

        :::bash
        $ qemu /home/kevin/qemu-disk-image.qcow

  * Convert `qcow` image to a `raw` image:

        :::bash
        $ qemu-img convert /home/kevin/qemu-disk-image.qcow -O raw /home/kevin/qemu-disk-image.raw

  * Mount a RAW disk image:

        :::bash
        $ mount -o loop,offset=32256 /home/kevin/qemu-disk-image.raw /media/qemu/

  * Mount a `qcow2` disk image via the `nbd` protocol (don't forget to install the `nbd-client` package):

        :::bash
        $ modprobe nbd max_part=63
        $ qemu-nbd -c /dev/nbd0 /home/kevin/qemu-disk-image.qcow2
        $ mount /dev/nbd0p1 /media/qemu

  * To run a x86_64 guest system on a 32-bit host, simply use `qemu-system-x86_64` binary command instead of `qemu`.


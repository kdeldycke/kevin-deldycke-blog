---
date: "2005-05-29"
title: How-To Mount a File System Binary Image
category: English
tags: CLI, Hardware, Linux
---

## Obtain a binary image

We have a USB key with a file system on it, and we want to save its content. We do a binary image using:

    ```shell-session
    $ dd if=/dev/sda1 of=/home/kevin/usb_key.img
    ```

## Mount the image file

Get informations about the file system of the image file using:

    ```shell-session
    $ fdisk -l -u /home/kevin/usb_key.img
    ```

This show you something like that:

    ```console
    Disque usb_key.img: 0 Mo, 0 octets
    9 têtes, 56 secteurs/piste, 0 cylindres, total 0 sectors
    Unités = secteurs de 1 * 512 = 512 octets

    Périphérique Boot   Start   End      Blocks   Id   System
    usb_key.img1        56      511559   255752   83   Linux
    ```

Get the sector number where the partition start (56) and the size of sectors (512). Multiply the two values:

    ```text
    56 * 512 = 28672
    ```

Then setup a loopback block device based on the image:

    ```shell-session
    $ losetup -o 28672 /dev/loop0 /home/kevin/usb_key.img
    ```

Now you can mount your USB key:

    ```shell-session
    $ mount /dev/loop0 /mnt/usb_key/
    ```


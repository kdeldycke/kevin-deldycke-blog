---
date: "2010-02-12"
title: How-to configure GRUB in (k)Ubuntu
category: English
tags: grub, Kubuntu, Ubuntu, Linux, Ubuntu, MBR
---

Here is a little note to remind me how to customize [GRUB](https://www.gnu.org/software/grub/) the (k)Ubuntu way.

![](/uploads/2010/grub-kubuntu-custom-menu.jpg)

In fact the only important information I need to remember is the location of the file containing all GRUB options:

    ```shell-session
    $ sudo vi /etc/default/grub
    ```

There I've lowered the `GRUB_TIMEOUT` option to 1 second to speed up the boot process (default was 10 seconds).

I also had some sound issues with the latest Karmic Koala's kernel upgrade. So I've changed the `GRUB_DEFAULT` variable from `0` to `2`. This tells GRUB to boot the third entry of the menu, which correspond to the kernel I was using before the bad upgrade. And be careful: you have to fix this index on each following kernel upgrade, because the given position is absolute and new kernels add their own entries at the top of the menu.

And finally, after all these changes, don't forget to regenerate all the GRUB's scripts with the following command:

    ```shell-session
    $ sudo update-grub
    ```


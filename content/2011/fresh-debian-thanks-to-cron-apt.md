---
date: "2011-05-24"
title: "Keep a Debian fresh thanks to cron-apt"
category: English
tags: apt, aptitude, cron, cron-apt, Debian, Linux, sed, Regular expression
---

As I [mentioned in an old comment](https://kevin.deldycke.com/2008/dpkg-apt-aptitude-commands#comment-769311499), I use `cron-apt` to keep my Debian servers fresh.

This post is just a quick reminder to my future self, about how I setup `cron-apt` on my machines.

First we install the package:

    ```shell-session
    $ aptitude install cron-apt
    ```

Then we configure it:

    ```shell-session
    $ sed -i 's/# MAILON="error"/MAILON="always"/g' /etc/cron-apt/config
    $ sed -i 's/# MAILTO="root"/MAILTO="user@example.com"/g' /etc/cron-apt/config
    ```

That's it!

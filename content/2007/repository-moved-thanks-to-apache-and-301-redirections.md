---
date: "2007-02-28"
title: "Repository Moved thanks to Apache and 301 Redirections"
category: English
tags: Apache, Hosting, htaccess, ISP, Linux, Mandriva, RPM, urpmi
---

Since the creation of my personal Mandriva repository (
[10 months ago]({filename}/2006/new-repository-for-mandriva-2006.md))
the number of my RPMs did not cease to increase. Currently all RPMs and SRPMs
from 2006.0 and 2007.0 take 383MiB of space.

So I decided to move the `https://kev.coolcavemen.com/static/repository` folder
to `https://kevin.deldycke.free.fr/repository`, which is a 10GiB (yes, ten
[gibibyte](https://en.wikipedia.org/wiki/Gibibyte), this is not a typo) free web
space offered by [Free](https://free.fr), my ISP.

To do this smoothly, I've just set up a generic `301` redirection thanks to
Apache. This is the only line I added to my root `.htaccess` file to enable
this:

    ```apache
    Redirect permanent /static/repository https://kevin.deldycke.free.fr/repository
    ```

This move will normally be completely silent for you. So please, let me now if
something bad happend while you play with my repository.
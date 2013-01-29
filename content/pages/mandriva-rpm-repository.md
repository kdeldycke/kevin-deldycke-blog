comments: false
date: 2006-04-13 02:21:16
layout: page
slug: mandriva-rpm-repository
title: Mandriva RPMs
wordpress_id: 10

![](/static/uploads/2007/04/mandriva-2007-blue-logo.png)

All these Mandriva RPM repositories are **no longer maintained**.

These repositories contains all the backports I made from [cooker](http://wiki.mandriva.com/en/Development). They also contain RPMs I found around the net, and some others I've created from scratch.

You can add a repository to your `urpmi` database by replacing the URL with the right one in the command line below:

    :::console
    sudo urpmi.addmedia --update kev-rpms http://kevin.deldycke.com/static/repository/mandriva/<version>/<arch>/

`urpmi` is able to resolve packages' dependencies, so  please, do not forget to add all `main`, `contrib` and `PLF` (both `free` and `non-free`) repository from [easy urpmi](http://easyurpmi.zarb.org). It's also a good idea to add `backports` version of all those previous repository.

Here is the list of repositories that are available right now:

    Mandriva version
    Repository type
    Content

2009.1

[x86_64](http://kevin.deldycke.com/static/repository/mandriva/2009.1/x86_64)

—

[SRPMs](http://kevin.deldycke.com/static/repository/mandriva/2009.1/SRPMS)

[Linux kernel](http://www.kernel.org) 2.6.31-rc5, [QLC](http://sourceforge.net/projects/qlc) 3.0.0, [dmg2img](http://vu1tur.eu.org/tools/) 1.6, [Google's Protocol Buffers](http://code.google.com/p/protobuf/) 2.2.0, [Google's ctemplate](http://code.google.com/p/google-ctemplate/) 0.95, [libmicrohttpd](http://www.gnu.org/software/libmicrohttpd/) 0.4.2, ...

2008.1

[x86_64](http://kevin.deldycke.com/static/repository/mandriva/2008.1/x86_64)

—

[SRPMs](http://kevin.deldycke.com/static/repository/mandriva/2008.1/SRPMS)

QLC 2.6.1, [Open DMX USB drivers](http://www.erwinrol.com/index.php?opensource/dmxusb.php), [LLA](http://code.google.com/p/linux-lighting/), ...

2008.0

—

[i586](http://kevin.deldycke.com/static/repository/mandriva/2008.0/i586)

[SRPMs](http://kevin.deldycke.com/static/repository/mandriva/2008.0/SRPMS)

[Amarok](http://amarok.kde.org) 1.4.8, [Interreta Televidilo](http://home.gna.org/televidilo/) 0.6, [Rugg](http://rugg.sourceforge.net) 0.2.3, [Python iCalendar](http://pypi.python.org/pypi/icalendar) 1.2, ...

2007.1

[x86_64](http://kevin.deldycke.com/static/repository/mandriva/2007.1/x86_64)

[i586](http://kevin.deldycke.com/static/repository/mandriva/2007.1/i586)

[SRPMs](http://kevin.deldycke.com/static/repository/mandriva/2007.1/SRPMS)

Amarok 1.4.7, Interreta Televidilo 0.6, Rugg 0.2.3, Python iCalendar 1.2, ...

2007.0

—

[i586](http://kevin.deldycke.com/static/repository/mandriva/2007.0/i586)

[SRPMs](http://kevin.deldycke.com/static/repository/mandriva/2007.0/SRPMS)

[Kdenlive](http://www.kdenlive.org) 0.4, Amarok 1.4.5, [SVK](http://svk.bestpractical.com) 2.0, Rugg 0.2.3, [Qemu](http://wiki.qemu.org) 0.9, [Grisbi](http://www.grisbi.org) 0.5.9, Python iCalendar 1.2, [Diva](http://www.mdk.org.pl/2006/12/7/state-of-diva) SVN trunk version, ...

2006.0

—

[i586](http://kevin.deldycke.com/static/repository/mandriva/2006.0/i586)

[SRPMs](http://kevin.deldycke.com/static/repository/mandriva/2006.0/SRPMS)

Amarok 1.4.3, [Tor](http://www.torproject.org) 0.1.1.21, Rugg 0.2.2, Qemu 0.7.2, Grisbi 0.5.8, [Baghira](http://baghira.sourceforge.net) 0.7, [Wormux](http://www.wormux.org) 0.7...


---
date: "2008-05-13"
title: QLC 2.6.1 for Mandriva 2008.1
category: English
tags: DMX, Linux, LLA, Mandriva, Open DMX, QLC, RPM, Stage Lighting, USB
---

![QLC 2.6.1 on Mandriva 2008.1](/uploads/2008/qlc-261-on-mandriva-20081.png)

I've just backported QLC 2.6.1 from Fedora Core to Mandriva 2008.1.
[Q Light Controller](https://qlc.sourceforge.net) is a software designed to pilot
lights (both moving and static ones) on stages via the
[DMX communication protocol](https://en.wikipedia.org/wiki/DMX512-A). This is my
first step to bring together two of my main recent interests:
[stage lighting](https://en.wikipedia.org/wiki/Stage_lighting) and linux.

These RPMs are currently
[only available for the x86_64 version of Mandriva](https://github.com/kdeldycke/mandriva-specs)
but includes the
[Open DMX USB drivers](https://www.erwinrol.com/index.php?opensource/dmxusb.php)
and
[Lighting Architecture for Linux (LLA)](https://www.nomis52.net/?section=projects&sect2=lla&page=llaintro)
packages. All the sources of these packages came from the
[repository I found](https://rpms.netmindz.net/FC6/) in the
["LLA, OpenDMX USB and Q Light Controller Tutorial" tutorial](https://opendmx.net/index.php/LLA,_OpenDMX_USB_and_Q_Light_Controller_Tutorial).

I haven't played with QLC yet: I've just started it and as you can see on the
screenshot it seems to work. Happy testing! ;)

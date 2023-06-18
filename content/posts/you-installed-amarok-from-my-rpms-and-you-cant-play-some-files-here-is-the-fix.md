---
date: "2006-08-19"
title: You installed Amarok from my RPMs and can't play some files? Here is the fix...
tags: Amarok, KDE, Linux, Mandriva, Music, RPM
---

My two previous RPMs packages of Amarok ([1.4.1](https://kevin.deldycke.com/2006/07/amarok-141-for-mandriva-2006/) and [1.4.2beta1](https://kevin.deldycke.com/2006/08/amarok-142-beta1-for-mandriva-2006/)) for Mandriva 2006 were not able to play some files because of their file format. In a previous comment, [Promeneur tell us](https://kevin.deldycke.com/2006/07/amarok-141-for-mandriva-2006/#comment-45) that my 1.4.1 package was not able to play Mpeg2 files.

I myself experienced a similar problem: both 1.4.1 and 1.4.2beta1 were not able to play any of my Flac files. Apart the "`There is no audio channel!`" error message, I had no other information to help me track the bug.

Then I remembered that I was using [PFL RPMs](https://plf.zarb.org/about.php) beside official Mandriva ones. So I updated plf-non-free and plf-free repositories. So I installed all packages whose name followed the "`xine-_something_-1.1.1`" pattern. Just after that Amarok was playing Flac files as expected!

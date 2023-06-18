---
date: "2007-06-02"
title: "How-to launch a KDE Application in Another Language"
category: English
tags: KDE, Linux
---

This is a old discussion I had at least 9 months ago with people from the `#kde` IRC channel.

I was looking for a way to get an error message in english instead of french. After reading the following discussion, the solution is quite obvious, but at that time I was probably too tired to think efficiently... :)

    ```irc
    <kev1> Hi ! I use amarok in french and I would like to run it in english. How can I do ?
    <kev1> Things like "env LANG=en amarok" doesn't work...
    <shining> kev1: LANG=C amarok
    <shining> ho no
    <shining> kde apps don't use the locale env, do they? they use kde-i18n stuff
    <Blissex> kev1: download the package with the amaroK english messages if your distro makes it a separate one. Else download the general KDE english stuff.
    <Blissex> shining: they use both. They need the right package to get the actual messages/names, and then the env variable to select among them.
    <kev1> Shining: doesn't work either...
    <shining> Blissex: ho I see
    <Blissex> shining: problem is, they all use the language set when KDE started :-)
    <kev1> Blissex: ok I see...
    <shining> kev1: why do you want that though? it's a bit strange
    <Blissex> kev1: it may be possible to run some KDE apps in one locale and others in another locale, but I would be surprised.
    <kev1> Shining: I have some error messages in amarok but they are translated in french. I need the english version to search on google and/or make a bug report if necessary
    <kev1> (I use amarok 1.4.2-beta1)
    <Ardonik> kev1: **kcontrol -> Accessibility -> Country**
    <kev1> Ardonik: ok, let me try it
    <shining> kev1: ha yes, I had the same problem for other apps, where LANG=C worked fine :)
    <kev1> Ardonik: thanks ! it work perfectly and immediately ! Quite impressive
    <Ardonik> No problem
    <Blissex> kev1: what you can do is to change the locale in 'Regional&Accessibility;', start amaroK, and then change it back.
    <kev1> Blissex: yes, that's what Ardonik suggest me and it work perfectly.
    ```

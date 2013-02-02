date: 2010-08-25 17:36:59
title: How-to fix Lotus Notes' disabled TCPIP port error
category: English
tags: Lotus Notes, Mac OS X Leopard, Lotus Notes, Apple, Mac OS X, Network

Today I encountered this error message:

![](/static/uploads/2010/08/lotus-notes-tcp-ip-error.png)

> Error logging into server localhost: You must enable the Notes TCPIP port.

This appeared in the fat Lotus Notes client v7.0.3 running on Mac OS X Leopard (10.5).

To fix this issue, first of all, quit Notes. Then [locate the Notes' preference file](http://www-01.ibm.com/support/docview.wss?uid=swg21090921) attached to your current user. Mine was found in my home directory at `/Users/kevin/Library/Preferences/Notes Preferences`. At the end of this file, add [these two directives](http://macosx.com/forums/1277870-post4.html):

    :::ini
    TCPIP=TCP,0,15,0
    Ports=TCPIP

Then relaunch Lotus Notes and switch from `Island (Disconnected)` location to another that will allow your client to listen to the network. In my case, `Home (Network Dialup)` did the trick:

![](/static/uploads/2010/08/lotus-notes-location-switch.png)

Problem solved ! :)

FYI, this error can still be encountered in Lotus Notes 8.5 on Mac OSX Snow Leopard (10.6). In this context, the solution is exactly the same.

Here is a screenshot of the location drop-down menu with the new Notes interface:

![](/static/uploads/2010/08/lotus-notes-8-5-location-switch.png)

And if you're looking for the `notes.ini` file on Windows, it's located at `C:\Documents and Settings\[username]\Local Settings\Application Data\Lotus\Notes\Data\`. At least in my case with Lotus Notes 8.5.2 under Windows XP SP2:

![](/static/uploads/2010/08/notes-ini-location-windows-xp.png)


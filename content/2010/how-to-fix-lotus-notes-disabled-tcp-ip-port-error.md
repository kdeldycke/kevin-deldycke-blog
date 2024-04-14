---
date: "2010-08-25"
title: "How-to fix Lotus Notes' disabled TCPIP port error"
category: English
tags: Lotus Notes, Mac OS X 10.5 Leopard, Mac OS X 10.6 Snow Leopard, Lotus Notes, Apple, macOS, Network
---

Today I encountered this error message:

![]({attach}lotus-notes-tcp-ip-error.png)

> Error logging into server localhost: You must enable the Notes TCPIP port.

This appeared in the fat Lotus Notes client v7.0.3 running on Mac OS X Leopard.

To fix this issue, first of all, quit Notes. Then [locate the Notes' preference
file](https://www-01.ibm.com/support/docview.wss?uid=swg21090921) attached to
your current user. Mine was found in my home directory at
`/Users/kevin/Library/Preferences/Notes Preferences`. At the end of this file,
add [these two directives](https://macosx.com/forums/1277870-post4.html):

```ini
TCPIP=TCP,0,15,0
Ports=TCPIP
```

Then relaunch Lotus Notes and switch from `Island (Disconnected)` location to
another that will allow your client to listen to the network. In my case,
`Home (Network Dialup)` did the trick:

![]({attach}lotus-notes-location-switch.png)

Problem solved! :)

FYI, this error can still be encountered in Lotus Notes 8.5 on Mac OS X
Snow Leopard. In this context, the solution is exactly the same.

Here is a screenshot of the location drop-down menu with the new Notes
interface:

![]({attach}lotus-notes-8-5-location-switch.png)

And if you're looking for the `notes.ini` file on Windows, it's located at
`C:\Documents and Settings\[username]\Local Settings\Application Data\Lotus\Notes\Data\`.
At least in my case with Lotus Notes 8.5.2 under Windows XP SP2:

![]({attach}notes-ini-location-windows-xp.png)

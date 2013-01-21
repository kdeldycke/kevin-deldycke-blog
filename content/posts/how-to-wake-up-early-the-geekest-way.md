comments: true
date: 2006-08-02 16:14:52
layout: post
slug: how-to-wake-up-early-the-geekest-way
title: How to wake up early, the geekest way
wordpress_id: 29
category: English
tags: life, Linux, mobile phone, mplayer, Music, travel

[![Mobile Phone, Broken Screen](http://kevin.deldycke.com/wp-content/uploads/2006/08/pict4644-150x150.jpg)](http://kevin.deldycke.com/wp-content/uploads/2006/08/pict4644.jpg) I was in a country far far away last month. So far that there was no broadband access (yes, this is possible). Anyway... Generally I use my mobile phone as a clock and as an alarm clock. Unfortunalty I brake it down just before my night flight.

So, to simplify, I was abroad in a hotel, the sun was down since a while, I was tired, and I had to wake up early. No electronic devices to help me, except my laptop... And then came the idea to combine `cron` and `mplayer` to automaticcaly play some MP3s at a given time.

Here is how I've done it. First, as `root`, create an empty file in `/etc/cron.d/`. Let us call it `wake-up`:

    
    :::console
    touch /etc/cron.d/wake-up
    



Then edit it to put the following command:

    
    :::text
    15 6 * * * root mplayer /home/kevin/music/CoolCavemen/AllCoolHits/*.flac > /dev/null 2>&1 /dev/null
    



This mean that mplayer will be launched at 6:15 and will play all FLAC files from the `/home/kevin/music/CoolCavemen/AllCoolHits/` directory. I let you adapt those parameters to fit your needs.

_Random Tips:_




  * Take care of time zone (system time and local time are very different).


  * Check that your volume is not muted and crank the volume up !


  * Run the `mplayer /home/kevin/music/CoolCavemen/AllCoolHits/*.flac > /dev/null 2>&1 /dev/null` command alone in another terminal before you go to sleep to be sure it work (i.e. to check that all sound-related sub-systems are loaded).


  * Be sure that cron deamon is up an running (do a `/etc/init.d/crond restart` if you are not sure).

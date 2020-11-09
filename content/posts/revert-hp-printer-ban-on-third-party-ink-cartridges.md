---
date: 2020-11-09 12:00:00
category: English
tags: CLI, Hardware, printer, Hewlett-Packard, firmware, ink, office, DRM, macOS
title: How-to revert HP printer's ban on 3rd-party ink cartridges
---

Hewlett & Packard, the founders, had great lessons to teach us (managers in high-tech) about culture. I even [quoted them](https://github.com/kdeldycke/awesome-engineering-team-management/commit/de3e64647c911f78a37b3e54c7e46197acb061e1) in my [awesome list on engineering team management](https://github.com/kdeldycke/awesome-engineering-team-management#readme). 👨‍💼

HP Inc., the company, sucks. At least their printer division's business model. They recently pushed a **firmware update to ban third-party compatible ink cartridges**. 💔

The timeline is straightforward:

* 2020, March: general lockdown. 🦠 I need a home office. SO is a scientist and spend her time printing papers for review. Got her an [HP Color LaserJet M254dw](https://amzn.com/B073R2WVKB/?tag=kevideld-20) to keep her productive workflow ([publish or perish!](https://en.wikipedia.org/wiki/Publish_or_perish)).

* 2020, October: HP release a new firmware (versioned `20201021`).

  ![](/uploads/2020/hp-laserjet-printer-20201021-firmware.jpg)

* 2020, November: my printer auto-upgrade. I'm welcomed with this *Supply Problem [Screen of Death](https://en.wikipedia.org/wiki/Screen_of_death)*:

  ![](/uploads/2020/hp-laserjet-printer-supply-problem-screen-of-death.jpg)

  I can't print anymore. 🤯
  
Eight months. My printer worked for only 8 months. 😤

OK. It's my fault. I should have spent more money buying certified™ gear. 😑

![](https://comdoc.com/wp-content/uploads/2019/01/copier-printer-meme-03.jpg)

The solution is to travel back in time when things were working just great, and downgrade to the previous firmware.

## Disable auto-upgrade

We will start by stopping this madness for good, and prevent the printer from downloading a firmware behind our back.

In the control panel, go to `Setup` > `Service` > `LaserJet Update` > `Manage Updates`:

![](/uploads/2020/hp-laserjet-printer-manage-updates-menu.jpg)

Then set these options:

* Allow Downgrade: `Yes`
* Check Automatically: `Off`
* Prompt Before Install: `Always Prompt`
* Allow Updates: `No`

I'm quite surprised downgrades are allowed. 🤔 It seems out of character. Therefor, with my *Evil Product Manager* hat, I advise HP to monetize this feature under a monthly Enterprise Subscription of sort. 😈

## Download old firmware

I got lucky and found the previous `20200612` firmware referenced in [`https://ftp.hp.com/pub/networking/software/pfirmware/pfirmware.glf`](https://ftp.hp.com/pub/networking/software/pfirmware/pfirmware.glf).

There you'll get a direct link to the `.rfu` file (Remote Firmware Update):[`http://ftp.hp.com/pub/networking/software/pfirmware/HP_Color_LaserJet_Pro_M254_dw_Printer_series_20200612.rfu`](http://ftp.hp.com/pub/networking/software/pfirmware/HP_Color_LaserJet_Pro_M254_dw_Printer_series_20200612.rfu).

And just in case it disappear from its original location, here is a [copy of `HP_Color_LaserJet_Pro_M254_dw_Printer_series_20200612.rfu`](/uploads/2020/HP_Color_LaserJet_Pro_M254_dw_Printer_series_20200612.rfu).

The checksum of that file is:

```shell-session
$ sha256sum ./HP_Color_LaserJet_Pro_M254_dw_Printer_series_20200612.rfu
91c7f51ceba2386f3b94dcb9da20c669ab10b1ee3a9b1e1f742c40091920188e
```

## Downgrade firmware

Once you get the `.rfu` file, list all your printers from a macOS terminal:

```shell-session
$ lpstat -p -d
printer HP_Color_LaserJet_M254dw_0 is idle.  enabled since Fri Nov  6 17:47:06 2020
system default destination: HP_Color_LaserJet_M254dw_0
```

And run the firmware downgrade CLI:

```shell-session
$ lpr -P HP_Color_LaserJet_M254dw_0 /Users/kde/Downloads/HP_Color_LaserJet_Pro_M254_dw_Printer_series_20200612.rfu
```

Nothing gets printed to the console.

I don't know what happens here but it seems the `.rfu` file is pushed to the printer's queue and then gets consumed as any other printable document. See, [the RFU file format is a matryoshka doll](https://www.jsof-tech.com/unpacking-hp-firmware-updates-part-1/) embedding printing commands, encoded data and raw NAND code.

After a minute  or two, the printers reboots and upgrades itself:

![](/uploads/2020/hp-laserjet-printer-firmware-updating.jpg)

And we're back in business! 🥳

A detour via `Setup` > `Service` > `Firmware Datecode` menu confirm we're running the the previous firmware:

![](/uploads/2020/hp-laserjet-printer-20200612-firmware.jpg)

## Printer security

In my research for this article, I found out about [PRET, a printer exploitation toolkit](https://github.com/RUB-NDS/PRET). It's a brilliant tool, in a malignant way. It allows for pen-testing and hacking, using the same vectors as the firmware update. 🤫

I'll probably play with it in the future. For fun, but also to try enhance the security of the printer. In the mean time, I guess a password is the bare minimum. And if my printer get kidnapped by a cyber gang, I now have a way to restore my printer's firmware! 😬
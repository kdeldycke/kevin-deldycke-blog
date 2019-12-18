---
date: 2019-12-18
title: How-to Unlock, Root and Upgrade a Sony Xperia E3
category: English
tags: Android, Smartphone, Sony, ROM, bootloader, brew, fastboot, adb, macOS
---

Got hold of a second-hand [Sony Xperia E3](https://en.wikipedia.org/wiki/Sony_Xperia_E3) a couple of weeks ago and was surprised by its general build quality and IPS screen for a 2014 phone.

Of course it was loaded with crapware and bloatware both from the ISP and manufacturer.

Time to get my hands dirty back in the Android ecosystem, and try to clean that up.

This process was tested with the following devices:

* Sony Xperia E3, D2203 model, LTE, with stock firmware and OS (Android Kitkat 4.4.2)
* MacBook Air (macOS 10.14 Mojave)


## Factory Reset

First things first, let's clean up that phone using the standard functions:

1. Connect to local wifi.

1. Update phone's stock firmware, OS and apps using Sony's *Update Center*.

1. Format the attached SD card if any to destroy previous user's personal data.

1. Factory reset the phone.


## Unlock Bootloader

Phone was locked, tied to an Orange contract. Sony's got all the services online to properly unlock the phone, and the warranty has been expired for a long time. So let's proceed!

1. Enter service mode by dialing `*#*#7378423#*#*` on the phone.

1. Go to `Service info` > `Configuration` > `Rooting Status` 

1. There, the presence of the `Bootloader unlock allowed: Yes` status confirm the phone is currently locked but alloed to be unlocked.

1. Dial `*#06#` on the phone to get its IMEI unique ID. Note that number somewhere.

1. Go to [Sony developer website to obtain an unlock code](https://developer.sony.com/develop/open-devices/get-started/unlock-bootloader).

1. Follow the procedure on that site, and enter your phone's IMEI to get an unlock key. Write it down.

There are several ways of feeding that key to the phone. My method here describe how I performed it under macOS (10.14 Mojave in my case).

1. It starts by activating the developer mode. On the phone, go to phone's `Settings` app > `About phone` and at the bottom click 7 times on the `Build number` item. Developer mode has been unlocked once you see the `You are now a developer` message.

1. Then you can enable it back in the `Settings` > `System` > `Developer options` menu.

1. There, check the `Developer option` toggle button is set to `ON`.

1. We're now going to [activate USB access with CLI tools](https://www.kingoapp.com/root-tutorials/how-to-enable-usb-debugging-mode-on-android.htm). Scroll down in the menu to find the `Debugging` item, and enable the `USB debugging` option.

1. On a macOS terminal, [install Homebrew](https://docs.brew.sh/Installation):

    ```
    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    ```
    
1. Now install Android tools with Homebrew from the terminal:

    ```
    $ brew install android-platform-tools
    ```

1. Plug the phone to your computer with a micro USB cable.

1. Check your device is recognized by `adb`:

	```
	$ adb devices
	List of devices attached
	BL4828DXXXXX	device
    ```

1. Reboot device in bootloader mode:

	```
	$ adb reboot bootloader
    ```

1. Unlock the device with the unlock key previously fetched from Sony online service:

	```
	$ fastboot oem unlock 0x0828XXXXXXXXXXXX
    ```

1. Reboot the device in standard mode:

	```
	$ fastboot reboot
	```

1. Go back to service mode (dial `*#*#7378423#*#*`; go to `Service info` > `Configuration` > `Rooting Status`) and confirm the `Bootloader unlock : Yes` status. If so, your phone is now unlocked!

All the steps above have been performed with the stock ecosystem: firmware, ROM and OS are all standard. Now we will delves into the dark side.


## Root Phone

We'll now root the phone.

1. Get a microSD card and insert it in the phone.

1. Format the external SD card from the phone.

1. Unmount SD card from the phone.

1. Remove the card from the phone.

1. Plug card to your computer.

1. Download [King Root](https://kingroot.net) for Android (v5.3.7 in my case).

1. Copy the `.apk` file to the SD card.

1. Unmount and remove the card from the computer.

1. Insert back the SD card in the phone, and mount it.

1. In `Settings` > `Security` menu, allow applications to be installed from unknown sources.

1. Connect to wifi, go to Google Play store and install a file browser. My personal favorite: [Amaze File Manager](https://play.google.com/store/apps/details?id=com.amaze.filemanager).

1. Use the file manager to browse into the SD card, [find the APK, install it and run KingRoot](https://kingroot.net/tutorials).


## Flash Custom Recovery

The custom ROM I'll provide here only targets Sony Xperia E3 D2203 LTE model with the stock 4.4.2 Android.

Before proceeding anyfurther, please double check your device is the right one, with the expected versions. If not you're at risk of bricking your device for good.

1. It was hard to find an appropriate ROM so [here is a copy of the `boot_D2203_4.4.2.img` file](../uploads/2019/boot_D2203_4.4.2.img). I originally found it on an article on [*How to Install Custom Recovery on Sony Xperia E3*](https://consumingtech.com/how-to-install-a-custom-recovery-on-the-sony-xperia-e3/), and the [image itself is hosted on MediaFire](http://www.mediafire.com/file/627epe7817tolaf/boot_D2203_4.4.2.img/file).

 	It is a CMW-based Recovery v6.0.4.7 uniquely built for the D2203 LTE model.

	Download it and compare its checksum:

	```
	$ wget -P ~/Downloads/ http://download1582.mediafire.com/d8vmcjzc4xfg/627epe7817tolaf/boot_D2203_4.4.2.img
	(...)

	$ sha1sum ~/Downloads/boot_D2203_4.4.2.img 
	7fdf48efa91167ee20282b6595e11fe5afef72f2  boot_D2203_4.4.2.img
	```

1. Make sure the phone is plugged into your computer, and reboot the device in bootloader mode:

	```
	$ adb devices
	List of devices attached
	BL4828DXXXXX	device
	$ adb reboot bootloader
    ```

1. Flash the custom ROM:

	```
	$ fastboot flash boot ~/Downloads/boot_D2203_4.4.2.img
	```
	
	Here you might stumble upon the following error:
	
	```
	Writing 'recovery' FAILED (remote: 'partition table doesn't exist')
	```
	
	If that the case it's because you tried to flash the ROM into the recovery partition (as generally advised in most tutorials out there), with a command similar to:
	
	```
	$ fastboot flash recovery boot.img
	```
	
	This doesn't cut it: as [*foxite* explained in 2016](https://forum.xda-developers.com/showpost.php?s=875aad126d132fea99ba9cee073c67ed&p=68056829&postcount=3), the custom ROM provided here targets the boot partition.
	
1. Now reboot the device:

	```
	$ fastboot reboot
	```
	
1. The boot process should be eventless, as if nothing happened.

1. But if you reboot your device once more, you'll notice a slight difference.

	When the Sony Xperia logo show up, at the very start of the boot process, the front notification LED is turned on for a couple of seconds while the phone briefly vibrate.
	
	But if at that moment you press alternatively the `Up` and `Down` volume buttons a couple of times, you'll boot into the custom recovery ROM you just flashed:
	
	![](../uploads/2019/sony-xperia-e3-d2203-lte-cmw-recovery.jpg)
	
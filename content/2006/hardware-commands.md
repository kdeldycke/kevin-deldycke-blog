---
date: '2006-12-06'
title: Hardware commands
category: English
tags: CLI, gpart, Hardware, HDD, kernel, Linux, MBR, partitions, X.org, gphoto, DSLR, Canon EOS 7D, dmidecode, printer, CUPS, smartmontools, NTFS
---

## Computer

- Get Mac hardware model:

  ```shell-session
  $ sudo dmidecode -s system-product-name
  MacBookAir5,2
  ```

## Disk

- Show all S.M.A.R.T. info of a disk:

  ```shell-session
  $ smartctl -a /dev/ada4
  ```

- Low-level format of the `hda` device:

  ```shell-session
  $ dd if=/dev/zero of=/dev/hda
  ```

- Same as above but for paranoïd, as random bits will be written 3 times before performing the "low-level format" (i.e. writting zeros):

  ```shell-session
  $ shred --verbose --force --iterations=3 --zero /dev/hda
  ```

## Partitions

- Remove the MBR:

  ```shell-session
  $ dd if=/dev/null of=/dev/hda bs=446 count=1
  ```

- Restore the original Windows MBR:

  ```shell-session
  $ apt-get install mbr
  $ install-mbr -i n -p D -t 0 /dev/hda
  ```

- Guess the partition table of a device, including damaged ones:

  ```shell-session
  $ gpart -v /dev/md0
  ```

- Search for a Linux partition:

  ```shell-session
  $ sudo fdisk -d /dev/disk0 | cut -d ',' -f 3 | grep --quiet "0x83"
  $ if [[ $? -ne 0 ]]; then
  >     echo "No Linux partition found."
  > else
  >     echo "Linux partition found."
  > fi
  ```

- Mount an NTFS partition:

  ```shell-session
  $ sudo ntfs-3g /dev/disk4s2 ./usb-hdd -o local -o allow_other -o auto_xattr -o auto_cache
  ```

- Extract the content of an [Apple Disk Image](https://en.wikipedia.org/wiki/Apple_Disk_Image) `.dmg` file and access its content:

  ```shell-session
  $ dmg2img ./my-package.dmg
  $ mount -t hfsplus -o loop ./my-package.img /media/my-mount-point
  ```

## Keyboard

- Change the keyboard layout in Debian (don't forget to logoff and logon to activate the new setting):

  ```shell-session
  $ dpkg-reconfigure keyboard-configuration
  ```

- X.orgs' configuration (`~/.Xmodmap`) to remap function and command keys of a Mac keyboard ([source](https://github.com/kdeldycke/dotfiles/blob/cc9d00879f14036498615067349f1d75fcd96bf5/dotfiles-linux/.Xmodmap#L10-L24)):

  ```
  ! --- Remove Cmd keys
  ! Remaps the keys (reading left-to-right):
  !    -FROM-
  !  Fn Control_L Alt_L Super_L Space Super_R Alt_R
  !    -TO-
  !  Fn Control_L Alt_L Alt_L Space Alt_R Alt_R
  !
  keycode 133 = Alt_L Meta_L Alt_L Meta_L
  keycode 134 = ISO_Level3_Shift
  clear Mod1
  clear Mod4
  clear Mod5
  add Mod1 = Alt_L Alt_R Meta_L
  add Mod4 = Super_L Super_R Super_L Hyper_L
  add Mod5 = ISO_Level3_Shift Mode_switch
  ```

## Trackpad

- X.orgs' configuration (`~/.Xmodmap`) to either set natural or reverse scrolling for Mac trackpads ([source](https://github.com/kdeldycke/dotfiles/blob/cc9d00879f14036498615067349f1d75fcd96bf5/dotfiles-linux/.Xmodmap#L1-L4)):

  ```
  ! --- Reverse Scrolling
  !pointer = 1 2 3 5 4 6 7 8 9 10 11 12 13 14 15
  ! --- Natural Scrolling
  pointer = 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
  ```

- To add touchpad kernel support, add the following option to kernel at boot time:

  ```shell-session
  $ psmouse.proto=imps
  ```

- Sometimes, depending of the laptop I use, the mouse pointer disappear from the screen when I plug a VGA cable to a projector. In this case, I resort to a ++ctrl+alt+f1++, then I login as a normal user and finally I start a new X session:

  ```shell-session
  $ startx -- :1
  ```

## Camera

- Get the number of shutter count of a DSLR (Canon EOS 7D in my case):

  ```shell-session
  $ gphoto2 --get-config /main/status/shuttercounter
  Label: Shutter Counter
  Type: TEXT
  Current: 49238
  ```

## Printer

- List printers:

  ```shell-session
  $ lpstat -p -d
  printer HP_Color_LaserJet_M254dw_0 is idle.  enabled since Fri Nov  6 17:47:06 2020
  system default destination: HP_Color_LaserJet_M254dw_0
  ```

  ```shell-session
  $ lpq
  HP_Color_LaserJet_M254dw_0 is ready and printing
  Rank    Owner   Job     File(s)                         Total Size
  1st     kde     209     (stdin)                         0 bytes
  active  kde     211     HP_Color_LaserJet_Pro_M254_dw_P 33557504 bytes
  2nd     kde     212     HP_Color_LaserJet_Pro_M254_dw_P 33557504 bytes
  3rd     kde     213     HP_Color_LaserJet_Pro_M254_dw_P 33557504 bytes
  ```

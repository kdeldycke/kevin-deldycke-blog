---
date: 2020-10-27
title: TrueNAS Configuration and Maintenance
category: English
tags: hardware, NAS, filesystem, OS, FreeNAS, TrueNAS, hdd, hard-drive, ssd, raid, storage, network, ZFS, disk, package manager
---

A collection of personal notes on the setup, configuration and maintenance of a home-office TrueNAS appliance.

## 🖥 Hardware

I dedicated a whole post on [building the machine](https://kevin.deldycke.com/2020/05/nas-hardware/), in which you'll get the detailed bill of material, cost breakdown and parts selection process.

## 📊 Reports

### Disk Temperature

⚠️ Do not activate any aggressive power-management parameters on disks. This is the main reasons temperatures are not reported in graphs.

## 📦 Package Management

To prevent the administrator to mess up with TrueNAS install, FreeBSD's package management has been locked down. Installing a package does not work:

```{.shell-session hl_lines="6"}
root@truenas[/]# pkg install dmg2img
Updating local repository catalogue...
pkg: file:///usr/ports/packages/meta.txz: No such file or directory
repository local has no meta file, using default settings
pkg: file:///usr/ports/packages/packagesite.txz: No such file or directory
Unable to update repository local
Error updating repositories!
```

If you know what you're doing and want to unlock package management, here is the fix:

```shell-session
root@truenas[/]# sed -i .orig 's/enabled: yes/enabled: no/' /usr/local/etc/pkg/repos/local.conf
root@truenas[/]# sed -i .orig 's/enabled: no/enabled: yes/' /usr/local/etc/pkg/repos/FreeBSD.conf
```

Now you're ready to update the package index:

```{.shell-session hl_lines="6"}
root@truenas[/]# pkg update
Updating FreeBSD repository catalogue...
Fetching meta.conf: 100%    163 B   0.2kB/s    00:01
Fetching packagesite.txz: 100%    6 MiB   6.7MB/s    00:01
Processing entries: 100%
FreeBSD repository update completed. 31953 packages processed.
All repositories are up to date.
```

And install your package:

```shell-session
root@truenas[/]# pkg install dmg2img
Updating FreeBSD repository catalogue...
FreeBSD repository is up to date.
All repositories are up to date.
New version of pkg detected; it needs to be installed first.
The following 1 package(s) will be affected (of 0 checked):

Installed packages to be UPGRADED:
	pkg: 1.14.6 -> 1.15.10 [FreeBSD]

Number of packages to be upgraded: 1

The operation will free 31 MiB.
7 MiB to be downloaded.

Proceed with this action? [y/N]: y
[1/1] Fetching pkg-1.15.10.txz: 100%    7 MiB   6.9MB/s    00:01
Checking integrity... done (0 conflicting)
[1/1] Upgrading pkg from 1.14.6 to 1.15.10...
[1/1] Extracting pkg-1.15.10: 100%
Updating FreeBSD repository catalogue...
FreeBSD repository is up to date.
All repositories are up to date.
The following 1 package(s) will be affected (of 0 checked):

New packages to be INSTALLED:
	dmg2img: 1.6.7 [FreeBSD]

Number of packages to be installed: 1

22 KiB to be downloaded.

Proceed with this action? [y/N]: y
[1/1] Fetching dmg2img-1.6.7.txz: 100%   22 KiB  22.5kB/s    00:01
Checking integrity... done (0 conflicting)
[1/1] Installing dmg2img-1.6.7...
[1/1] Extracting dmg2img-1.6.7: 100%

root@truenas[/]# dmg2img

dmg2img v1.6.7 (c) vu1tur (to@vu1tur.eu.org)

Usage: dmg2img [-l] [-p N] [-s] [-v] [-V] [-d] <input.dmg> [<output.img>]
or     dmg2img [-l] [-p N] [-s] [-v] [-V] [-d] -i <input.dmg> -o <output.img>

Options: -s (silent) -v (verbose) -V (extremely verbose) -d (debug)
         -l (list partitions) -p N (extract only partition N)
```

## 🐛 Issues

### FreeNAS to TrueNAS migration

I wrote a long article on [how to migrate an encrypted pool from FreeNAS to TrueNAS](https://kevin.deldycke.com/2020/12/migration-from-freenas-to-truenas/).

### Unreachable Network due to Multiple NICs

My machine was regularly disconnected from the network and couldn't be cleanly rebooted. This started under `FreeNAS 11.3-U4.1` and is still reproducible with a fresh `TrueNAS 12.0`.

The issue lies somewhere in all connected interfaces being granted DHCP active service:

https://www.youtube.com/watch?v=vDMooVj-flM

The [issue is being discussed on iXsystems' JIRA](https://jira.ixsystems.com/browse/NAS-108043).

### `ValidateUpdate` error on upgrade

Got the following error on upgrade?

```pytb
PermissionError: [Errno 13] Permission denied: './ValidateUpdate'
```

The fix: temporary [switch the System Dataset](https://www.truenas.com/docs/hub/tasks/advanced/system-dataset/) to `freenas-boot`. Your default system dataset is probably set to your ZFS pool which might be unavailable for whatever reason. In my case, I was in the middle of a [pool migration process](https://kevin.deldycke.com/2020/12/migration-from-freenas-to-truenas/).
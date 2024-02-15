---
date: '2012-05-08'
title: VirtualBox commands
category: English
tags: disk, image, VirtualBox, virtualization
---

- Clone a virtual disk image:

  ```shell-session
  $ VBoxManage clonehd original-disk.vdi copy.vdi
  ```

- Resize a virtual disk image to 20 Gb:

  ```shell-session
  $ VBoxManage modifyhd disk.vdi --resize 20000
  ```

- Convert a VirtualBox image to a raw image:

  ```shell-session
  $ VBoxManage clonehd --format RAW disk.vdi disk.raw
  ```

- Convert a raw image to a VirtualBox image:

  ```shell-session
  $ VBoxManage convertdd disk.raw disk.vdi --format VDI
  ```

- List virtual machines:

  ```shell-session
  $ VBoxManage list vms
  ```

- Fix broken NAT ([source](https://askubuntu.com/questions/216865/vitualbox-nat-stopped-working-after-ubuntu-upgrade-to-12-10)):

  ```shell-session
  $ VBoxManage modifyvm "name" --natdnshostresolver1 on
  $ VBoxManage modifyvm "name" --natdnsproxy1 on
  ```

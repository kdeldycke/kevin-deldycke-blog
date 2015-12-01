---
date: 2013-03-20 12:25:36
title: libvirt commands
category: English
tags: CLI, Linux, libvirt, QEMU, virtual machine

List system virtual machines:

    :::bash
    $ virsh -c qemu:///system list --all

List session VMs:

    :::bash
    $ virsh -c qemu:///session list --all

Dump a VM configuration to XML file:

    :::bash
    $ virsh -c qemu:///system dumpxml vm-name > vm-name-conf.xml

Create a new VM by importing its XML configuration:

    :::bash
    $ virsh -c qemu:///system define vm-name-conf.xml


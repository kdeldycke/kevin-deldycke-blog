comments: true
date: 2011-05-17 12:13:04
layout: post
slug: setting-hdds-smart-monitoring-debian-squeeze
title: Setting up HDD's SMART monitoring on Debian Squeeze
wordpress_id: 3169
category: English
tags: Debian, HDD, Linux, Server, smartmontools, squeeze

Here is how I setup SMART monitoring and maintenance of an array of Hard-Disk Drives running a Debian Squeeze.

First, let's install the `smartmontools` package:


    :::console
    $ aptitude install smartmontools




We now have to check that SMART is activated on our drives:


    :::console
    $ smartctl -a /dev/sdb | grep "SMART support is: Enabled"
    $ smartctl -a /dev/sdc | grep "SMART support is: Enabled"
    $ smartctl -a /dev/sdd | grep "SMART support is: Enabled"
    $ smartctl -a /dev/sde | grep "SMART support is: Enabled"




Nowadays all modern drives are already activated in factories. But in case they're not you can activate this feature with the following command:


    :::console
    $ smartctl -s on -a /dev/sdb




Now we have to activate the `smartd` daemon, and let it start automatically when the machine boot:


    :::console
    $ sed -i 's/#start_smartd=yes/start_smartd=yes/g'                           /etc/default/smartmontools
    $ sed -i 's/#smartd_opts="--interval=1800"/smartd_opts="--interval=1800"/g' /etc/default/smartmontools




For some reason, I prefer to not let `smartd` select by itself drives it should check. Here is how to deactivate the auto-detection:


    :::console
    $ sed -i 's/^DEVICESCAN /#DEVICESCAN /g' /etc/smartd.conf




Now let's specify by hand the way our drives should be monitored and maintained. Here are the lines I added to `/etc/smartd.conf`:


    :::text
    /dev/sdb -a -o on -S on -s (S/../.././02|L/../../6/03) -m user@example.com
    /dev/sdc -a -o on -S on -s (S/../.././04|L/../../6/05) -m user@example.com
    /dev/sdd -a -o on -S on -s (S/../.././06|L/../../6/07) -m user@example.com
    /dev/sde -a -o on -S on -s (S/../.././08|L/../../6/09) -m user@example.com




Finally, we need to restart the SMART service to take into account all our changes:


    :::text
    $ /etc/init.d/smartmontools restart


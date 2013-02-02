date: 2010-02-28 12:39:32
title: System & Shell commands
category: English
tags: CLI, echo, kernel, Linux, nohup, shell, system

  * Run a process detached to the current terminal:

        :::bash
        $ nohup my_command &

  * Run a process with a shell for a system user which has none (i.e. its default shell is set to `/bin/false` in `/etc/passwd`):

        :::bash
        $ su sys_user -s /bin/bash -c "my_command"

  * Get the exit code of the latest runned command:

        :::bash
        $ echo $?

  * Run the last command as `root` ([source](http://blog.hardikr.com/post/2337320222/sudo-previous-command)):

        :::bash
        $ sudo !!

  * Show the user under which I'm currently logged in:

        :::bash
        $ whoami

  * List cron jobs of the current user:

        :::bash
        $ crontab -l

  * If you have the following error:

        :::bash
        $ -bash: ./myscript.sh: /bin/bash^M: bad interpreter: No such file or directory

    Then the fix consist of removing the bad characters:

        :::bash
        $ sed -i 's/\r//' ./myscript.sh

  * Extract strings from a binary file:

        :::bash
        $ strings ./firmware.bin | less

  * Free up some memory by clearing RAM caches ([source](http://www.scottklarr.com/topic/134/linux-how-to-clear-the-cache-from-memory/)):

        :::bash
        $ sync ; echo 3 > /proc/sys/vm/drop_caches

  * Display which distro is running the system ([source](http://news.ycombinator.com/item?id=1973441)):

        :::bash
        $ lsb_release -a

    or

        :::bash
        $ cat /etc/lsb-release

  * List of most used commands:

        :::bash
        $ history | awk '{a[$2]++}END{for(i in a){print a[i] " " i}}' | sort -rn | head

  * Disable a service on Debian/Ubuntu, then re-enable it:

        :::bash
        $ update-rc.d my-service-name remove
        $ update-rc.d my-service-name defaults

  * Same thing as above but on a RedHat-like system:

        :::bash
        $ chkconfig sshd --del
        $ chkconfig sshd --add


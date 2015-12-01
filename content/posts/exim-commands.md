---
date: 2010-07-28 11:54:54
title: Exim commands
category: English
tags: CLI, email, Exim, Linux, Mail transfer agents
---

  * List mails in the queue:

        :::bash
        $ exim -bp

  * View headers of a mail:

        :::bash
        $ exim -Mvh <mail-id>

  * View body of a mail:

        :::bash
        $ exim -Mvb <mail-id>

  * Remove a mail from the queue:

        :::bash
        $ exim -Mrm <mail-id>

  * Remove all frozen mails in the queue:

        :::bash
        $ exiqgrep -z -i | xargs exim -Mrm


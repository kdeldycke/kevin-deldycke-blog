comments: true
date: 2010-07-28 11:54:54
layout: post
slug: exim-commands
title: Exim commands
wordpress_id: 1617
category: English
tags: CLI, E-mail, Exim, Linux, Mail transfer agents




  * List mails in the queue:

    
    :::console
    exim -bp
    






  * View headers of a mail:

    
    :::console
    exim -Mvh <mail-id>
    






  * View body of a mail:

    
    :::console
    exim -Mvb <mail-id>
    






  * Remove a mail from the queue:

    
    :::console
    exim -Mrm <mail-id>
    






  * Remove all frozen mails in the queue:

    
    :::console
    exiqgrep -z -i | xargs exim -Mrm
    







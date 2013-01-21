comments: true
date: 2011-11-08 12:20:19
layout: post
slug: gpg-commands
title: GPG commands
wordpress_id: 3560
category: English
tags: CLI, cryptography, GPG, Linux, security




  * Generate a key (interactive mode):

    
    :::console
    gpg --gen-key
    






  * You can use the key generator in an unattended mode. Values in the example below are the same as the defaults proposed in the interactive mode above. Parameters in comments are there for reference:

    
    :::console
    gpg --gen-key --batch <<EOF
    Key-Type: RSA
    Key-Length: 2048
    Subkey-Type: RSA
    Subkey-Length: 2048
    Expire-Date: 0
    Name-Real: Kevin
    # Name-Email: kevin@deldycke.com
    # Name-Comment: My auto-generated key
    # Passphrase: my_secret_passphrase
    EOF
    






  * List available keys for the current user:

    
    :::console
    gpg --list-keys
    






  * Decrypt a file:

    
    :::console
    gpg --decrypt archive.001.tar.gpg --output archive.001.tar
    






  * Same as above but for a collection of files:

    
    :::console
    gpg --multifile --decrypt archive.*.tar.gpg
    







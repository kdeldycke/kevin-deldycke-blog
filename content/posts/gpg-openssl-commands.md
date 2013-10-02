date: 2011-11-08 12:20:19
title: GPG & OpenSSL commands
category: English
tags: CLI, cryptography, GPG, Linux, security, OpenSSL, SSL, RSA

  * Generate a random password:

        :::bash
        $ openssl rand -base64 18

  * Generate a key (interactive mode):

        :::bash
        $ gpg --gen-key

  * You can use the key generator in an unattended mode. Values in the example below are the same as the defaults proposed in the interactive mode above. Parameters in comments are there for reference:

        :::bash
        $ gpg --gen-key --batch <<EOF
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

        :::bash
        $ gpg --list-keys

  * Decrypt a file:

        :::bash
        $ gpg --decrypt archive.001.tar.gpg --output archive.001.tar

  * Same as above but for a collection of files:

        :::bash
        $ gpg --multifile --decrypt archive.*.tar.gpg

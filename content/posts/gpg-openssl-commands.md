---
date: 2011-11-08 12:20:19
title: GPG & OpenSSL commands
category: English
tags: CLI, cryptography, GPG, Linux, security, OpenSSL, SSL, RSA
---

  * Generate a random password:

        ```shell-session
        $ openssl rand -base64 18
        ```

  *  Examine ASN.1 structure of a [CSR](https://en.wikipedia.org/wiki/Certificate_signing_request):

        ```shell-session
        $ openssl asn1parse -i -in ./0000_csr-certbot.pem
        ```

  * Generate a key (interactive mode):

        ```shell-session
        $ gpg --gen-key
        ```

  * You can use the key generator in an unattended mode. Values in the example below are the same as the defaults proposed in the interactive mode above. Parameters in comments are there for reference:

        ```shell-session
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
        ```

  * List available keys for the current user:

        ```shell-session
        $ gpg --list-keys
        ```

  * Decrypt a file:

        ```shell-session
        $ gpg --decrypt archive.001.tar.gpg --output archive.001.tar
        ```

  * Same as above but for a collection of files:

        ```shell-session
        $ gpg --multifile --decrypt archive.*.tar.gpg
        ```

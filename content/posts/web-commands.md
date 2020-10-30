---
date: 2010-03-26 17:08:36
title: Web commands
category: English
tags: certificate, CLI, HTML, KDE, konqueror, Linux, OpenSSL, RSA, SSL, wget, x509, Regular expression, MIME type, Media Type
---


## Scraping

  * Download a web page an all its requisites:

        ```shell-session
        $ wget -r -p -nc -nH --level=1 https://pypi.python.org/simple/python-ldap/
        ```

  * Create a PNG image of a rendered html page:

        ```shell-session
        $ kwebdesktop 1024 768 capture.png https://slashdot.org/
        ```


## Servers

  * Test that your site is sending gzipped content:

        ```shell-session
        $ curl -i -H "Accept-Encoding: gzip,deflate" https://kevin.deldycke.com 2>&1 | grep gzip
        ```

  * Ping some pages on internet to force our corporate proxy to refresh its internal cache:

        ```shell-session
        $ for EGG in BeautifulSoup PIL Plone; do wget --server-response -O /dev/null https://pypi.python.org/simple/$EGG/; done
        ```

  * Debug mysterious numbers ([source](https://news.ycombinator.com/item?id=22037088)):

        ```shell-session
        $ echo 'obase=16; 1195725856' | bc | xxd -r -ps | od -cb
        0000000   G   E   T
                107 105 124 040
        0000004
        ```


## Certificates

  * Create a minimal self-signed unencrypted SSL certificate without issuer information and a validity period of 10 years:

        ```shell-session
        $ openssl req -x509 -nodes -subj '/' -days 3650 -newkey rsa:2048 -keyout self-signed.pem -out self-signed.pem
        ```

  * Create a pair of SSL self-signed certificate and (unencrypted) private key ([source](https://devsec.org/info/ssl-cert.html)):

        ```shell-session
        $ openssl genrsa -out private.key 2048
        $ openssl req -new -subj '/' -key private.key -out certreq.csr
        $ openssl x509 -req -days 3650 -in certreq.csr -signkey private.key -out self-signed.pem
        $ rm certreq.csr
        ```

  * View certificate details:

        ```shell-session
        $ openssl x509 -noout -text -in self-signed.pem
        ```

  * Fetch from a website its first certificate of the chain:

        ```shell-session
        $ openssl s_client -connect imap.gmail.com:993 -showcerts 2>&1 < /dev/null | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' | sed -ne '1,/-END CERTIFICATE-/p' > ~/gmail.pem
        ```

  * Fetch the certificate from a website (the one returned is the last of the chain):

        ```shell-session
        $ openssl s_client -connect imap.gmail.com:993 -showcerts 2>&1 < /dev/null | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' | tac | sed -ne '1,/-BEGIN CERTIFICATE-/p' | tac > ./google.pem
        ```


## MIME type

  * List all the diferrent [media types (formerly known as MIME types)](https://www.iana.org/assignments/media-types/media-types.xhtml) of all the files in the `www` folder:

        ```shell-session
        $ find ./www -type f -exec file --mime-type -b "{}" \; | sort | uniq
        ```


## Markup

  * Search non-breakable spaces that doesn't end with a semicolon:

        ```shell-session
        $ grep -RIi --extended-regexp '&nbsp[^;]' ./
        ```

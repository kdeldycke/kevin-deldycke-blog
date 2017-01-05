---
date: 2010-03-26 17:08:36
title: Web commands
category: English
tags: certificate, CLI, HTML, KDE, konqueror, Linux, OpenSSL, RSA, SSL, wget, x509, Regular expression
---

  * Download a web page an all its requisites:

        :::bash
        $ wget -r -p -nc -nH --level=1 https://pypi.python.org/simple/python-ldap/

  * Test that your site is sending gzipped content:
 
        :::bash
        $ curl -i -H "Accept-Encoding: gzip,deflate" https://kevin.deldycke.com 2>&1 | grep gzip

  * List all the diferrent MIME types of all the files in the `www` folder:

        :::bash
        $ find ./www -type f -exec mimetype -b "{}" \; | sort | uniq

  * Create a PNG image of a rendered html page:

        :::bash
        $ kwebdesktop 1024 768 capture.png https://slashdot.org/

  * Search in all files malformed HTML entities (in this case non-breakable spaces that doesn't end with a semicolon):

        :::bash
        $ grep -RIi --extended-regexp '&nbsp[^;]' ./

  * Here is a one-liner I use to ping some pages on internet to force our corporate proxy to refresh its internal cache:

        :::bash
        $ for EGG in BeautifulSoup PIL Plone; do wget --server-response -O /dev/null https://pypi.python.org/simple/$EGG/; done

  * Create a minimal self-signed unencrypted SSL certificate without issuer information and a validity period of 10 years:

        :::bash
        $ openssl req -x509 -nodes -subj '/' -days 3650 -newkey rsa:2048 -keyout self-signed.pem -out self-signed.pem

  * Create a pair of SSL self-signed certificate and (unencrypted) private key ([source](https://devsec.org/info/ssl-cert.html)):

        :::bash
        $ openssl genrsa -out private.key 2048
        $ openssl req -new -subj '/' -key private.key -out certreq.csr
        $ openssl x509 -req -days 3650 -in certreq.csr -signkey private.key -out self-signed.pem
        $ rm certreq.csr

  * View certificate details:

        :::bash
        $ openssl x509 -noout -text -in self-signed.pem

  * Fetch from a website its first certificate of the chain:

        :::bash
        $ openssl s_client -connect imap.gmail.com:993 -showcerts 2>&1 < /dev/null | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' | sed -ne '1,/-END CERTIFICATE-/p' > ~/gmail.pem

  * Fetch the certificate from a website (the one returned is the last of the chain):

        :::bash
        $ openssl s_client -connect imap.gmail.com:993 -showcerts 2>&1 < /dev/null | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' | tac | sed -ne '1,/-BEGIN CERTIFICATE-/p' | tac > ./google.pem


---
date: 2006-05-01 00:19:53
title: How-to locally Disable Python CGI scripts.
category: English
tags: Apache, Linux, Python, Server, Web
---

Since the beginning of this blog, my collection of python scripts were not readable. This was due to the fact that files with `.py` extension are seen by the apache web server as CGI scripts. To tell apache that python files can be published as-is, put a `.htaccess` beside your files. Then edit it to add the following directive:

    ```apache
    RemoveHandler .py
    ```

That's all! This will let apache serve `.py` files as normal plain text files. [More info about RemoveHandler](https://httpd.apache.org/docs/1.3/mod/mod_mime.html.en#removehandler) can be found in official apache documentation.


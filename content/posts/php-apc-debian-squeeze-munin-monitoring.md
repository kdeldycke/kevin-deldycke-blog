comments: true
date: 2011-07-19 12:28:10
layout: post
slug: php-apc-debian-squeeze-munin-monitoring
title: PHP APC on Debian Squeeze with Munin monitoring
wordpress_id: 3269
category: English
tags: apx, Debian, Debian Squeeze, munin, nginx, PHP, Server, Web

Installing [APC](http://php.net/manual/en/book.apc.php) on Debian Squeeze is as simple as installing the package:

    :::bash
    $ aptitude install php5-apc

In my case this package come from the PHP bundle distributed by the [Dotdeb repository](http://www.dotdeb.org).

If installing APC is easy, monitoring it with Munin requires some extra manipulations. There is currently no good [APC plugin available on Munin Exhange](http://exchange.munin-monitoring.org/plugins/search?keyword=apc). So we'll use the external [munin-php-apc project](http://code.google.com/p/munin-php-apc/) instead.

The latter can't get APC statistics by itself: it need an extra PHP file to be served locally. As you can read in my previous article, [my Munin is powered by Nginx](http://kevin.deldycke.com/2011/06/munin-monitor-debian-squeeze-server/). So now we'll setup Nginx to serve this extra PHP file:

    :::bash
    $ mkdir -p /var/www/apc
    $ cd /var/www/apc
    $ wget http://munin-php-apc.googlecode.com/svn/trunk/php_apc/apc_info.php
    $ chown -R www-data:www-data /var/www/apc

Then I need to update my `/etc/nginx/sites-available/munin` file (see [details about this file on my previous article](http://kevin.deldycke.com/2011/06/munin-monitor-debian-squeeze-server/)) to have the second `server` section look like this:

    :::nginx
    server {
      server_name localhost;
      include /etc/nginx/php.conf;
      root /var/www/apc;
      allow 127.0.0.1;
      deny all;
      location / {
        access_log off;
      }
      location /nginx_status {
        stub_status on;
        access_log off;
      }
    }

Here the included `/etc/nginx/php.conf` file is the one in which I've concentrate all the Nginx directives required to activate PHP file parsing. The content and the mechanism behind this file is describe in my [article on setting up Nginx with PHP-FPM](http://kevin.deldycke.com/2011/06/nginx-php-fpm-mysql-debian-squeeze-server/).

Let's get back to our Munin monitoring setup. I can restart now Nginx and check that I can access locally to my raw statistics:

    :::bash
    $ /etc/init.d/nginx reload
    $ wget http://localhost/apc_info.php
    $ wget http://localhost/nginx_status

The last step is to install and configure the Munin plugin:

    :::bash
    $ aptitude install libwww-perl
    $ wget http://munin-php-apc.googlecode.com/svn/trunk/php_apc/php_apc_ --output-document=/usr/share/munin/plugins/php_apc_
    $ chmod -R 755 /usr/share/munin/plugins/
    $ ln -s /usr/share/munin/plugins/php_apc_ /etc/munin/plugins/php_apc_usage
    $ ln -s /usr/share/munin/plugins/php_apc_ /etc/munin/plugins/php_apc_hit_miss
    $ ln -s /usr/share/munin/plugins/php_apc_ /etc/munin/plugins/php_apc_purge
    $ ln -s /usr/share/munin/plugins/php_apc_ /etc/munin/plugins/php_apc_fragmentation
    $ ln -s /usr/share/munin/plugins/php_apc_ /etc/munin/plugins/php_apc_files
    $ ln -s /usr/share/munin/plugins/php_apc_ /etc/munin/plugins/php_apc_rates
    $ echo "[php_apc_*]
    user root
    env.url http://localhost/apc_info.php?auto
    " > /etc/munin/plugin-conf.d/php_apc
    $ /etc/init.d/munin-node restart

And finally, after a while, you'll get those beautiful graphs:

![](/static/uploads/2011/06/php-apc-munin-graphs.png)


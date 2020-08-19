---
date: 2011-09-20 12:22:13
title: My Nginx + PHP-FPM + MySQL configuration
category: English
tags: Debian, Debian Squeeze, Linux, MySQL, SQL, nginx, ovh, PHP, php-fpm, Server, virtualization, Web, WordPress
---

This article is a follow-up to the one I wrote 3 months ago, in which I
explained how to [install a web stack based on Nginx, PHP-FPM and
MySQL](https://kevin.deldycke.com/2011/06/nginx-php-fpm-mysql-debian-squeeze-server/)
on a Debian Squeeze server. Now it's time to tune this basic install to get
some performance out of it.

![](/uploads/2011/ovh-vps-3-virtual-server.png)

The setup I'll detail below runs on an [OVH VPS](https://www.ovh.co.uk/vps/)
instance. This virtual server has 4 CPU cores at 1.5GHz, 1 Go RAM and 50 Gb
HDD.

I'm mostly running WordPress instances on that server, so you'll see some
reference of it in this post.

## MySQL

First, let's tune MySQL. That's the easiest part of that article, as you only
need to create a `.cnf` file in `/etc/mysql/conf.d/` and place there all your
custom parameters. Here is the content of my `/etc/mysql/conf.d/kev.cnf`:

    ```ini
    [mysqld]
    interactive_timeout = 50
    join_buffer = 1M
    key_buffer = 250M
    max_connections = 100
    max_heap_table_size = 32M
    myisam_sort_buffer_size = 96M
    query_cache_limit = 4M
    query_cache_size = 250M
    query_prealloc_size = 65K
    query_alloc_block_size = 128K
    read_buffer_size = 1M
    read_rnd_buffer_size = 768K
    sort_buffer_size = 1M
    table_cache = 4096
    thread_cache_size = 1024
    tmp_table_size = 32M
    wait_timeout = 500
    # Debug
    #general_log_file = /var/log/mysql/mysql.log
    #general_log = 1
    # InnoDBinnodb_buffer_pool_size = 256Minnodb_additional_mem_pool_size = 10Minnodb_log_file_size = 32Minnodb_flush_method = O_DIRECTinnodb_file_per_table = 1innodb_flush_log_at_trx_commit = 0
    [mysqld_safe]
    nice = -5
    open_files_limit = 8192

    [isamchk]
    key_buffer = 64M
    sort_buffer = 64M
    read_buffer = 16M
    write_buffer = 16M
    ```

Most of these parameters were set for my particular usage and with insights
from the [MySQL Tuning Primer
Script](https://launchpad.net/mysql-tuning-primer).

## PHP-FPM

Unlike MySQL, the structure of PHP configuration files on Debian Squeeze
doesn't let us easily add our customizations. We have to modify the default
files provided at the package installation.

Here is my setup of the PHP processes pool:

    ```diff
    --- /etc/php5/fpm/pool.d/www.conf.orig     2011-06-07 08:14:30.000000000 +0200
    +++ /etc/php5/fpm/pool.d/www.conf  2011-08-15 17:34:09.000000000 +0200
    @@ -237,3 +237,10 @@
     ;php_admin_value[error_log] = /var/log/fpm-php.www.log
     ;php_admin_flag[log_errors] = on
     ;php_admin_value[memory_limit] = 32M
    +
    +pm.max_children = 25
    +pm.start_servers = 4
    +pm.min_spare_servers = 2
    +pm.max_spare_servers = 10
    +pm.max_requests = 500
    +request_terminate_timeout = 30
    ```

The second customization I made is not about performances but convenience. It
just allow my WordPress' users to upload larger files:

    ```diff
    --- /etc/php5/fpm/php.ini.orig      2011-06-18 13:32:37.000000000 +0200
    +++ /etc/php5/fpm/php.ini   2011-06-22 22:50:49.000000000 +0200
    @@ -725,7 +725,7 @@

     ; Maximum size of POST data that PHP will accept.
     ; https://php.net/post-max-size
    -post_max_size = 8M
    +post_max_size = 15M

     ; Magic quotes are a preprocessing feature of PHP where PHP will attempt to
     ; escape any character sequences in GET, POST, COOKIE and ENV data which might
    @@ -876,7 +876,7 @@

     ; Maximum allowed size for uploaded files.
     ; https://php.net/upload-max-filesize
    -upload_max_filesize = 2M
    +upload_max_filesize = 15M

     ; Maximum number of files that can be uploaded via a single request
     max_file_uploads = 20
    ```

## Nginx

Let's say my Wordpress blog is installed in `/var/www/my_wordpress`. To let it
be served by Nginx, we add a configuration file for this site in
`/etc/nginx/sites-available/my_wordpress`:

    ```nginx
    server {
      server_name blog.example.com;
      root /var/www/my_wordpress/;
      include /etc/nginx/wordpress.conf;
      location /static {
        autoindex on;
      }
    }

    server {
      listen 80 default_server;
      server_name .example.com .example.org .example.net;
      rewrite ^ http://blog.example.com$request_uri? permanent;
    }
    ```

In the configuration above, you can see that I want my blog to be served at
`http://blog.example.com`. I also added some domain redirections in the form of
a second `server` section, and a way to better display my static file
repository by letting Nginx generate index pages.

Then don't forget to activate this site:

    ```shell-session
    $ ln -s /etc/nginx/sites-available/my_wordpress /etc/nginx/sites-enabled/
    ```

The file above refer to `/etc/nginx/wordpress.conf` which is where I place all
the configuration directives common to all the WordPress blogs on my server.
Here is the content of that file:

    ```nginx
    # This order might seem weird - this is attempted to match last if rules below fail.
    # See: https://wiki.nginx.org/HttpCoreModule
    location / {
      try_files $uri $uri/ /index.php?q=$uri&$args;
    }

    # Add trailing slash to */wp-admin requests.
    rewrite /wp-admin$ $scheme://$host$uri/ permanent;

    include global.conf;

    include php.conf;
    ```

Again, this file make a reference to `php.conf`, which is the same as [the one
featured in my previous
article](https://kevin.deldycke.com/2011/06/nginx-php-fpm-mysql-debian-squeeze-server/).
I only removed the `index` directive to place it elsewhere, and added a limit
on the number of PHP requests a client can make:

    ```nginx
    location ~ \.php$ {
      # Throttle requests to prevent abuse
      limit_req zone=antidos burst=5;

      # Zero-day exploit defense.
      # https://forum.nginx.org/read.php?2,88845,page=3
      # Won't work properly (404 error) if the file is not stored on this server, which is entirely possible with php-fpm/php-fcgi.
      # Comment the 'try_files' line out if you set up php-fpm/php-fcgi on another machine.  And then cross your fingers that you won't get hacked.
      try_files $uri =404;

      fastcgi_split_path_info ^(.+\.php)(/.+)$;
      include /etc/nginx/fastcgi_params;

      # As explained in https://kbeezie.com/view/php-self-path-nginx/ some fastcgi_param are missing from fastcgi_params.
      # Keep these parameters for compatibility with old PHP scripts using them.
      fastcgi_param PATH_INFO       $fastcgi_path_info;
      fastcgi_param PATH_TRANSLATED $document_root$fastcgi_path_info;
      fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;

      # Some default config
      fastcgi_connect_timeout        60;
      fastcgi_send_timeout          180;
      fastcgi_read_timeout          180;
      fastcgi_buffer_size          128k;
      fastcgi_buffers            4 256k;
      fastcgi_busy_buffers_size    256k;
      fastcgi_temp_file_write_size 256k;

      fastcgi_intercept_errors    on;
      fastcgi_ignore_client_abort off;

      fastcgi_pass 127.0.0.1:9000;
    }
    ```

Here is where the `index` directive moved: `/etc/nginx/conf.d/kev.conf`. I also
added there some tweaks and the global request throttling configuration:

    ```nginx
    # Hide Nginx version
    server_tokens off;

    # Set default index file names
    index index.php index.html index.htm;

    # Allow uploads up to 15 Mo
    client_max_body_size 15m;

    # Create a global request accounting pool to prevent DOS
    limit_req_zone $binary_remote_addr zone=antidos:10m rate=3r/s;
    ```

The `global.conf` file we saw in `/etc/nginx/wordpress.conf` refer to
`/etc/nginx/global.conf`, which contain additional measures to remove cruft
from log files and enhance security:

    ```nginx
    # Do not log excessive request on common web content like favicon and robots.txt
    location = /favicon.ico {
      log_not_found off;
      access_log off;
    }
    location = /robots.txt {
      allow all;
      log_not_found off;
      access_log off;
    }

    # Deny all attempts to access any dotfile (=hidden files) such as .htaccess, .htpasswd, .DS_Store, .directory, .svn, .git, ...
    location ~ /\. {
      deny all;
      access_log off;
      log_not_found off;
    }
    ```

All of default Nginx configuration can't be overridden by additional files. We
have to change `/etc/nginx/nginx.conf` itself:

    ```diff
    --- /etc/nginx/nginx.conf.orig   2011-06-06 00:46:56.000000000 +0200
    +++ /etc/nginx/nginx.conf        2011-08-15 17:44:58.000000000 +0200
    @@ -3,8 +3,9 @@
     pid /var/run/nginx.pid;

     events {
    -       worker_connections 768;
    -       # multi_accept on;
    +       use epoll;
    +       worker_connections 1024;
    +       multi_accept on;
     }

     http {
    @@ -16,7 +17,7 @@
            sendfile on;
            tcp_nopush on;
            tcp_nodelay on;
    -       keepalive_timeout 65;
    +       keepalive_timeout 3;
            types_hash_max_size 2048;
            # server_tokens off;
    ```

That's all for our customizations. We can now restart all our servers:

    ```shell-session
    $ /etc/init.d/mysql restart
    $ /etc/init.d/php5-fpm restart
    $ /etc/init.d/nginx restart
    ```

## Conclusion

I'm running my websties under this configuration for about 3 months and I'm really happy with the results. I'm sure I can push optimizations further, but it may require lots of time and effort compared to the marginal gain I'll get. My websites are responsive enough to me. And if they collapse in the future under the load of the Reddit crowd, I'll still have the option to move to a bigger virtual server (vertical scaling FTW!).

date: 2011-07-26 12:51:45
title: Lighttpd-powered WebDAVs server on Debian Squeeze
category: English
tags: Debian, Debian Squeeze, lighttpd, Linux, OpenSSL, Server, SSL, Web, WebDAV, RSA

Here is a tiny article about how I used [Lighttpd](http://www.lighttpd.net) to serve content over [WebDAV](http://wikipedia.org/wiki/WebDAV).

First, install the required packages:

    :::bash
    $ aptitude install lighttpd-mod-webdav

As we want to provide a secure WebDAV access, we need to install [OpenSSL](http://www.openssl.org):

    :::bash
    $ aptitude install openssl

Then we create the file `/etc/lighttpd/clear-creds.lst`, that will contain credentials required for authentication, under the following form:

    :::text
    user1:password1
    user2:password2
    user3:password3

Logins and passwords are stored here in clear. This is stupid, but for this project I was looking to setup a quick and dirty server. For temporary tests this setup is OK, but I encourage you to switch to a better credential storage system.

Now I want to serve WebDAV content within a secure channel. A self-signed SSL certificate will be enough. Let's generate one:

    :::bash
    $ cd /etc/lighttpd/
    $ openssl req -x509 -nodes -subj '/' -days 3650 -newkey rsa:2048 -keyout server.pem -out server.pem

We'll configure Lighttpd by loading the default parameters of modules we use:

    :::bash
    $ cd /etc/lighttpd/conf-enabled/
    $ ln -s ../conf-available/05-auth.log
    $ ln -s ../conf-available/10-ssl.conf
    $ ln -s ../conf-available/10-webdav.conf

Now I create a custom configuration file:

    :::bash
    $ touch /etc/lighttpd/conf-available/99-custom.conf
    $ cd /etc/lighttpd/conf-enabled/
    $ ln -s ../conf-available/99-custom.conf

Here is the content of that `99-custom.conf` configuration file:

    :::lighttpd
    # Hide server version
    server.tag = "lighttpd"

    # Force all request to be in HTTPs
    # This also redirects all WebDAV requests to WebDAVs
    $HTTP["scheme"] == "http" {
      $HTTP["host"] =~ "(.*)" {
        url.redirect = ( "^/(.*)" => "https://%1/$1" )
      }
    }

    # Valid credentials are required for any request
    auth.backend = "plain"
    auth.backend.plain.userfile = "/etc/lighttpd/clear-creds.lst"
    auth.require = (
      "/" => (
        "method" => "digest",
        "realm" => "My WebDAV server",
        "require" => "valid-user"
      )
    )

    # Enable WebDAV in read and write mode
    webdav.activate = "enable"
    webdav.is-readonly = "disable"

    # Customize directory listings a bit
    dir-listing.set-footer = "<a href='http://example.com'>Company</a>'s document repository."

And do not forget to restart the server:

    :::bash
    $ /etc/init.d/lighttpd restart

![](/uploads/2011/lighttpd-webdav-server.png)

As you can see in the screenshot above, you can now:

  * Browse the file system in read/write mode with a WebDAV client via a `webdavs://12.34.56.78/` URL;
  * Access content in read-only mode with a browser by a classic `https://12.34.56.78/` URL.

---
date: 2009-09-21 20:59:10
title: Moving a WordPress blog to another domain
category: English
tags: Apache, Blog, CLI, find, grep, Hosting, Linux, MySQL, SQL, sed, Server, Web, WordPress, Regular expression
---

![qpx-site-domain-migration](/uploads/2009/qpx-site-domain-migration.png)

I provide hosting for free to some of my friends. One of them,
[QPX](https://wqpx.wordpress.com/), had a side project called *Lich'ti*. But the
latter is no longer active, so he decided to not renew the `lich-ti.fr` domain.

If the *Lich'ti* domain name is dead, QPX's personal blog is not. His website is
powered by WordPress and was available at `https://qpx.lich-ti.fr`. My job is now
to move it to `https://qpx.coolcavemen.com`. In this post, I'll tell you how I've
done it.

Before going further, backup everything, and be ready to revert back to your
original situation at any moment! What works for me will not necessary works
for you...

To play nice with your visitors, you can
[setup a temporary maintenance page](https://www.milienzo.com/2007/05/16/how-to-display-a-maintenance-page-whilst-upgrading-wordpress/)
while we're performing the migration.

Let's start the migration by replacing, in the files served by Apache, all
occurrences of the old domain name by the new one:

    :::bash
    $ find /var/www/qpx-blog -mount -print -type f -exec sed -i 's/qpx.lich-ti.fr/qpx.coolcavemen.com/g' "{}" \;

If you have doubts about the efficiency of the command above, you can check the
presence of the string we're looking to replace via this command:

    :::bash
    $ grep -RIi "qpx.lich-ti.fr" ./*

Then, we dump the database containing all WordPress content and config to a
local file (the command will prompt for password):

    :::bash
    $ mysqldump -p --host=localhost --port=3306 --user=root --opt --databases "qpx_blog" > qpx_dump.sql

And we replace all strings of the old domain by the new one:

    :::bash
    $ sed 's/qpx.lich-ti.fr/qpx.coolcavemen.com/g' qpx_dump.sql > new_qpx.sql

Finally, we re-inject the modified database content after clearing the original:

    :::bash
    $ mysql -p --host=localhost --port=3306 --user=root --execute='DROP DATABASE `qpx_blog`;'
    $ mysql -p --host=localhost --port=3306 --user=root < new_qpx.sql

Now you can disable the maintenance page and test the blog to check nothing's
broken.

Again, to play nice with your visitors (and search engines), you can redirect
old URLs to the new domain, with apache directives similar to this one:

    :::apache
    <VirtualHost *:80>
      ServerName qpx.lich-ti.fr
      RedirectMatch permanent (.*) http://qpx.coolcavemen.com$1
    </VirtualHost>

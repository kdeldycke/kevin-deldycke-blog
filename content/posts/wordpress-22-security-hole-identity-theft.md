comments: true
date: 2007-06-07 17:22:51
layout: post
slug: wordpress-22-security-hole-identity-theft
title: Wordpress 2.2 Security Hole: Identity Theft
wordpress_id: 191
category: English
tags: Apache, Blog, hack, log, security, Server, Web, WordPress

I'm running 4 Wordpress blogs, for me and my friends. All of them are updated to latest version of Wordpress as soon as a new one is available.

One of them, [Maomium](http://maomium.com), was hacked last night. Someone created a user account on it then stole my admin identity to post content. As soon as I discovered the hack, I've put the blog down and changed all passwords which may have been exposed to the hacker (database, etc...).

Before the hack happened, my apache log show me that a person was looking for blogs powered by Wordpress 2.2 and open to registration:

    :::console
    123.76-136-217.adsl-dyn.isp.belgacom.be www.maomium.com - [07/Jun/2007:00:51:55 +0200] "GET /category/wordpress/ HTTP/1.1" 200 2960 "http://www.google.be/search?hl=fr&q=%22powered+by+wordpress+2.2%22+Register&btnG=Rechercher&meta=" "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1.4) Gecko/20070515 Firefox/2.0.0.4"

This person was my hacker. As you can see he's a belgian guy and his broadband provider is [Belgacom, to which I sent an abuse request](http://selfcare.belgacom.net/index.html?l=private:internet:security:notify&a=hacking_skynet). He register himself as [Waryas](http://waryas.skynetblogs.be) with his `myv4you@hotmail.com` email. I know that, thanks to the email Wordpress send me each time someone register. Then [google told me](http://www.google.fr/search?q=myv4you%40hotmail.com) that [this hack was not his first](http://www.coolforum.net/forum/detail.php?forumid=1&id=17468&p=1#29054).

If you want to disect his behaviour, you can [download my apache log](http://kevin.deldycke.com/wp-content/uploads/2007/06/wordpress-22-register-new-user-hack.txt).

This event show us that the Wordpress vulnerablility regarding guest account registration is still there. So the [advice given by CountZero](http://www.4null4.de/174/wp-users-disable-guest-account-registration-immediately/) **must** be applied !

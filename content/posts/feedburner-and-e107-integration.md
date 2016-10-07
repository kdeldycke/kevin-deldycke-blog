---
date: 2007-05-27 20:45:12
title: FeedBurner and e107 integration
category: English
tags: Apache, Atom, Blog, CMS, e107, feed, FeedBurner, htaccess, RDF, RSS, Server, Web, WordPress
---

![](/uploads/2007/e107-and-feedburner.png)

In the context of my [plan to move an e107-based website to Wordpress](http://kevin.deldycke.com/2006/08/e107-to-wordpress-migration-here-is-why/), I need to take care of my RSS subscribers. To let people (and search engines) get my content via old URLs, I will use [Apache redirections](http://en.wikipedia.org/wiki/URL_redirection) to do this transparently and permanently. My final goal is to have a Wordpress website with all RSS feeds (blog posts and comments) managed by [FeedBurner](http://www.feedburner.com), to gather statistics about my audience.

Actually there is plenty of feeds format available in e107 (RSS 1.0, RSS 2.0, Atom and RDF) and one feed can be accessed through multiple URLs. We will reduce this incredible mess by using RSS 2.0 feeds only and redirect all others to it.

First, check that the e107 RSS feed plugin is activated. Then [create an account on FeedBurner](https://www.feedburner.com/fb/a/register) and setup there two feeds, one for your website's news and another one for comments. Based on default e107 parameters, your news feed URL is like `http://www.my-domain.com/e107_plugins/rss_menu/rss.php?1.2` and comments feed like `http://www.my-domain.com/e107_plugins/rss_menu/rss.php?5.2`.

Then, create (or edit) the `http://www.my-domain.com/.htaccess` file, and add following code:

    :::apache
    RewriteEngine On

    RewriteCond %{HTTP_USER_AGENT} !FeedBurner [NC]
    RewriteCond %{QUERY_STRING} ^(5|Comments)
    RewriteRule e107_plugins/rss_menu/rss\.php http://feeds.feedburner.com/myfeed-comments? [R=301,L]

    RewriteCond %{HTTP_USER_AGENT} !FeedBurner [NC]
    RewriteCond %{QUERY_STRING} ^(1|News|.*)
    RewriteRule e107_plugins/rss_menu/rss\.php http://feeds.feedburner.com/myfeed? [R=301,L]

This code is inspired by the one written by [Mike Atlas](http://www.mikeatlas.com), who had a similar issue and wanted to [outsource his e107 forum RSS feeds to FeedBurner](http://www.mikeatlas.com/blog/2007/03/09/transparently-outsourcing-your-rss-feeds-to-feedburner/).

The first rewrite rule will redirect all URLs that start with `http://www.my-domain.com/e107_plugins/rss_menu/rss.php?5` or `http://www.my-domain.com/e107_plugins/rss_menu/rss.php?Comments` to `http://feeds.feedburner.com/myfeed-comments`.

The second rewrite rule will redirect all other URLs that start with `http://www.my-domain.com/e107_plugins/rss_menu/rss.php` (including `http://www.my-domain.com/e107_plugins/rss_menu/rss.php?1` and `http://www.my-domain.com/e107_plugins/rss_menu/rss.php?News`) to `http://feeds.feedburner.com/myfeed`.

That's all! Thanks to this server-side redirection, nobody will notice that the feeds have moved and no subscriber will be bothered to update their [aggregator](http://en.wikipedia.org/wiki/Aggregator).

In my case, the only remaining task to do is to move my e107 website to Wordpress then install [FeedSmith plugin](http://blogs.feedburner.com/feedburner/archives/2007/05/feedburner_adopts_twoyearold_r_1.php). But that's another story... ;)

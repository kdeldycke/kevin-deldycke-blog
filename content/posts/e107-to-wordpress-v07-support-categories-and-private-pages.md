comments: true
date: 2007-03-08 23:51:16
layout: post
slug: e107-to-wordpress-v07-support-categories-and-private-pages
title: e107 to WordPress v0.7: support Categories and Private Pages
wordpress_id: 144
category: English
tags: Blog, e107, PHP, Web, WordPress

![e107 to WordPress import plugin v0.7: News and Categories Imported screenshot](/static/uploads/2007/03/e107-to-wordpress-v07-news-and-category-imported1.png)

I've released a new version of my e107 migration script for WordPress. This release is [numbered v0.7](http://wordpress.org/extend/plugins/e107-importer/).

Here is the change-log:

  * Import e107 news categories.

  * Mails can be sent to each user to warn them about their new password. This is the only solution I found to fix [the issue about reseted passwords](http://kevin.deldycke.com/2006/11/wordpress-to-e107-v06-better-content-rendering-and-extended-news-support/#comment-2422).

  * Thanks to the 2.1 branch of Wordpress, static pages can be set as private. This version of my script use this feature.

  * Private pages also deprecate the questions asked to the user when importing pages. So I deleted [those parameters ("`Warning 2`" on the screenshot)](/static/uploads/2006/11/e107-to-wordpress-v05.png) to make the import process easier.

  * Embedded e107 code updated from v0.7.8.

  * Tested with Wordpress 2.1.2.

  * Some little UI imporvements (to match admin UI consistency).

Because of its de-facto standard status, my import script is now packaged as a `.zip` file. It can be downloaded from [my Linux Scripts section](http://kevin.deldycke.com/code/).

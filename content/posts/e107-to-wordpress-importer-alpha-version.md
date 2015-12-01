---
date: 2006-08-24 20:52:50
title: e107 to Wordpress Importer: Alpha version
category: English
tags: Blog, CMS, e107, PHP, Web, WordPress

As I said yesterday, I will migrate my e107 content to Wordpress. My first step in this direction was to write a Wordpress import filter.

So here is my [first draft of the e107 to Wordpress importer (direct link to php file)](http://wordpress.org/extend/plugins/e107-importer/).

To use it, copy the e107.php file to your `wp-admin/import` folder. To launch the import, go to the `Import` page of your Wordpress administation panel, select e107, and fill required fields (user, password, database host, database name and table's prefix) to let the script reach your e107 datas. Then, follow steps and instructions until the end.

Be carefull, actually the script is a very alpha version that only get e107 news items and transform them to Wordpress posts. It's more a proof-of-concept script than a really useable and stable importer.

In future releases, I plan to add following features:

  * Import News categories as tags,

  * Import static pages,

  * Import comments,

  * Import users (both post and comment authors),

  * Auto convert bb tags to html,

  * Auto import images embedded in news/pages.

You can also [get the latest version of the script from my "Linux Scripts" page](http://kevin.deldycke.com/code/).

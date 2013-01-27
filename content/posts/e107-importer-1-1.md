comments: true
date: 2011-03-01 11:37:09
layout: post
slug: e107-importer-1-1
title: e107 Importer 1.1 available !
wordpress_id: 2938
category: English
tags: CMS, e107, import, migration, PHP, plugin, Web, WordPress

[A month after the 1.0 release](http://kevin.deldycke.com/2011/01/e107-importer-wordpress-plugin-v1-0-released/), here is my [e107 Importer v1.1 for WordPress](http://wordpress.org/extend/plugins/e107-importer/) !

![](http://kevin.deldycke.com/wp-content/uploads/2011/03/e107-importer-option-panel.png)

The biggest new feature is support of e107 forum import to the [bbPress WordPress plugin](http://wordpress.org/extend/plugins/bbpress/). This plugin is still in alpha and was not released yet. This mean you have to [fetch it from its Subversion repository](http://trac.bbpress.org/browser/branches/plugin?rev=2942). And be careful to get the recommended version (SVN release 2942).

Because of the experimental status of forum import, the default option of e107 Importer is to not import forums. I decided to include this feature anyway to get feedbacks. So please don't consider forum import as a highly reliable. It may work for you or may not. And please write detailed bug reports.

Here is a detailed changelog between 1.0 and 1.1:

  * Add import of forums and threads to bbPress WordPress plugin.

  * Parse BBCode and e107 constants in forums and thread.

  * Add forums and threads redirections.

  * Make e107 user import optional. This needs you to set a pre-existing WordPress user that will take ownership of all imported content.

  * Parse BBCode in titles too.

  * Import images embedded in comments and forum threads.

  * Description update of existing users is no longer destructive.

  * Add an entry in the FAQ regarding script ending prematurely.

  * Disable all extra HTML rendering hooks like the one coming from e107 linkwords plugin.

  * Allow news and pages import to be skipped.

  * Add missing news category redirects.

  * Minimal requirement set to WordPress 3.1.

  * Some pages are not tied to a user. In this case, default to the current user.


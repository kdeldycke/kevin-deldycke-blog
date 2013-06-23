date: 2011-04-05 16:37:43
title: e107 Importer 1.2 is out, with an enhanced BBCode parser.
category: English
tags: Blog, code, e107, MySQL, SQL, PHP, Web, WordPress

![](/static/uploads/2011/e107-importer-12-option-panel.png)

Here is a brand new version of my e107 Importer plugin. This release fix lots of nasty bugs. Better, I added an enhanced BBCode parser which try to clean-up what e107's parser output. This new parser also try to align the final HTML with what WordPress produce by default.

As usual, my [plugin is available on the official WordPress plugin directory](http://wordpress.org/extend/plugins/e107-importer/).

Here is the detailed changelog:

  * Upgrade e107 code to match latest [0.7.25-rc1](http://e107.org/news.php?item.879).

  * Fix variable bleeding when importing items in batches.

  * Add a new way of handling e107 extended news using WordPress' excerpts.

  * Parse BBCode and replace e107 constants in news excerpt.

  * Use internal WordPress library (kses) to parse HTML in the image upload step.

  * Do not upload the same images more than once.

  * Add a new enhanced BBCode parser on top of the one from e107. Make it the default parser.

  * Each time we alter the original imported content, we create a post revision.


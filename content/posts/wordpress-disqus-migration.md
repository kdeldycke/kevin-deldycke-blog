comments: true
date: 2013-01-22 13:26:53
layout: post
slug: wordpress-disqus-migration
title: WordPress to Disqus Migration
category: English
tags: Comment, Disqus, HTML, migration, MySQL, SQL, Regular expression, WordPress

I've just finished migrating all the comments of this blog from WordPress to [Disqus](http://disqus.com). Why using an external comment platform ? It's just that I plan to ditch WordPress entirely, and switch to a static site generator in the near future. Here are some details on my migration to Disqus.

Disqus has everything you need to easily import WordPress comments. But first, I had to massage some data.

Articles of this blog features a lots of code. Comments are no exception and embed snippets too. Code blocks are rendered by the [SyntaxHighlighter Evolved WordPress plugin](http://wordpress.org/extend/plugins/syntaxhighlighter/). This extension use square brackets to enclose code. [Disqus uses standard HTML tags](http://help.disqus.com/customer/portal/articles/665057).

Let's update this notation directly in WordPress database:

    :::bash
    $ mysqldump --opt kevblog wp_comments > ./comments.sql
    $ perl -pe 's/\[code lang=(.*?)\]/<pre><code class=\1>/g' ./comments.sql > comments-fixed.sql
    $ sed -i 's/\[\/code\]/<\/code><\/pre>/g' ./comments-fixed.sql
    $ mysql kevblog < ./comments-fixed.sql

[Disqus doesn't support HTML lists](http://help.disqus.com/customer/portal/articles/466253-what-html-tags-are-allowed-within-comments). So I manually updated WordPress comments to remove occurrences of `<ul>` and `<ol>`, and replace `<li>` by an UTF-8 `•` [bullet](http://en.wikipedia.org/wiki/Bullet_(typography)).

Another issue: if [Disqus support images in comment](http://blog.disqus.com/post/3764930816/fun-with-images), in imported comments they are left as HTML tags and therefore not rendered by Disqus. I was the only one on my blog posting images in comments. So I simply moved them to the corresponding parent article.

Finally, I fixed the comment threading from the old days sub-commenting was not supported by WordPress. This was simply addressed with a series of MySQL queries:

    :::mysql
    UPDATE `wp_comments` SET `comment_parent` = 234   WHERE `comment_ID` = 342;
    UPDATE `wp_comments` SET `comment_parent` = 4987  WHERE `comment_ID` = 5667;
    UPDATE `wp_comments` SET `comment_parent` = 10915 WHERE `comment_ID` = 10916;
    (...)

After all these updates, my comments where ready to be [exported to Disqus](http://help.disqus.com/customer/portal/articles/466255-exporting-comments-from-wordpress-to-disqus).

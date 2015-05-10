date: 2013-11-05 12:00:00
title: How-to simplify Amazon affiliate links
category: English
tags: Amazon, ads, campaign, affiliates, Markdown, find, sed, Linux

From the beginning on this blog, I'm using the long-form of URLs for Amazon referrals. Here's one for the [GoPro Hero3](http://amzn.com/B00F3F0GLU/?tag=kevideld-20) in HTML:

    :::html
    My brand new <a href="http://www.amazon.com/gp/product/B00F3F0GLU/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00F3F0GLU&linkCode=as2&tag=kevideld-20">GoPro Hero3</a><img src="http://www.assoc-amazon.com/e/ir?t=kevideld-20&l=as2&o=1&a=B00F3F0GLU" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /> is awesome.

Which renders to:

> My brand new [GoPro Hero3](http://amzn.com/B00F3F0GLU/?tag=kevideld-20) is awesome.

Now with a Markdown syntax, the code becomes:

    :::markdown
    My brand new [GoPro Hero3](http://www.amazon.com/gp/product/B00F3F0GLU/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00F3F0GLU&linkCode=as2&tag=kevideld-20) ![](http://www.assoc-amazon.com/e/ir?t=kevideld-20&l=as2&o=1&a=B00F3F0GLU) is awesome.

These links are ugly and requires a second URL for the 1-pixel image tracker.

I just discovered that you can [use a shorter version](http://blog.crazybob.org/2008/10/how-to-create-simple-amazon-affiliate.html) of the link. Which make the markup cleaner:

    :::markdown
    My brand new [GoPro Hero3](http://amzn.com/B00F3F0GLU/?tag=kevideld-20) is awesome.

And here's how I've transformed, in all my Markdown articles, the long Amazon links to their short form.

First, I simply removed all 1-pixel trackers:

    :::bash
    $ find ./* -iname "*.md" -exec perl -0777 -i -pe "s/\!\[\]\(http:\/\/www\.assoc-amazon\.com.*?\)//gs" "{}" \;

Then I converted all links in one batch with this magic one-liner:

    :::bash
    $ find ./* -iname "*.md" -exec perl -0777 -i -pe "s/\(http:\/\/www\.amazon\.com\/gp\/product\/(.*?)\/.*?\)/\(http:\/\/www\.amazon\.com\/dp\/\1\/\?tag=kevideld-20\)/gs" "{}" \;

---
date: '2013-11-05'
title: How-to simplify Amazon affiliate links
category: English
tags: Amazon, ads, campaign, affiliates, Markdown, find, sed, Linux, Regular expression
---

From the beginning on this blog, I'm using the long-form of URLs for Amazon referrals. Here's one for the [GoPro Hero3](https://amzn.com/B00F3F0GLU/?tag=kevideld-20) in HTML:

```html
My brand new
<a href="https://www.amazon.com/gp/product/B00F3F0GLU/ref=as_li_ss_tl?ie=UTF8&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B00F3F0GLU&amp;linkCode=as2&amp;tag=kevideld-20">
 GoPro Hero3
</a>
<img alt="" border="0" height="1" src="https://www.assoc-amazon.com/e/ir?t=kevideld-20&amp;l=as2&amp;o=1&amp;a=B00F3F0GLU" style="border:none !important; margin:0px !important;" width="1"/>
is awesome.

```

Which renders to:

> My brand new [GoPro Hero3](https://amzn.com/B00F3F0GLU/?tag=kevideld-20) is awesome.

Now with a Markdown syntax, the code becomes:

```markdown
My brand new [GoPro Hero3](https://www.amazon.com/gp/product/B00F3F0GLU/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00F3F0GLU&linkCode=as2&tag=kevideld-20) ![](https://www.assoc-amazon.com/e/ir?t=kevideld-20&l=as2&o=1&a=B00F3F0GLU) is awesome.
```

These links are ugly and requires a second URL for the 1-pixel image tracker.

I just discovered that you can [use a shorter version](https://blog.crazybob.org/2008/10/how-to-create-simple-amazon-affiliate.html) of the link. Which make the markup cleaner:

```markdown
My brand new [GoPro Hero3](https://www.amazon.com/dp/B00F3F0GLU/?tag=kevideld-20) is awesome.
```

And here's how I've transformed, in all my Markdown articles, the long Amazon links to their short form.

First, I simply removed all 1-pixel trackers:

```shell-session
$ find ./* -iname "*.md" -exec perl -0777 -i -pe "s/\!\[\]\(http:\/\/www\.assoc-amazon\.com.*?\)//gs" "{}" \;
```

Then I converted all links in one batch with this magic one-liner:

```shell-session
$ find ./* -iname "*.md" -exec perl -0777 -i -pe "s/\(http:\/\/www\.amazon\.com\/gp\/product\/(.*?)\/.*?\)/\(http:\/\/www\.amazon\.com\/dp\/\1\/\?tag=kevideld-20\)/gs" "{}" \;
```

You can even go further (thanks [Elias](https://kevin.deldycke.com/2013/simplify-amazon-affiliate-links#comment-1404886079) for the tip) and use Amazon's URL shortener to get the following short links:

```markdown
My brand new [GoPro Hero3](https://amzn.com/B00F3F0GLU/?tag=kevideld-20) is awesome.
```

This is the `sed` command I used to convert all links from the previous form to this new scheme:

```shell-session
$ find ./* -iname "*.md" -exec perl -0777 -i -pe "s/\(http:\/\/www\.amazon\.com\/dp\/(.*?)\)/\(http:\/\/amzn\.com\/\1\)/gs" "{}" \;
```

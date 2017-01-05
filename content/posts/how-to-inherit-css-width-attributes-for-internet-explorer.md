---
date: 2008-06-03 21:56:03
title: How-to inherit CSS width attributes for Internet Explorer
category: English
tags: CSS, Firefox, HTML, Internet Explorer
---

Let's say you rely on a third party CSS framework that set the default layout of
your content. The following CSS rule is part of the framework:

    :::css
    img {
      width: 100%;
    }

This CSS directive tell all your images to use the full width available to them.

Now, for any reason (aesthetic, layout, etc.), you want to reset this behaviour.

One solution (the laziest) is to remove those three lines from the original CSS
file. But if you're like me, this sound too dirty for you as you don't want to
modify the original CSS file (I like to avoid patches on third party tools and
                              libraries I don't maintain).

Another solution consist in overriding this `width` attribute in another CSS
file that you will call after the original one. This case is covered by the
[CSS 2.1 specification](https://www.w3.org/TR/CSS21/) which define the
[`inherit` value](https://www.w3.org/TR/CSS21/cascade.html#value-def-inherit):

    :::css
    img {
      width: inherit;
    }

This solution is perfect and work as expected in Firefox. Unfortunately, and
without any surprise, it doesn't with Microsoft's browser as
[IE has anecdotical support of CSS's `inherit`](https://www.sitepoint.com/blogs/2007/11/22/in-all-fairness-%e2%80%a6-internet-explorer-still-stinks/).

But today I found a trick to fix this in both Firefox and Internet Explorer. The
workaround is to use the `auto` value instead of `inherit`:

    :::css
    img {
      width: auto;
    }

I've tested it with both
[Firefox 3.0rc1](https://blog.mozilla.com/blog/2008/05/20/firefox-3-release-candidate-now-available-for-download/)
and Internet Explorer 6.0.2800.1106CO.

Of course this solution is not generic: it only work in my case because `img`
html tags has `width` attributes that support the `auto` value.

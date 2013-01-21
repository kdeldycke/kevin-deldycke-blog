comments: true
date: 2008-06-07 19:34:20
layout: post
slug: how-to-add-a-corner-banners-to-a-k2-wordpress-theme-style
title: How-to add a corner banner to a K2 Wordpress theme's style
wordpress_id: 226
category: English
tags: alpha, banner, corner, CSS, design, Gimp, HTML, IE, K2, Photoshop, PHP, PNG, qpx, style, Theme, transparency, Web, WordPress

![](http://kevin.deldycke.com/wp-content/uploads/2008/06/beta-version-illustration-150x150.png)

In this post I will give you all the technical details to create a corner banner for the wordpress K2 theme. This solution is uninstrusive as it can be bundled with a K2 style without modifying the K2 core theme.

We will use the new [hooks](http://code.google.com/p/kaytwo/wiki/K2CSSandCustomCSS#PHP) from the brand new [K2 1.0RC6](http://getk2.com/2008/04/k2-release-candidate-6-released/). So first, we have to create a `functions.php` file in our style directory (example: `/wp-content/themes/k2/styles/my-style`). Then add the following PHP code in it:

    
    :::php
    <?php
    
    // Add HTML code required by our corner banner
    function add_corner_banner() {
      ?>
      <a id="cornerbanner" href="http://coolcavemen.com/news/new-website-beta-released/" title="New website released as beta version !"></a>
      <?php
    }
    
    // Call add_corner_banner() method on each template_body_top hook
    add_action(‘template_body_top’, ‘add_corner_banner’);
    
    ?>
    



This code tell K2 to replace the `template_body_top` hook define in all K2 pages, by the result of the `add_corner_banner()` PHP function. This function is coded to return the HTML code we need for the corner banner.

Then we need to add the following CSS code to our style (`/wp-content/themes/k2/styles/my-style/my-style.css`):

    
    :::css
    #cornerbanner {
      background: url("/wp-content/themes/k2/styles/my-style/corner-banner.png") no-repeat;
      display: block;
      height: 205px;
      width: 205px;
      position: absolute;
      top: 0;
      right: 0;
      z-index: 999;
      text-decoration: none;
    }
    



This CSS code refer to the [`corner-banner.png`](http://kevin.deldycke.com/wp-content/uploads/2008/06/corner-banner.png) which is a 205x205 px PNG image with an alpha channel to simulate shadows and fine transparency. Here is the [Gimp `xcf` source file](http://kevin.deldycke.com/wp-content/uploads/2008/06/corner-banner.xcf) I used to generate it.

This CSS code is designed for a top right banner. If you need a top left banner, replace:

    
    :::css
      right: 0;
    


by

    
    :::css
      left: 0;
    



This also work for horizontal positioning:

    
    :::css
      top: 0;
    


can be replaced by

    
    :::css
      bottom: 0;
    



That's all ! My solution is not supposed to work (and was not tested) with Internet Explorer as the latter is known to have [terrible PNG transparency support](http://en.wikipedia.org/wiki/Portable_Network_Graphics#Web_browser_support_for_PNG). You can still apply fixes on my code using [iepngfix](http://www.twinhelix.com/css/iepngfix/), [jquery](http://jquery.andreaseberhard.de/pngFix/) or [PNG8 images](http://www.sitepoint.com/blogs/2007/09/18/png8-the-clear-winner/).

I've provided you with all the technical details to create a corner banner and add it to your K2 style seamlessly. It's now up to you to adapt it to your needs. Be Creative ! Oh, and by the way, when you'll change the banner PNG file, do not forget to update the CSS code with your image width and height.

**Update**: [my friend QPX](http://qpx.coolcavemen.com) sent me an alternative banner made with photoshop: here is the [ready-to-use PNG file](http://kevin.deldycke.com/wp-content/uploads/2008/06/corner-banner-qpx.png) and the [photoshop source file](http://kevin.deldycke.com/wp-content/uploads/2008/06/corner-banner-qpx.psd).

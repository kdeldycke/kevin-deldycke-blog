date: 2013-06-17 12:32
title: Fix big HTML table rendering in IE
category: English
tags: Internet Explorer, Microsoft, OpenERP, HTML, webdesign

It is well-known since the burst of the dot-com bubble that [tables are bad for layout](http://en.wikipedia.org/wiki/Tableless_web_design). But tables still makes perfect sense to present huge quantities of tabular data.

The thing is, Internet Explorer can't cope with big HTML tables. So when it encounters a huge number of cells, IE9 starts to shift them randomly:

![](/uploads/2013/go-home-internet-explorer-you-are-drunk.png)

You can [go here to reproduce this issue](http://jsfiddle.net/kiranmn/kYRnV/).

I absolutely don't care about these issues. Life is short. I have better things to do than fixing IE bugs.

Still, at work, things are different. You're trading time for money. And it's up to your customer to choose what you should do with your time. I guess that's the tragedy of becoming a part of the software workforce.

That's how I started to dive into IE hell.

After some research, I found out the root cause of this issue. It's the presence of extra spaces and line returns between cells. Any sane browser should ignore these. But IE9 simply can't.

This issue seems to have been [known since April 2011](http://social.msdn.microsoft.com/Forums/en-US/iewebdevelopment/thread/28d78780-c95c-4c35-9695-237ebb912d90) (at least), but hasn't been addressed by Microsoft yet.

And you know how I fixed this ? I fearlessly added the following piece of JavaScript in my initialization code:

    :::javascript
    // Fix IE9 cells misalignment
    $("table tr").contents().filter(function() {
        return this.nodeType == 3;
    }).remove();

The code above just strips all extra spaces from tables it find. You can [see this hack in action](https://github.com/Smile-SA/smile_openerp_matrix_widget/commit/c9646dd344e6bc05d5b9f8d33bd3cd6116e1c0f3) in my [matrix widget for OpenERP 6.0](http://kevin.deldycke.com/2012/08/announcing-openerp-matrix-widget/).

This is ugly, but makes my customer happy. Life is full of contradictions. And that's normal.

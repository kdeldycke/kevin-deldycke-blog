comments: true
date: 2011-08-16 12:10:06
layout: post
slug: webping-open-sourced
title: WebPing Open-sourced !
wordpress_id: 3715
category: English
tags: Apache, email, flot, GitHub, HTML, HTTP, javascript, jquery, munin, nagios, Plone, Python, Server, SQLite, SQL, Web, webping, yaml

I've just released WebPing under a GPL license. It's available right now on a [GitHub repository](http://github.com/kdeldycke/webping).

WebPing is a script I started to work on in 2009 while working at [EDF](http://www.edf.com/). Back then, I needed a monitoring tool to keep an eye on the 80+ [Plone](http://plone.org/) instances that my team managed. For several corporate reasons, I wasn't allowed to use a proper monitoring tool like [Munin](http://munin-monitoring.org/) or [Nagios](http://www.nagios.org/). So I created a small script to fill this need. That's how WebPing came to be.

WebPing is just a stupid Python script that is designed to be ticked regularly by a cron job. It try to fetch a list of URLs and store response times in an SQLite database. Then it create a static HTML report you're free to serve with any HTTP server (an [example Apache configuration](http://github.com/kdeldycke/webping/blob/master/apache.conf) is provided). The configuration of WebPing and the list of URLs it monitor is stored in a YAML file.

The produced HTML report use the [Flot jQuery plugin](http://code.google.com/p/flot) to render graphs. Here is how the dashboard looks like:

![](/static/uploads/2011/08/webping-dashboard.png)

Finally, WebPing is able to send reports and alerts by emails. Here is how a mail alert looks like:

![](/static/uploads/2011/08/webping-email-alert.png)

Since I created WebPing, I found several other projects more or less developed around the same idea. See [Kong](http://github.com/ericholscher/django-kong), which is based on Django and [Twill](http://twill.idyll.org/), a web-oriented [DSL](http://en.wikipedia.org/wiki/Domain-specific_language). Another project I spotted after the facts was [multi-mechanize](http://code.google.com/p/multi-mechanize). Like Kong, it's written in Python. But I never played with one or the other.

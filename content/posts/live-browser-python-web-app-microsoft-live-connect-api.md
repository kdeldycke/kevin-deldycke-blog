comments: true
date: 2011-12-06 12:27:03
layout: post
slug: live-browser-python-web-app-microsoft-live-connect-api
title: Live Browser : a Python web app using Microsoft Live Connect API
wordpress_id: 3901
category: English
tags: API, Boilerplate, bootstrap, cherrypy, cloud-computing, Git, GitHub, javascript, jquery, mako, microsoft, Microsoft live connect, mongodb, OAuth, Python, Web

5 months ago I was called by a recruiter for a position in a startup building cloud-computing solutions. At the end of my first interview with the engineers of the company, I was asked to write a little web application to test my technical abilities.

The goal was to create a back-end talking to [Microsoft's Live Connect API](http://msdn.microsoft.com/windowslive) and keep a cache of user profiles. Then a front-end demonstrating my HTML/CSS/JS know-how was to be built. User authentication was supposed to use [OAuth](http://oauth.net).

The only technological constraint was to use Python. I decided to use [CherryPy](http://cherrypy.org) and [Mako](http://www.makotemplates.org) to leverage the [boilerplate code I just released back then](http://kevin.deldycke.com/2011/08/cherrypy-mako-formish-ooop-boilerplate/). For the persistent layer, my first intention was to use [SQLAlchemy](http://www.sqlalchemy.org), but quickly switched to [MongoDB](http://www.mongodb.org) as I never played with it and this project was a great opportunity to.

If my web app was far from finished, it was still well-received by the team. After other interviews I was made an competitive offer. I finally declined as I wanted to finish what I stated at my current company.

What's left of this experience is _Live Browser_, the web app I created, which [source code is now available on GitHub](https://github.com/kdeldycke/live_browser).

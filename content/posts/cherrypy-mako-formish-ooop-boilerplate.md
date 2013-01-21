comments: true
date: 2011-08-23 12:58:37
layout: post
slug: cherrypy-mako-formish-ooop-boilerplate
title: CherryPy + Mako + Formish + OOOP boilerplate
wordpress_id: 3817
category: English
tags: cherrypy, formish, GitHub, GPL, mako, ooop, open source, OpenERP, Python

After [WebPing last week](http://kevin.deldycke.com/2011/08/webping-open-sourced/), here is another release of Open-Source code. This time it's my boilerplate codebase I created to integrate some Python components with the goal of publishing [OpenERP](http://www.openerp.com/) content on the web.

This stack is composed of:



  
  * [CherryPy](http://www.cherrypy.org/) to serve web content,

  
  * [Mako](http://www.makotemplates.org/) for HTML templating,

  
  * [Formish](http://github.com/ish) for HTML form generation and validation,

  
  * [OOOP](http://github.com/lasarux/ooop) to talk to OpenERP server via web services.



This project contains the experiments I did while working at [Smile](http://www.smile.fr/), when I explored the possibility of integrating these components. This code was a proof-of-concept that we leveraged later for a highly specific OpenERP project.

Because of the highly experimental nature of this project, it contains lots of stupid and failed attempts. The whole code base should be thoroughly cleaned up before it can be considered reusable.

All that code is [available in a GitHub repository](http://github.com/kdeldycke/cherrypy_mako_formish_ooop_boilerplate), under a [GPL v2 license](http://www.gnu.org/licenses/gpl-2.0.html).

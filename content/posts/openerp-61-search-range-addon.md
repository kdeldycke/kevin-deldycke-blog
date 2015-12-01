---
date: 2013-04-23 12:25:36
title: Addon to restore search range in OpenERP 6.1
category: English
tags: OpenERP, Javascript, Backbone.js, jQuery, Web, addon

In OpenERP 6.1, the default search widget for dates and floats [no longer feature a range](https://bugs.launchpad.net/openerp-web/+bug/926390/):

![](/uploads/2013/openerp-61-no-range-search-widget.png)

This was [uncovered](https://bugs.launchpad.net/openerp-web/+bug/949990) by [users](https://answers.launchpad.net/openobject-server/+question/198725) in the [community](https://answers.launchpad.net/openobject-server/+question/198863). But it's not a bug, [it's a feature](https://bugs.launchpad.net/openerp-web/+bug/926390/comments/4), a design decision.

Worse, `datetime` search field in OpenERP 6.1 [no longer let you set the time](https://bugs.launchpad.net/openerp-web/+bug/1037658):

![](/uploads/2013/openerp-61-datetime-search-view.png)

To fix these issues, I've created [`web_smile_search_range`](https://github.com/Smile-SA/smile_openerp_addons_6.1/tree/master/web_smile_search_range) a module which is available since 2012, but I never advertised it on this blog.

This module is based on an [open-source addon from Credativ](http://bazaar.launchpad.net/~credativ/credativ-openerp/addons-6.1/files/head:/web_searchdaterange/). I extended the later to:

  * Replace single `date`, `datetime` and `float` search fields to a range.
  * Allow selection of time in `datetime` search fields.

Thus restoring the default behavior from OpenERP 6.0 that was ditched in 6.1.

And if you need to dig deeper in the code, you'll quickly find out that the core of the module lie in the [`search.js` file](https://github.com/Smile-SA/smile_openerp_addons_6.1/blob/master/web_smile_search_range/static/src/js/search.js), which extend in Javascript the search fields models of our interests.
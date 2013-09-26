date: 2012-04-17 12:46:34
title: How-to add a warning banner to OpenERP's web client
category: English
tags: CSS, HTML, mako, OpenERP, ERP

When working with multiple OpenERP instances in different stages, you can be sure your customer will one day mix up your pre-production and production instance, which can have catastrophic effects.

A quick and dirty hack to prevent such events is to add a hard-coded warning message to all content produced by OpenERP:

![](/uploads/2012/openerp-login-screen-with-alert-banner.png)

The result above was produced on OpenERP 6.0 thanks to the following patch on the [`header.mako`](http://bazaar.launchpad.net/~openerp/openobject-client-web/6.0/view/head:/addons/openerp/controllers/templates/header.mako) template file:

    :::diff
    --- addons/openerp/controllers/templates/header.mako.orig       2012-02-20 11:13:08.228864937 +0000
    +++ addons/openerp/controllers/templates/header.mako    2012-02-20 11:12:41.361480113 +0000
    @@ -115,3 +115,18 @@
             });
         });
     </script>
    +
    +<!-- Custom header banner -->
    +</tr><tr>
    +<style type="text/css">
    +    #warning-banner {
    +        background-color: #c00;
    +        color: #fff;
    +        text-align: center;
    +        font-weight: bold;
    +        padding: 0.6em;
    +    }
    +</style>
    +<td id="warning-banner" colspan="3">
    +    <p>Warning: this is a pre-production OpenERP instance.</p>
    +</td>


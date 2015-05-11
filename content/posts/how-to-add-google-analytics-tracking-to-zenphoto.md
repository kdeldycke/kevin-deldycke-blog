date: 2008-08-16 22:49:55
title: How-to add Google Analytics tracking to Zenphoto
category: English
tags: analytics, Google, hack, patch, PHP, Zenphoto, SSL

![](/uploads/2008/zenphoto-12.png)

This is the patch I apply on each [Zenphoto](http://www.zenphoto.org) I install
and upgrade. This little hack add
[Google Analytics](http://www.google.com/analytics/) tracking for all users
except administrators.

Why ? As you can see in
[ticket #441 in Zenphoto bugtracker](http://www.zenphoto.org/trac/ticket/441),
there is no intention of adding support of GA in Zenphoto, even as an optional
plugin. Hence my tiny hack. And for the non-admin stuff, I like having unbiased
statistics: on low-audience websites, administrators can generate more traffic
than legitimate users (if not all...).

Here is the
[downloadable patch file](/uploads/2008/google-analytics-tracking-for-non-admin-users.patch),
and its content:

    :::diff
    diff -ru ./zenphoto-orig/zp-core/template-functions.php ./zenphoto/zp-core/template-functions.php
    --- ./zenphoto-orig/zp-core/template-functions.php  2008-08-15 07:43:05.000000000 +0200
    +++ ./zenphoto/zp-core/template-functions.php 2008-08-16 17:08:03.000000000 +0200
    @@ -147,7 +147,16 @@

        echo "<li><a href=\"".$zf."/admin.php?logout$redirect\">".gettext("Logout")."</a></li>\n";
        echo "</ul></div>\n";
    - }
    + } else {
    +    echo "<script type=\"text/javascript\">
    +var gaJsHost = ((\"https:\" == document.location.protocol) ? \"https://ssl.\" : \"http://www.\");
    +document.write(unescape(\"%3Cscript src='\" + gaJsHost + \"google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E\"));
    +</script>
    +<script type=\"text/javascript\">
    +var pageTracker = _gat._getTracker(\"UA-XXXXXX-Y\");
    +pageTracker._trackPageview();
    +</script>";
    +  }
     }

     /**

This patch was generated from a
[Zenphoto v1.2](http://www.zenphoto.org/2008/08/zenphoto-12-release-announcement/)
and will likely not work with any other version.

Do not forget to update the dummy Google Analytics account ID above
(`UA-XXXXXX-Y`) by yours.

And finally, to apply the patch, invoke the classic `patch` command:

    :::bash
    $ patch -p0 < ./google-analytics-tracking-for-non-admin-users.patch

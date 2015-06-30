Kevin Deldycke's blog
=====================

These are the source files of the content of my [blog](http://kevin.deldycke.com),
which is powered by [Pelican](http://getpelican.com), a static site generator written in Python.

The theme it uses is called [Plumage](https://github.com/kdeldycke/plumage).


Installation
------------

Install Pelican and its dependencies:

    $ sudo aptitude install -y python-markdown python-pygments python-beautifulsoup pandoc python-smartypants s3cmd
    $ pip install --upgrade pelican mdx_video typogrify Fabric


Development
-----------

In one terminal, run:

    $ fab regenerate

And in another:

    $ fab serve

Then go to [http://localhost:8000](http://localhost:8000).


Deployment
----------

We use `make` for deployment as `fab` is not wired yet:

    $ make s3_upload


TODO
----

  * Re-use previous artworks from Maomium ?
  * Test different ad placements: http://news.ycombinator.com/item?id=4974511
  * Get rid of /year/month/ for articles ? Or get rid of month only ?
  * Deduplicate articles' tags.
  * Use a free OpenShift instance to host a script monitoring Github commits ? See:
      * https://www.openshift.com
      * https://pypi.python.org/pypi/pelicangit
  * Fix Google Analytics bouncing rate ? See: http://drawingablank.me/blog/fix-your-bounce-rate.html
  * Migrate Resume from Google Docs to web-based page in Pelican ? Inspiration:
      * https://wrapbootstrap.com/theme/simply-minimal-responsive-resume-WB0DCP565
  * Use pelican-titlecase. See: https://github.com/jrarseneau/pelican-titlecase/issues/1
  * Automate and script S3 deployment with:
      * https://github.com/heyimalex/s3tup
      * https://github.com/boto/boto
  * Migrate `/content/extra/htaccess` rules to [S3 routing rules](http://docs.aws.amazon.com/AmazonS3/latest/dev/HowDoIWebsiteConfiguration.html#configure-bucket-as-website-routing-rule-syntax) and/or use https://pypi.python.org/pypi/pelican-alias for redirects ?
  * Activate AWS CloudFront ? (See: http://paulstamatiou.com/hosting-on-amazon-s3-with-cloudfront/ )
  * Create an autoindex plugin: activate it to produce index of /documents, then get rid of
    htaccess-static.
  * Add static site search:
      * http://blog.new-bamboo.co.uk/2013/02/26/full-text-search-in-your-browser
      * http://lunrjs.com/
      * https://github.com/getpelican/pelican/issues/170
      * https://github.com/slashdotdash/jekyll-lunr-js-search


License
-------

The content of this repository is copyrighted (c) 2004-2014 Kevin Deldycke.

Unless contrary mention, the licensing terms below applies:

  * Code and software released under [GNU/GPL licence, v2.0](http://www.fsf.org/licensing/licenses/gpl.html).
  * Other content published under [Creative Commons Attribution-Share Alike 3.0 license](http://creativecommons.org/licenses/by-sa/3.0/).

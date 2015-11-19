Kevin Deldycke's blog
=====================

These are the source files of the content of my [blog
](http://kevin.deldycke.com), which is powered by [Pelican
](http://getpelican.com), a static site generator written in Python.

The theme it uses is called [Plumage](https://github.com/kdeldycke/plumage).


Installation
------------

Install Pelican and its dependencies:

    $ pip install --upgrade pelican Markdown mdx_video typogrify beautifulsoup4 Fabric s3cmd

Then fetch a copy of the repository:

    $ git clone --recursive https://github.com/kdeldycke/dotfiles.git


Development
-----------

Update to latest sub-modules:

    $ git submodule init
    $ git submodule update --remote --merge

In one terminal, run:

    $ fab regenerate

And in another:

    $ fab serve

Then go to [http://localhost:8000](http://localhost:8000).


Deployment
----------

Setup `s3cmd`:

    $ s3cmd --configure

We use `make` for deployment as `fab` is not wired yet:

    $ make s3_upload


TODO
----

  * Re-use previous artworks from Maomium ?
  * Test different ad placements: http://news.ycombinator.com/item?id=4974511
  * Get rid of /year/month/ for articles ? Or get rid of month only ?
  * Deduplicate articles' tags.
  * Fix Google Analytics bouncing rate ? See: http://drawingablank.me/blog/fix-your-bounce-rate.html
  * Migrate Resume from Google Docs to web-based page in Pelican ? Inspiration:
      * https://wrapbootstrap.com/theme/simply-minimal-responsive-resume-WB0DCP565
  * Automate and script S3 deployment with:
      * https://github.com/heyimalex/s3tup
      * https://github.com/boto/boto
  * Migrate `/content/extra/htaccess` rules to [S3 routing rules](http://docs.aws.amazon.com/AmazonS3/latest/dev/HowDoIWebsiteConfiguration.html#configure-bucket-as-website-routing-rule-syntax) and/or use https://pypi.python.org/pypi/pelican-alias for redirects ?
  * Activate AWS CloudFront ? See:
      * http://paulstamatiou.com/hosting-on-amazon-s3-with-cloudfront/
      * http://pmac.io/2014/06/pelican-s3-cloudfront/
  * Create an autoindex plugin: activate it to produce index of /documents, then get rid of
    htaccess-static.


License
-------

The content of this repository is copyrighted (c) 2004-2015 Kevin Deldycke.

Unless contrary mention, the licensing terms below applies:

  * Code and software released under [GNU/GPL licence, v2.0
    ](http://www.fsf.org/licensing/licenses/gpl.html).
  * Other content published under [Creative Commons Attribution-Share Alike 3.0
    license](http://creativecommons.org/licenses/by-sa/3.0/).

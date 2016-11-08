Kevin Deldycke's blog
=====================

These are the source files of the content of my
[blog](http://kevin.deldycke.com), which is powered by
[Pelican](http://getpelican.com), a static site generator written in Python.

The theme it uses is called [Plumage](https://github.com/kdeldycke/plumage).


Installation
------------

Fetch a copy of the repository:

    $ git clone --recursive https://github.com/kdeldycke/kevin-deldycke-blog.git

Install dependencies:

    $ cd ./kevin-deldycke-blog
    $ pip install -r ./requirements.txt


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

### Content

  * Migrate Resume from Google Docs to web-based page in Pelican ? Inspiration:
      * https://wrapbootstrap.com/theme/simply-minimal-responsive-resume-WB0DCP565
  * Create an autoindex plugin: activate it to produce index of /documents, then get rid of
    htaccess-static.
  * Fix Google Analytics bouncing rate ? See: http://drawingablank.me/blog/fix-your-bounce-rate.html
  * Get rid of /year/month/ for articles ? Or get rid of month only ?
  * Add links to yearly/monthly indexes in archives
  * Try to paginate monthly and yearly archives
  * Reuse edit link logic from https://github.com/pmclanahan/pelican-edit-url ?
  * Migrate `/content/extra/htaccess` rules to [S3 routing rules](http://docs.aws.amazon.com/AmazonS3/latest/dev/HowDoIWebsiteConfiguration.html#configure-bucket-as-website-routing-rule-syntax) and/or use https://pypi.python.org/pypi/pelican-alias for redirects ?

### Deployment

  * Automate and script S3 deployment with:
      * https://github.com/heyimalex/s3tup
      * https://github.com/boto/boto
  * Activate AWS CloudFront ? See:
      * http://paulstamatiou.com/hosting-on-amazon-s3-with-cloudfront/
      * http://pmac.io/2014/06/pelican-s3-cloudfront/

### Theme

  * Re-use previous artworks from Maomium ?
  * Test different ad placements: http://news.ycombinator.com/item?id=4974511
  * Use a big carousel for front-page articles (ex: http://twitter.github.com/bootstrap/examples/carousel.html ) + a bit of http://srobbin.com/jquery-plugins/backstretch/ to keep aspect-ratio
  * Check some web-dev essentials:
      * http://webdevchecklist.com/
      * https://github.com/getpelican/pelican-plugins/tree/master/w3c_validate
      * https://github.com/dypsilon/frontend-dev-bookmarks
  * Use custom jinja filters instead of heavy tag soup in my theme ? Example: https://bitbucket.org/sirex/blog/src/32c192ff7a10/pelican.conf.py#cl-53
  * Add progressive image loading. See:
      * https://github.com/vvo/lazyload
      * https://github.com/tuupola/jquery_lazyload
      * https://github.com/luis-almeida/unveil
  * Concatenate and minify CSS and Javascript. See:
      * https://pypi.python.org/pypi/mincss
      * http://ralsina.com.ar/weblog/posts/mincss-is-amazing.html
      * https://pypi.python.org/pypi/pelican-minify
      * https://github.com/getpelican/pelican-plugins/tree/master/assets
  * Inline and embed all CSS in the page ? See: http://www.peterbe.com/plog/100-percent-inline-css
  * Use LESS version of bootstrap for cleaner customizations ?
  * Look at app-template for code inspiration and ideas:
      *  https://github.com/nprapps/app-template/blob/master/templates/_base.html
      *  https://github.com/nprapps/app-template/blob/master/render_utils.py
  * Make Masonry responsive ? See:
      * http://osvaldas.info/responsive-jquery-masonry-or-pinterest-style-layout
      * http://deanclatworthy.com/2012/09/responsive-twitter-bootstrap-masonry/
      * http://www.maurizioconventi.com/2012/06/19/responsive-example-integrating-twitter-bootstrap-and-jquery-masonry/
  * Add progressive loading on masonery layouts. See: http://masonry.desandro.com/demos/infinite-scroll.html
  * Generate thumbnails in article content. See:
      * https://github.com/getpelican/pelican-plugins/pull/40
      * https://github.com/getpelican/pelican-plugins/pull/43
  * Auto-enhance created thumbnails ? See: https://news.ycombinator.com/item?id=5999201
  * Group contiguous images in a post into a tiled galery:
      * as in WordPress' jetpack plugin: https://github.com/crowdfavorite-mirrors/wp-jetpack/tree/master/modules/tiled-gallery
      * or thanks to https://github.com/jakobholmelund/fitpicsjs
  * Replace MGlass zoom icon overlay with pure CSS. Inspirations:
      * Cover effect at http://h5bp.github.io/Effeckt.css/dist/captions.html
      * http://codepen.io/Twikito/pen/Jeaub
      * To center the zoom icon, we can use one of these trick: http://codepen.io/shshaw/full/gEiDt
  * CSS typography: http://www.newnet-soft.com/blog/csstypography
  * Upgrade to Bootstrap 4.x
  * Image gallery inspiration: https://github.com/Jack000/Expose


License
-------

The content of this repository is copyrighted (c) 2004-2016 Kevin Deldycke.

Unless contrary mention, the content of this repository is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC
BY-NC-SA 4.0) license](LICENSE).

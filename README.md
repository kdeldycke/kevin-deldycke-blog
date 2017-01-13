Kevin Deldycke's blog
=====================

These are the source files of the content of my
[blog](https://kevin.deldycke.com), which is powered by
[Pelican](https://getpelican.com), a static site generator written in Python.

The theme it uses is called [Plumage](https://github.com/kdeldycke/plumage).


Installation
------------

Fetch a copy of the repository:

    $ git clone --recursive https://github.com/kdeldycke/kevin-deldycke-blog.git
    $ cd ./kevin-deldycke-blog

To fetch and/or reset submodules to their commited reference:

    $ git submodule update --init --recursive

Install dependencies:

    $ pip install -r ./requirements.txt


Development
-----------

Update to latest submodules:

    $ git submodule init
    $ git submodule update --remote --merge

In one terminal, run:

    $ fab regenerate

And in another:

    $ fab serve

Then go to [http://localhost:8000](http://localhost:8000).


Deployment
----------

Prepare site for publishing:

    $ pelican ./content -o ./output -s ./publishconf.py --verbose

Setup AWS CLI:

    $ aws configure
    AWS Access Key ID [None]: (...)
    AWS Secret Access Key [None]: (...)
    Default region name [None]:
    Default output format [None]:

    $ cat ~/.aws/credentials
    [default]
    aws_access_key_id = (...)
    aws_secret_access_key = (...)

    $ cat ~/.aws/config
    [default]

Create the destination bucket if it doesn't exist yet:

    $ aws s3 mb s3://kevin.deldycke.com

Setup bucket:

    $ aws s3 website s3://kevin.deldycke.com --index-document index.html --error-document 500-error/index.html

Upload content to S3 bucket ([full
documentation](https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html)):

    $ aws s3 sync ./output s3://kevin.deldycke.com --delete --grants read=uri=http://acs.amazonaws.com/groups/global/AllUsers full=emailaddress=kevin@deldycke.com

And to check metadata, for the `index.html` file at the root for example:

    $ aws s3api head-object --bucket kevin.deldycke.com --key index.html

Register and install a new [Let's Encrypt](https://letsencrypt.org)
certificate:

    $ AWS_ACCESS_KEY_ID="(...)" AWS_SECRET_ACCESS_KEY="(...)" certbot --agree-tos -a certbot-s3front:auth --certbot-s3front:auth-s3-bucket kevin.deldycke.com -i certbot-s3front:installer --certbot-s3front:installer-cf-distribution-id (...) -d kevin.deldycke.com --config-dir ./letsencrypt --logs-dir ./letsencrypt/logs --work-dir ./letsencrypt --non-interactive --email kevin@deldycke.com


TODO
----

### Content

  * Migrate Resume from Google Docs to web-based page in Pelican ? Inspiration:
      * https://wrapbootstrap.com/theme/simply-minimal-responsive-resume-WB0DCP565
  * Create an autoindex plugin: activate it to produce index of /documents, then get rid of
    htaccess-static.
  * Fix Google Analytics bouncing rate ? See: https://drawingablank.me/blog/fix-your-bounce-rate.html
  * Get rid of /year/month/ for articles ? Or get rid of month only ?
  * Add links to yearly/monthly indexes in archives
  * Try to paginate monthly and yearly archives
  * Reuse edit link logic from https://github.com/pmclanahan/pelican-edit-url ?
  * Migrate `/content/extra/htaccess` rules to [S3 routing rules](https://docs.aws.amazon.com/AmazonS3/latest/dev/HowDoIWebsiteConfiguration.html#configure-bucket-as-website-routing-rule-syntax) and/or use https://pypi.python.org/pypi/pelican-alias for redirects ?

### Deployment

  * Activate AWS CloudFront ? See:
      * https://paulstamatiou.com/hosting-on-amazon-s3-with-cloudfront/
      * https://pmac.io/2014/06/pelican-s3-cloudfront/

### Theme

  * Re-use previous artworks from Maomium ?
  * Test different ad placements: https://news.ycombinator.com/item?id=4974511
  * Use a big carousel for front-page articles (ex: https://twitter.github.com/bootstrap/examples/carousel.html ) + a bit of https://srobbin.com/jquery-plugins/backstretch/ to keep aspect-ratio
  * Check some web-dev essentials:
      * https://webdevchecklist.com/
      * https://github.com/getpelican/pelican-plugins/tree/master/w3c_validate
      * https://github.com/dypsilon/frontend-dev-bookmarks
  * Use custom jinja filters instead of heavy tag soup in my theme ? Example: https://bitbucket.org/sirex/blog/src/32c192ff7a10/pelican.conf.py#cl-53
  * Add progressive image loading. See:
      * https://github.com/vvo/lazyload
      * https://github.com/tuupola/jquery_lazyload
      * https://github.com/luis-almeida/unveil
  * Concatenate and minify CSS and Javascript. See:
      * https://pypi.python.org/pypi/mincss
      * https://ralsina.com.ar/weblog/posts/mincss-is-amazing.html
      * https://pypi.python.org/pypi/pelican-minify
      * https://github.com/getpelican/pelican-plugins/tree/master/assets
  * Inline and embed all CSS in the page ? See: https://www.peterbe.com/plog/100-percent-inline-css
  * Use LESS version of bootstrap for cleaner customizations ?
  * Look at app-template for code inspiration and ideas:
      *  https://github.com/nprapps/app-template/blob/master/templates/_base.html
      *  https://github.com/nprapps/app-template/blob/master/render_utils.py
  * Make Masonry responsive ? See:
      * https://osvaldas.info/responsive-jquery-masonry-or-pinterest-style-layout
      * https://deanclatworthy.com/2012/09/responsive-twitter-bootstrap-masonry/
      * https://www.maurizioconventi.com/2012/06/19/responsive-example-integrating-twitter-bootstrap-and-jquery-masonry/
  * Add progressive loading on masonery layouts. See: https://masonry.desandro.com/demos/infinite-scroll.html
  * Generate thumbnails in article content. See:
      * https://github.com/getpelican/pelican-plugins/pull/40
      * https://github.com/getpelican/pelican-plugins/pull/43
  * Auto-enhance created thumbnails ? See: https://news.ycombinator.com/item?id=5999201
  * Group contiguous images in a post into a tiled galery:
      * as in WordPress' jetpack plugin: https://github.com/crowdfavorite-mirrors/wp-jetpack/tree/master/modules/tiled-gallery
      * or thanks to https://github.com/jakobholmelund/fitpicsjs
  * Replace MGlass zoom icon overlay with pure CSS. Inspirations:
      * Cover effect at https://h5bp.github.io/Effeckt.css/dist/captions.html
      * https://codepen.io/Twikito/pen/Jeaub
      * To center the zoom icon, we can use one of these trick: https://codepen.io/shshaw/full/gEiDt
  * CSS typography: https://www.newnet-soft.com/blog/csstypography
  * Upgrade to Bootstrap 4.x
  * Image gallery inspiration: https://github.com/Jack000/Expose


License
-------

The content of this repository is copyrighted (c) 2004-2017 Kevin Deldycke.

Unless contrary mention, the content of this repository is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC
BY-NC-SA 4.0) license](LICENSE).

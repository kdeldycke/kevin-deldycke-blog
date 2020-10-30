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

To fetch and/or reset submodules to their committed reference:

    $ git submodule update --init --recursive

Install dependencies:

    $ python -m pip install --upgrade pip poetry
    $ poetry install


Development
-----------

Update to latest submodules:

    $ git submodule init
    $ git submodule update --remote --merge

In one terminal, run:

    $ pelican --verbose ./content

And in another:

    $ pelican --verbose --listen
    (...)
    -> Serving at port 8000, server 127.0.0.1.

Then go to [http://localhost:8000](http://localhost:8000).



TODO
----

### Content

  * Migrate Resume from Google Docs to web-based page in Pelican ? Inspiration:
      * https://wrapbootstrap.com/theme/simply-minimal-responsive-resume-WB0DCP565
  * Get rid of /year/month/ for articles ? Or get rid of month only ?
  * Reuse edit link logic from https://github.com/pmclanahan/pelican-edit-url ?

### Theme

  * Re-use previous artworks from Maomium ?
  * Test different ad placements: https://news.ycombinator.com/item?id=4974511
  * Use a big carousel for front-page articles (ex: https://twitter.github.com/bootstrap/examples/carousel.html ) + a bit of https://srobbin.com/jquery-plugins/backstretch/ to keep aspect-ratio
  * Check some web-dev essentials:
      * https://webdevchecklist.com/
      * https://github.com/getpelican/pelican-plugins/tree/master/w3c_validate
      * https://github.com/dypsilon/frontend-dev-bookmarks
  * Use custom jinja filters instead of heavy tag soup in my theme ? Example: https://bitbucket.org/sirex/blog/src/32c192ff7a10/pelican.conf.py#cl-53
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
  * Generate thumbnails in article content. See:
      * https://github.com/getpelican/pelican-plugins/pull/40
      * https://github.com/getpelican/pelican-plugins/pull/43
  * Auto-enhance created thumbnails ? See: https://news.ycombinator.com/item?id=5999201


License
-------

The content of this repository is copyrighted (c) 2004-2017 Kevin Deldycke.

Unless contrary mention, the content of this repository is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC
BY-NC-SA 4.0) license](LICENSE).

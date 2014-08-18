#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kevin Deldycke'
SITENAME = u'Kevin Deldycke'

PATH = 'content'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'
LOCALE = 'C'
# Don't forget to install "pip install mdx_video"
MD_EXTENSIONS = ['codehilite', 'extra', 'video']
TYPOGRIFY = True

# Do not publish articles set in the future
WITH_FUTURE_DATES = False
# Force Pelican to use the file name as the slug, instead of derivating it from the title.
FILENAME_METADATA = '(?P<slug>.*)'

# Force the same URL structure as WordPress
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
ARTICLE_DIR = 'posts'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'
PAGE_DIR = 'pages'

TEMPLATE_PAGES = {
    'templates/videos.html': 'video/index.html',
    'templates/code.html': 'code/index.html',
    'templates/themes.html': 'themes/index.html',
}

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'

YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags, categories and archives are Direct Templates, so they don't have a
# <NAME>_URL option.
TAGS_SAVE_AS = 'tags/index.html'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_SAVE_AS = 'archives/index.html'

# Deactivate author URLs
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False

# Deactivate localization
ARTICLE_LANG_SAVE_AS = False
PAGE_LANG_SAVE_AS = False

FEED_RSS = 'feed/index.html'
FEED_ATOM = 'feed/atom/index.html'
FEED_ALL_RSS = False
FEED_ALL_ATOM = False
TRANSLATION_FEED_RSS = False
TRANSLATION_FEED_ATOM = False

#http://kevin.deldycke.com/tag/openerp/feed/
TAG_FEED_RSS = 'tag/%s/feed/index.html'
TAG_FEED_ATOM = 'tag/%s/feed/atom/index.html'

#http://example.com/category/categoryname/feed
CATEGORY_FEED_RSS = 'category/%s/feed/index.html'
CATEGORY_FEED_ATOM = 'category/%s/feed/atom/index.html'

FEED_MAX_ITEMS = 5
DEFAULT_CATEGORY = 'English'
DEFAULT_DATE_FORMAT = '%b. %d, %Y'
REVERSE_ARCHIVE_ORDER = True
DISPLAY_PAGES_ON_MENU = False

# Pagination
DEFAULT_ORPHANS = 2
DEFAULT_PAGINATION = 5
# TODO: set PAGINATION_PATTERNS to produce nice URLs like index/page/23/ instead of indexXX.html

THEME = "plumage"

STATIC_PATHS = [
    'uploads',
    'documents',
    'extra',
]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/htaccess': {'path': '.htaccess'},
    'extra/htaccess-static': {'path': 'documents/.htaccess'},
}

PLUGIN_PATH = 'plugins'
PLUGINS = [
    'related_posts',
    #'thumbnailer',
    'neighbors',
    'sitemap',
]


### Plugin-specific settings

RELATED_POSTS_MAX = 3

# TODO: align default SITEMAP config to http://wordpress.org/extend/plugins/google-sitemap-generator/stats/
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

IMAGE_PATH = "uploads"
#THUMBNAIL_DIR = ""
THUMBNAIL_SIZES = {
    'thumbnail': '462x?',
}
DEFAULT_TEMPLATE = """<a href="{url}" class="zoomable" title="{filename}"><img src="{thumbnail}" alt="{filename}"></a>"""


### Theme-specific settings

SITE_THUMBNAIL = '/uploads/2006/avatar-orig.png'
SITE_THUMBNAIL_TEXT = 'Official avatar since MMIV'

SITESUBTITLE = "Open-Source Software Engineer"

MENUITEMS = (
    ('Home', '/'),
    ('Videos', '/video/'),
    ('Code', '/code/'),
    ('Themes', '/themes/'),
    ('About', '/about/'),
)

GOOGLE_SEARCH = 'partner-pub-0142056597033291:1880158713'

LEFT_SIDEBAR = """
    <!--<div data-spy="affix" data-offset-top="0">-->
    <!--<h4>Sponsors</h4>-->
    <script type="text/javascript"><!--
      google_ad_client = "pub-0142056597033291";
      google_ad_slot = "9501596707";
      google_ad_width = 160;
      google_ad_height = 600;
      //-->
    </script>
    <script type="text/javascript" src="http://pagead2.googlesyndication.com/pagead/show_ads.js"></script>
    <!--</div>-->
    """

ARTICLE_EDIT_LINK = 'https://github.com/kdeldycke/kevin-deldycke-blog/edit/master/content/posts/%(slug)s.md'

SOCIAL_TITLE = "Contact"
SOCIAL = (
    ('@kdeldycke', 'http://twitter.com/kdeldycke'),
)

LINKS_TITLE = "Professional profiles"
LINKS = (
    ('PDF resume', 'http://docs.google.com/document/export?format=pdf&amp;id=1XaJgwRAhxHDuBSD-JqE--8WKGx0uTasa6IOU4IFBeKg'),
    ('Careers 2.0', 'http://careers.stackoverflow.com/kdeldycke'),
    ('LinkedIn', 'http://linkedin.com/in/kevindeldycke/en'),
    ('Viadeo', 'http://viadeo.com/fr/profile/kevin.deldycke'),
)

COPYRIGHT = "Unless contrary mention, the licensing terms below applies:<br/>Code and software released under <a href='http://www.fsf.org/licensing/licenses/gpl.html'>GNU/GPL licence v2.0</a>;<br/>Other content published under <a href='http://creativecommons.org/licenses/by-sa/3.0/'>Creative Commons Attribution-Share Alike 3.0 license</a>."
DISQUS_SITENAME = 'kevin-deldycke-blog'
GOOGLE_ANALYTICS = 'UA-657524-1'
GOOGLE_ANALYTICS_DOMAIN = 'deldycke.com'

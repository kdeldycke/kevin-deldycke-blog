#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

AUTHOR = u'Kevin Deldycke'
SITENAME = u'Kevin Deldycke'

PATH = 'content'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'
LOCALE = 'C'
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'mdx_video': {},
        'mdx_titlecase': {},
    },
    'output_format': 'html5',
    # Allow numbered lists to not start with 1. Used in following article:
    # http://kevin.deldycke.com/2016/12/falsehoods-programmers-believe-about-falsehoods-lists/
    # See: https://pythonhosted.org/Markdown/reference.html#lazy_ol
    'lazy_ol': False,
}
TYPOGRIFY = True

# Do not publish articles set in the future
WITH_FUTURE_DATES = False

# Force Pelican to use the file name as the slug, instead of derivating it from
# the title.
SLUGIFY_SOURCE = 'basename'

# Force the same URL structure as WordPress
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
ARTICLE_PATHS = ['posts']

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'
PAGE_PATHS = ['pages']

TEMPLATE_PAGES = {
    'templates/videos.html': 'video/index.html',
    'templates/code.html': 'code/index.html',
    'templates/themes.html': 'themes/index.html',
}

DIRECT_TEMPLATES = [
    'index', 'tags', 'categories', 'authors', 'archives', 'search']

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
ARTICLE_LANG_SAVE_AS = None
DRAFT_LANG_SAVE_AS = None
PAGE_LANG_SAVE_AS = None

FEED_RSS = 'feed/index.html'
FEED_ATOM = 'feed/atom/index.html'
FEED_ALL_RSS = None
FEED_ALL_ATOM = None
TRANSLATION_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# http://kevin.deldycke.com/tag/openerp/feed/
TAG_FEED_RSS = 'tag/%s/feed/index.html'
TAG_FEED_ATOM = 'tag/%s/feed/atom/index.html'

# http://example.com/category/categoryname/feed
CATEGORY_FEED_RSS = 'category/%s/feed/index.html'
CATEGORY_FEED_ATOM = 'category/%s/feed/atom/index.html'

FEED_MAX_ITEMS = 5
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'English'
DEFAULT_DATE_FORMAT = '%b. %d, %Y'
REVERSE_ARCHIVE_ORDER = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Pagination
DEFAULT_ORPHANS = 2
DEFAULT_PAGINATION = 5
# TODO: set PAGINATION_PATTERNS to produce nice URLs like index/page/23/
# instead of indexXX.html

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

PLUGIN_PATHS = ['plugins-core']
PLUGINS = [
    'deadlinks',
    'related_posts',
    # 'thumbnailer',
    'tipue_search',
    'neighbors',
    'sitemap',
]


### Plugin-specific settings

DEADLINK_VALIDATION = True

RELATED_POSTS_MAX = 3

IMAGE_PATH = "uploads"
#THUMBNAIL_DIR = ""
THUMBNAIL_SIZES = {
    'thumbnail': '462x?',
}
DEFAULT_TEMPLATE = """<a href="{url}" class="zoomable" title="{filename}">
<img src="{thumbnail}" alt="{filename}"></a>"""


### Theme-specific settings

SITE_THUMBNAIL = '/uploads/2015/profile-photo-squared-thumbnail.jpg'
SITE_THUMBNAIL_TEXT = 'Might come with a beard'

SITESUBTITLE = "Professional Yak Shaver"

MENUITEMS = (
    ('Home', '/'),
    ('Videos', '/video/'),
    ('Code', '/code/'),
    ('Themes', '/themes/'),
    ('About', '/about/'),
)

TIPUE_SEARCH = True

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
    <script type="text/javascript"
        src="http://pagead2.googlesyndication.com/pagead/show_ads.js"></script>
    <!--</div>-->
    """

ARTICLE_EDIT_LINK = 'https://github.com/kdeldycke/kevin-deldycke-blog/edit/master/content/posts/%(slug)s.md'

SOCIAL_WIDGET_NAME = "Online presence"
SOCIAL = (
    ("Twitter", 'https://twitter.com/kdeldycke'),
    ("Github", 'https://github.com/kdeldycke'),
    ("Keybase.io", 'https://keybase.io/kdeldycke'),
)

LINKS_WIDGET_NAME = "Professional profiles"
LINKS = (
    ('LinkedIn', 'https://linkedin.com/in/kevindeldycke/en'),
    ('PDF resume', 'http://docs.google.com/document/export?format=pdf&amp;id='
     '1XaJgwRAhxHDuBSD-JqE--8WKGx0uTasa6IOU4IFBeKg'),
)

COPYRIGHT = """Unless contrary mentioned, the content of this site is published
under a <a rel='license'
href='https://creativecommons.org/licenses/by-nc-sa/4.0/'>Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International license</a>."""

DISQUS_SITENAME = 'kevin-deldycke-blog'

GOOGLE_ANALYTICS = 'UA-657524-1'

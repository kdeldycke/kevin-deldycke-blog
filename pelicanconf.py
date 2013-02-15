#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Kevin Deldycke'
SITENAME = u'Kevin Deldycke'
SITEURL = 'http://kevin.deldycke.com'
SITESUBTITLE = "Open-Source Software Engineer"

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'
LOCALE = 'C'
MARKUP = 'md'
# Don't forget to install "pip install mdx_video"
MD_EXTENSIONS = ['codehilite', 'extra', 'video']

# TODO: explore
#DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'archives',]
#PAGINATED_DIRECT_TEMPLATES = ['index',]

# Force the same URL structure as WordPress
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
ARTICLE_DIR = 'posts'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'
PAGE_DIR = 'pages'

TEMPLATE_PAGES = {
  'templates/code.html': 'code/index.html',
  }

# Force Pelican to use the file name as the slug, instead of derivating it from the title.
FILENAME_METADATA = '(?P<slug>.*)'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'

# Deactivate author URLs
AUTHOR_SAVE_AS = False

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

FEED_MAX_ITEMS = 10
DEFAULT_CATEGORY = 'English'
DEFAULT_ORPHANS = 2
DEFAULT_PAGINATION = 5
DEFAULT_DATE_FORMAT = '%b. %d, %Y'
REVERSE_ARCHIVE_ORDER = True
DISPLAY_PAGES_ON_MENU = False

DISQUS_SITENAME = "kevin-deldycke-blog"
GOOGLE_ANALYTICS = "UA-657524-1"

THEME = "theme"

STATIC_PATHS = [
  'uploads',
  'documents',
  ]

FILES_TO_COPY = (
    ('extra/favicon.ico', 'favicon.ico'),
    ('extra/robots.txt', 'robots.txt'),
    ('extra/htaccess', '.htaccess'),
    ('extra/htaccess-static', 'static/.htaccess'),
    )

MENUITEMS = (
    ('Home', '/'),
    ('Videos', '/video/'),
    ('Code', '/code/'),
    ('Themes', '/themes/'),
    ('About', '/about/'),
    )

# Blogroll
LINKS =  (
    ('Categories', '/categories.html'),
    ('Archives', '/archives.html'),
    ('Tags', '/tags.html'),
    )

PLUGINS = [
    'pelican.plugins.sitemap',
    ]

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

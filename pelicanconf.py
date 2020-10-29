#!/usr/bin/env python
# -*- coding: utf-8 -*-

import plumage

SITEURL = "http://localhost:8000"
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True

AUTHOR = SITENAME = "Kevin Deldycke"

PATH = "content"

TIMEZONE = "Europe/Paris"
DEFAULT_LANG = "en"
MARKDOWN = {
    "extension_configs": {
        # https://python-markdown.github.io/extensions/#officially-supported-extensions
        "markdown.extensions.abbr": {},
        # Example of admonition use at:
        # https://github.com/kdeldycke/kevin-deldycke-blog/blob/main/content/posts/python-ultimate-regular-expression-to-catch-html-tags.md
        "markdown.extensions.admonition": {},
        "markdown.extensions.attr_list": {},
        "markdown.extensions.def_list": {},
        "markdown.extensions.footnotes": {},
        "markdown.extensions.md_in_html": {},
        "markdown.extensions.meta": {},
        # Allow numbered lists to not start with 1. Used in following article:
        # https://kevin.deldycke.com/2016/12/falsehoods-programmers-believe-about-falsehoods-lists/
        "markdown.extensions.sane_lists": {},
        "markdown.extensions.smarty": {},
        "markdown.extensions.tables": {},
        "markdown.extensions.toc": {
            "permalink": True,
            # Style aligns to Plumage theme at:
            # https://github.com/kdeldycke/plumage/blob/v1.1.0/plumage/static/css/style.css#L184-L202
            "permalink_class": "headerlink text-decoration-none small pl-2",
        },
        "mdx_titlecase.mdx_titlecase:TitlecaseExtension": {},
        "mdx_video": {},
        # https://facelessuser.github.io/pymdown-extensions/
        "pymdownx.betterem": {},
        "pymdownx.caret": {},
        "pymdownx.emoji": {},
        "pymdownx.highlight": {},
        "pymdownx.keys": {},
        "pymdownx.magiclink": {},
        "pymdownx.smartsymbols": {},
        "pymdownx.superfences": {
            # No need for magic indention-based code blocks: all ours are
            # delimited by fences anyway.
            "disable_indented_code_blocks": True,
        },
    },
    "output_format": "html5",
}
TYPOGRIFY = True

# Do not publish articles set in the future
WITH_FUTURE_DATES = False

# Force Pelican to use the file name as the slug, instead of derivating it from
# the title.
SLUGIFY_SOURCE = "basename"

# Force the same URL structure as WordPress
ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = ARTICLE_URL + "index.html"
ARTICLE_PATHS = ["posts"]

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = PAGE_URL + "index.html"
PAGE_PATHS = ["pages"]

TEMPLATE_PAGES = {
    "templates/themes.html": "themes/index.html",
}

DIRECT_TEMPLATES = ["index", "tags", "categories", "authors", "archives", "search"]

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = TAG_URL + "index.html"

CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = CATEGORY_URL + "index.html"

YEAR_ARCHIVE_SAVE_AS = "{date:%Y}/index.html"
MONTH_ARCHIVE_SAVE_AS = "{date:%Y}/{date:%m}/index.html"

# Tags, categories and archives are Direct Templates, so they don't have a
# <NAME>_URL option.
TAGS_SAVE_AS = "tags/index.html"
CATEGORIES_SAVE_AS = "categories/index.html"
ARCHIVES_SAVE_AS = "archives/index.html"

# Deactivate author URLs
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False

# Deactivate localization
ARTICLE_LANG_SAVE_AS = None
DRAFT_LANG_SAVE_AS = None
PAGE_LANG_SAVE_AS = None

FEED_RSS = "feed/index.html"
FEED_ATOM = "feed/atom/index.html"
FEED_ALL_RSS = None
FEED_ALL_ATOM = None
TRANSLATION_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# https://kevin.deldycke.com/tag/openerp/feed/
TAG_FEED_RSS = "tag/{slug}/feed/index.html"
TAG_FEED_ATOM = "tag/{slug}/feed/atom/index.html"

# https://example.com/category/categoryname/feed
CATEGORY_FEED_RSS = "category/{slug}/feed/index.html"
CATEGORY_FEED_ATOM = "category/{slug}/feed/atom/index.html"

FEED_MAX_ITEMS = 5
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = "English"
DEFAULT_DATE_FORMAT = "%b. %d, %Y"
REVERSE_ARCHIVE_ORDER = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Pagination
DEFAULT_ORPHANS = 2
DEFAULT_PAGINATION = 5
# TODO: set PAGINATION_PATTERNS to produce nice URLs like index/page/23/
# instead of indexXX.html

THEME = plumage.get_path()

STATIC_PATHS = [
    "uploads",
    "documents",
    "extra",
]

EXTRA_PATH_METADATA = {
    "extra/ads.txt": {"path": "ads.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/htaccess": {"path": ".htaccess"},
    "extra/htaccess-static": {"path": "documents/.htaccess"},
}

PLUGIN_PATHS = [
    "pelican-deadlinks",
]
# Once all plugins hard-linked in this repository by the way of git submodules
# gets their own package, we can get rid of PLUGIN_PATHS and set PLUGINS to
# None. That way all plugins installed by poetry will be auto-discovered by
# Pelican.
PLUGINS = [
    # deadlink plugin seems temporarily broken and produce this fatal error:
    # CRITICAL: AttributeError: module 'deadlinks' has no attribute 'register'
    # "deadlinks",
    "pelican.plugins.seo",
    "pelican.plugins.similar_posts",
    "pelican.plugins.neighbors",
    "pelican.plugins.sitemap",
    "pelican.plugins.thumbnailer",
    "pelican.plugins.tipue_search",
]


# ----- Plugin-specific settings

# deadlinks
DEADLINK_VALIDATION = True

# seo
SEO_REPORT = True
SEO_ENHANCER = True

# similar_posts
SIMILAR_POSTS_MAX_COUNT = 3

# thumbnailer
IMAGE_PATH = "uploads"
# THUMBNAIL_DIR = ""
THUMBNAIL_SIZES = {
    "thumbnail": "462x?",
}
DEFAULT_TEMPLATE = """<a href="{url}" class="zoomable" title="{filename}">
<img src="{thumbnail}" alt="{filename}"></a>"""


# ----- Theme-specific settings

SITE_THUMBNAIL = "/uploads/2015/profile-photo-squared-thumbnail.jpg"
SITE_THUMBNAIL_TEXT = "Might come with a beard"

SITESUBTITLE = "Professional Yak Shaver"

MENUITEMS = (
    ("Home", "/"),
    ("Themes", "/themes/"),
    ("About", "/about/"),
)

TIPUE_SEARCH = True

LEFT_SIDEBAR = """
    <!--<div data-spy="affix" data-offset-top="0">-->
    <!--<h4>Sponsors</h4>-->
    <script async
        src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
    <!-- Responsive Ad -->
    <ins class="adsbygoogle"
         style="display:block"
         data-ad-client="ca-pub-0142056597033291"
         data-ad-slot="9726265119"
         data-ad-format="auto"></ins>
    <script>
    (adsbygoogle = window.adsbygoogle || []).push({});
    </script>
    <!--</div>-->
    """

ARTICLE_EDIT_LINK = (
    "https://github.com/kdeldycke/kevin-deldycke-blog/edit/main/content/posts/"
    "%(slug)s.md"
)

SOCIAL_WIDGET_NAME = "Online presence"
SOCIAL = (
    ("Twitter", "https://twitter.com/kdeldycke"),
    ("GitHub", "https://github.com/kdeldycke"),
    ("Hacker News", "https://news.ycombinator.com/user?id=kdeldycke"),
    ("Open Hub", "https://www.openhub.net/accounts/kevin"),
    ("YouTube", "https://www.youtube.com/channel/UCW0k7La7M8q-_yp3RYfNhFw/"),
)

LINKS_WIDGET_NAME = "Professional profiles"
LINKS = (("LinkedIn", "https://linkedin.com/in/kevindeldycke/en"),)

COPYRIGHT = """Unless contrary mentioned, the content of this site is published
under a <a class="text-dark" rel="license"
href="https://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International license</a>."""

DISQUS_SITENAME = "kevin-deldycke-blog"

GOOGLE_ANALYTICS = "UA-657524-1"

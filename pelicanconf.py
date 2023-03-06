# XXX Use local plumage copy for dev
# from importlib.machinery import SourceFileLoader
# from pathlib import Path
# SourceFileLoader(
#     "plumage",
#     str(Path("../plumage/plumage/__init__.py").resolve())
# ).load_module()

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
        },
        # XXX broken on Python 3.9
        # "mdx_titlecase.mdx_titlecase:TitlecaseExtension": {},
        "mdx_video": {},
        # https://facelessuser.github.io/pymdown-extensions/
        "pymdownx.betterem": {},
        "pymdownx.caret": {},
        "pymdownx.emoji": {},
        "pymdownx.keys": {},
        "pymdownx.magiclink": {},
        "pymdownx.smartsymbols": {},
    },
    "output_format": "html5",
}
TYPOGRIFY = True

# Code block renderers.
SUPERFENCES = True
if SUPERFENCES:
    code_config = {
        "pymdownx.highlight": {
            "linenums": True,
            "linenums_style": "pymdownx-inline",
        },
        "pymdownx.superfences": {
            # No need for magic indention-based code blocks: all ours are
            # delimited by fences anyway.
            "disable_indented_code_blocks": True,
        },
    }
else:
    code_config = {
        "markdown.extensions.codehilite": {
            "linenums": True,
            "linenos": "inline",
            "linespans": "coderow",
            "lineanchors": "L",
            "anchorlinenos": True,
            "wrapcode": True,
        },
        "markdown.extensions.fenced_code": {},
    }
MARKDOWN["extension_configs"].update(code_config)  # type: ignore[attr-defined]

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
PAGE_SAVE_AS = "{slug}.html"
PAGE_PATHS = ["pages"]

TEMPLATE_PAGES = {
    "templates/themes.html": "themes.html",
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
# Note: ``DIRECT_TEMPLATES`` work a bit differently and only the ``_SAVE_AS`` settings
# are available. See: https://docs.getpelican.com/en/latest/settings.html#url-settings
ARCHIVES_SAVE_AS = "archives.html"
CATEGORIES_SAVE_AS = "categories.html"
TAGS_SAVE_AS = "tags.html"
# Deactivate author URLs
AUTHORS_SAVE_AS = False
AUTHOR_SAVE_AS = False

# Deactivate localization
ARTICLE_LANG_SAVE_AS = None
DRAFT_LANG_SAVE_AS = None
PAGE_LANG_SAVE_AS = None

FEED_RSS = "feed.rss"
FEED_ATOM = "feed.atom"
FEED_ALL_RSS = None
FEED_ALL_ATOM = None
TRANSLATION_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

TAG_FEED_RSS = "tag/{slug}/feed.rss"
TAG_FEED_ATOM = "tag/{slug}/feed.atom"

CATEGORY_FEED_RSS = "category/{slug}/feed.rss"
CATEGORY_FEED_ATOM = "category/{slug}/feed.atom"

FEED_MAX_ITEMS = 5
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = "English"
DEFAULT_DATE_FORMAT = "%b. %d, %Y"
REVERSE_ARCHIVE_ORDER = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Pagination.
DEFAULT_ORPHANS = 2
DEFAULT_PAGINATION = 5
# Deactivate pagination everywhere but the index page.
PAGINATED_TEMPLATES = {
    "index": DEFAULT_PAGINATION,
}
PAGINATION_PATTERNS = (
    (1, "{url}", "{save_as}"),
    (2, "{base_name}/page/{number}/", "{base_name}/page/{number}/index.html"),
)

THEME = plumage.get_path()

STATIC_PATHS = [
    "uploads",
    "documents",
    "extra",
]

EXTRA_PATH_METADATA = {
    "extra/_headers": {"path": "_headers"},
    "extra/_redirects": {"path": "_redirects"},
    "extra/ads.txt": {"path": "ads.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/robots.txt": {"path": "robots.txt"},
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
    "pelican.plugins.image_process",
    "pelican.plugins.seo",
    "pelican.plugins.similar_posts",
    "pelican.plugins.neighbors",
    "pelican.plugins.sitemap",
    "pelican.plugins.tipue_search",
    "pelican.plugins.webassets",
]


# ----- Plugin-specific settings

# deadlinks
DEADLINK_VALIDATION = True

# pelican.plugins.seo
SEO_REPORT = False
SEO_ENHANCER = True

# pelican.plugins.similar_posts
SIMILAR_POSTS_MAX_COUNT = 3

# pelican.plugins.image_process
IMAGE_PROCESS = {
    "article-photo": {
        "type": "responsive-image",
        "sizes": """
            (min-width: 1200px) 800px,
            (min-width: 992px) 650px,
            (min-width: 768px) 718px,
            100vw
        """,
        "srcset": [
            # All keeps 4:3 aspect ratios.
            ("600w", ["scale_in 600 450 True"]),
            ("800w", ["scale_in 800 600 True"]),
            ("1600w", ["scale_in 1600 1200 True"]),
        ],
        # Default Plumage's central content column is 540px wide, so default to
        # 600w variant.
        "default": "600w",
    },
    "example-pict": {
        "type": "picture",
        "sources": [
            {
                "name": "default",
                "media": "(min-width: 640px)",
                "srcset": [
                    ("640w", ["scale_in 640 480 True"]),
                    ("1024w", ["scale_in 1024 683 True"]),
                    ("1600w", ["scale_in 1600 1200 True"]),
                ],
                "sizes": "100vw",
            },
            {
                "name": "source-1",
                "srcset": [
                    ("1x", ["crop 100 100 200 200"]),
                    ("2x", ["crop 100 100 300 300"]),
                ],
            },
        ],
        "default": ("default", "640w"),
    },
}


# ----- Theme-specific settings

SITE_THUMBNAIL = "/uploads/2018/profile-photo-square-thumbnail.jpg"
SITE_THUMBNAIL_TEXT = "Might come with a beard"

SITESUBTITLE = " 🦬🪒🐇🕳 - Yak shaving the rabbit holes"

MENUITEMS = (
    ("Home", "/"),
    ("Themes", "/themes/"),
    ("About", "/about/"),
)

CODE_STYLE = "monokai"

TIPUE_SEARCH = True

LEFT_SIDEBAR = (
    """
    <script async
    """
    """src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?"""
    """client=ca-pub-0142056597033291" crossorigin="anonymous"></script>"""
    """
    <!-- Responsive Ad -->
    <ins class="adsbygoogle"
         style="display:block"
         data-ad-client="ca-pub-0142056597033291"
         data-ad-slot="9726265119"
         data-ad-format="auto"
         data-full-width-responsive="true"></ins>
    <script>
         (adsbygoogle = window.adsbygoogle || []).push({});
    </script>
    """
)

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
under a <a class="text-body-secondary" rel="license"
href="https://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International license</a>."""

DISQUS_SITENAME = "kevin-deldycke-blog"

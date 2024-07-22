import re
from pathlib import Path

import plumage

SITEURL = "http://localhost:8000"
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True

AUTHOR = SITENAME = "Kevin Deldycke"

PATH = "content"

TIMEZONE = "Europe/Paris"
DEFAULT_LANG = "en"

TYPOGRIFY = True

# https://github.com/ashwinvis/myst-reader#docutils-renderer
MYST_DOCUTILS_SETTINGS = {
    # Allow to use the ```mermaid (...)``` directive:
    # "myst_fence_as_directive": {"python", "shell-session", "mermaid"},
    "myst_number_code_blocks": ["python", "shell-session"],
    # 7 is the max value:
    # https://github.com/executablebooks/MyST-Parser/blob/5f03f5c/myst_parser/config/main.py#L291
    "myst_heading_anchors": 7,
    # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
    "myst_enable_extensions": {
        "attrs_block",
        "attrs_inline",
        "deflist",
        "replacements",
        "smartquotes",
        "strikethrough",
        "tasklist",
    },
}

# Allow MyST syntax in content metadata:
# https://github.com/ashwinvis/myst-reader/tree/main#specifying-file-metadata
FORMATTED_FIELDS = [
    "title",
]

# Do not publish articles set in the future
WITH_FUTURE_DATES = False

# Force Pelican to use the file name as the slug, instead of derivating it from
# the title.
SLUGIFY_SOURCE = "basename"

ARTICLE_URL = "{date:%Y}/{slug}"
ARTICLE_SAVE_AS = ARTICLE_URL + ".html"
# Select all yearly folders as containing articles and their attachments.
ARTICLE_PATHS = [
    d.name
    for d in (Path(__file__).parent / PATH).iterdir()
    if d.is_dir() and re.fullmatch("[0-9]{4}", d.name)
]

PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"
PAGE_PATHS = ["pages"]

TEMPLATE_PAGES = {
    "templates/themes.html": "themes.html",
}

DIRECT_TEMPLATES = ["index", "tags", "categories", "authors", "archives"]

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = TAG_URL + "index.html"

CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = CATEGORY_URL + "index.html"

# Only activates yearly archives. Keep monthly and daily archives deactivated.
YEAR_ARCHIVE_SAVE_AS = "{date:%Y}/index.html"

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
    (2, "{base_name}/page/{number}", "{base_name}/page/{number}.html"),
)

THEME = plumage.get_path()

STATIC_PATHS = ["extra"]

EXTRA_PATH_METADATA = {
    "extra/_headers": {"path": "_headers"},
    "extra/_redirects": {"path": "_redirects"},
    "extra/ads.txt": {"path": "ads.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/profile-photo-square-thumbnail.jpg": {
        "path": "profile-photo-square-thumbnail.jpg"
    },
}


# ----- Plugin-specific settings

# pelican.plugins.deadlinks
DEADLINK_VALIDATION = True

# pelican.plugins.seo
SEO_REPORT = False
SEO_ENHANCER = True

# pelican.plugins.similar_posts
SIMILAR_POSTS_MAX_COUNT = 3


# ----- Theme-specific settings

SITE_THUMBNAIL = "/profile-photo-square-thumbnail.jpg"
SITE_THUMBNAIL_TEXT = "Might come with a beard"

SITESUBTITLE = " — 🦬🪒🐇🕳 yak-shaving the rabbit holes"

MENUITEMS = (
    ("Home", "/"),
    ("Themes", "/themes"),
    ("About", "/about"),
)

CODE_STYLE = "monokai"

STORK_SEARCH = True

LEFT_SIDEBAR = (
    """
    <script async
    """
    """src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?"""
    """client=ca-pub-2767080117475424" crossorigin="anonymous"></script>"""
    """
    <!-- Responsive ad -->
    <ins class="adsbygoogle"
         style="display:block"
         data-ad-client="ca-pub-2767080117475424"
         data-ad-slot="1778316959"
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
)

LINKS_WIDGET_NAME = "Professional profiles"
LINKS = (("LinkedIn", "https://linkedin.com/in/kevindeldycke/en"),)

COPYRIGHT = """Unless contrary mentioned, the content of this site is published
under a <a class="text-body-secondary" rel="license"
href="https://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International license</a>."""

DISQUS_SITENAME = "kevin-deldycke-blog"

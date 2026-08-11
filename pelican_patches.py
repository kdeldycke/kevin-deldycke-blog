"""Local workarounds for Pelican behaviours this blog needs changed.

Fixes are collected here rather than pushed straight to Plumage or Pelican, so each one
gets exercised against the whole corpus before being proposed to whichever project it
belongs to. See ``CLAUDE.md`` for the policy.

The hooks install themselves on import: ``pelicanconf.py`` imports this module, and
Pelican reads its settings before it reads any content. Registering through the
``PLUGINS`` setting instead would be a trap, as ``load_plugins()`` only auto-discovers
the ``pelican.plugins`` namespace while ``PLUGINS`` is left unset. Naming one plugin
there would silently drop the six this blog relies on.
"""

from __future__ import annotations

import os
import posixpath
import re
from html import escape

from pelican import signals
from pelican.contents import Article, Content

# The src of an <img>, captured in three pieces so the value can be swapped without
# disturbing the other attributes. Deliberately narrow: <img> is the only tag whose
# relative paths this blog writes by hand.
IMG_SRC = re.compile(r"""(<img\b[^>]*?\bsrc=["'])([^"']+)(["'])""", re.IGNORECASE)

# Anything carrying a scheme: http:, https:, data:, mailto: and friends.
HAS_SCHEME = re.compile(r"^[a-z][a-z0-9+.\-]*:", re.IGNORECASE)


def _is_source_relative(url: str) -> bool:
    """Is this a path a non-Pelican Markdown renderer would resolve on its own?"""
    # Already usable as-is: absolute, protocol-relative, site-rooted or a bare fragment.
    if not url or url.startswith(("/", "#")) or HAS_SCHEME.match(url):
        return False
    # An intra-site marker Pelican has yet to expand. `{attach}`, `{static}` and
    # `{filename}` are still literal at this point, because the substitution runs later
    # in `Content._update_content()`. Both delimiter styles are accepted by the default
    # INTRASITE_LINK_REGEX, so both are skipped. What they expand to is already absolute.
    return "{" not in url and "|" not in url


def absolutize_relative_images(instance: Content) -> None:
    """Turn image paths written relative to the Markdown file into absolute site URLs.

    Pelican only recognises its own ``{attach}`` marker, which nothing else understands:
    GitHub and editor previews render it as a broken image. A plain relative path renders
    everywhere, but Pelican has no reason to touch it, so it survives untouched into the
    tag and category feeds. There a reader resolves it against the feed's own URL rather
    than the article's, and 404s, because Pelican emits no ``xml:base``.

    Rewriting on ``content_object_init`` catches the content before the writer and the
    feed generator read it, so page and feed agree.

    Only articles qualify. For them the folder holding the Markdown file and the folder
    the page is written to are the same (``content/2005/`` becomes ``output/2005/``),
    which is exactly what lets a source-relative path survive into the output. Pages
    break that symmetry by being written to the site root, so they are left alone.
    """
    if not isinstance(instance, Article):
        return

    content = getattr(instance, "_content", None)
    source = getattr(instance, "relative_source_path", None)
    if not content or not source:
        return

    # Where the article's attachments land, relative to the site root. Taken from the
    # source path rather than from `save_as`, because that is what STATIC_PATHS mirrors
    # when it copies the files over.
    base = posixpath.dirname(source.replace(os.sep, "/"))
    siteurl = instance.settings.get("SITEURL", "").rstrip("/")

    def rewrite(match: re.Match[str]) -> str:
        prefix, url, suffix = match.groups()
        if not _is_source_relative(url):
            return match.group(0)
        target = posixpath.normpath(posixpath.join(base, url)) if base else url
        return f"{prefix}{siteurl}/{target}{suffix}"

    instance._content = IMG_SRC.sub(rewrite, content)


# A canonical link already present in the document, whoever wrote it.
CANONICAL_LINK = re.compile(r"""<link\b[^>]*\brel=["']canonical["']""", re.IGNORECASE)


def _served_url(save_as: str) -> str:
    """Map a path under ``output/`` to the URL Cloudflare Pages serves it at.

    Pages resolves a directory to its ``index.html`` and strips ``.html`` from every
    other name, redirecting the suffixed spelling to the bare one. The output path
    therefore already carries the answer, and no generator state is needed to read it.
    """
    if save_as == "index.html":
        return ""
    if save_as.endswith("/index.html"):
        # Keep the trailing slash: TAG_URL and CATEGORY_URL both end in one.
        return save_as[: -len("index.html")]
    if save_as.endswith(".html"):
        return save_as[: -len(".html")]
    return save_as


def canonicalize_listings(path: str, context: dict) -> None:
    """Give every generated listing page a ``<link rel="canonical">``.

    The ``seo`` plugin writes one for articles and pages only: its ``run_html_enhancer``
    returns early unless the render context holds an ``article`` or a ``page``, which no
    listing template supplies. That leaves the homepage, the per-tag, per-category and
    per-year indexes, the ``archives``/``categories``/``tags`` summaries and the index
    pagination with nothing naming the host they belong to.

    It matters because the site answers on two hostnames. ``kevin.deldycke.com`` is a
    CNAME to ``kevin-deldycke-blog.pages.dev``, and Cloudflare keeps that subdomain
    publicly reachable for the life of the project: it cannot be deleted, and hiding it
    would take a Pages Function on every request, since neither ``_redirects`` nor
    ``_headers`` can match on host. Naming the canonical host in the markup costs
    nothing at request time and settles the question wherever the document is served
    from. See ``docs/infrastructure.md``.

    Paginated pages point at themselves rather than at the first page, which is what
    Google asks for: canonicalizing a sequence onto its head drops the rest of it.

    The tag is spliced in as text instead of through BeautifulSoup, the way the plugin
    does it. Re-serializing would round-trip 800-odd documents full of hand-written
    HTML through a parser for the sake of one line, and the corpus is exactly the kind
    that notices. Skipping documents that already carry a canonical keeps this safe to
    run over output the plugin has already touched.
    """
    if not path.endswith(".html"):
        return
    # Already handled by the seo plugin, whose receiver shares this signal.
    if context.get("article") or context.get("page"):
        return

    output_path = context.get("OUTPUT_PATH")
    siteurl = context.get("SITEURL", "").rstrip("/")
    if not output_path:
        return

    with open(path, encoding="utf-8") as document:
        markup = document.read()
    if CANONICAL_LINK.search(markup) or "</head>" not in markup:
        return

    url = _served_url(os.path.relpath(path, output_path).replace(os.sep, "/"))
    tag = f'<link href="{escape(f"{siteurl}/{url}", quote=True)}" rel="canonical">'
    with open(path, "w", encoding="utf-8") as document:
        document.write(markup.replace("</head>", f"{tag}</head>", 1))


def register() -> None:
    """Connect every patch above to the signal it hooks into.

    Safe to call more than once: Blinker keys receivers by identity, and this module is
    cached in ``sys.modules``, so a second call reconnects the same function objects.
    """
    signals.content_object_init.connect(absolutize_relative_images)
    signals.content_written.connect(canonicalize_listings)


register()

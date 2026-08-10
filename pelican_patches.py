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


def register() -> None:
    """Connect every patch above to the signal it hooks into.

    Safe to call more than once: Blinker keys receivers by identity, and this module is
    cached in ``sys.modules``, so a second call reconnects the same function objects.
    """
    signals.content_object_init.connect(absolutize_relative_images)


register()

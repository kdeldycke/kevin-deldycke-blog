# Copyright Kevin Deldycke <kevin@deldycke.com> and contributors.
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

"""Regression tests for the local Pelican workarounds.

Every case below goes through a real ``Article``, not a stand-in, because the patch hangs
off ``content_object_init``, which Pelican fires from ``Content.__init__``. Building the
object therefore exercises the registration and the rewrite together: if the import side
effect in ``pelicanconf.py`` ever stops installing the hook, these fail.
"""

from __future__ import annotations

import pytest
from pelican.contents import Article, Page
from pelican.settings import DEFAULT_CONFIG

import pelican_patches

SITEURL = "https://kevin.deldycke.com"

# Somewhere under the content root. Only the folder matters: it is what the rewritten
# URL is built from, and what STATIC_PATHS mirrors when copying attachments over.
CONTENT_ROOT = "/content"
ARTICLE_SOURCE = f"{CONTENT_ROOT}/2005/post.md"


def build(content, cls=Article, source_path=ARTICLE_SOURCE, siteurl=SITEURL):
    """Instantiate a piece of Pelican content, which fires the signal the patch is on."""
    settings = DEFAULT_CONFIG.copy()
    settings["SITEURL"] = siteurl
    settings["PATH"] = CONTENT_ROOT
    return cls(
        content=content,
        metadata={"title": "Title"},
        settings=settings,
        source_path=source_path,
    )


@pytest.mark.parametrize(
    ("src", "expected"),
    (
        # Paths relative to the Markdown file are the whole point: they render in GitHub
        # and editor previews, and get anchored to the article's folder here.
        ("photo.jpg", f"{SITEURL}/2005/photo.jpg"),
        ("nested/photo.jpg", f"{SITEURL}/2005/nested/photo.jpg"),
        ("./photo.jpg", f"{SITEURL}/2005/photo.jpg"),
        ("../2004/photo.jpg", f"{SITEURL}/2004/photo.jpg"),
        # Anything already resolvable on its own is left exactly as it was.
        (f"{SITEURL}/2005/photo.jpg", f"{SITEURL}/2005/photo.jpg"),
        ("http://example.com/photo.jpg", "http://example.com/photo.jpg"),
        ("//example.com/photo.jpg", "//example.com/photo.jpg"),
        ("/rooted.jpg", "/rooted.jpg"),
        ("data:image/gif;base64,R0lGOD", "data:image/gif;base64,R0lGOD"),
        ("#fragment", "#fragment"),
        # Pelican's own markers are still literal at this point: they are expanded later,
        # by Content._update_content(), and come out absolute on their own. Both
        # delimiter styles of the default INTRASITE_LINK_REGEX have to survive.
        ("{attach}photo.jpg", "{attach}photo.jpg"),
        ("|attach|photo.jpg", "|attach|photo.jpg"),
        ("{static}/img/photo.jpg", "{static}/img/photo.jpg"),
        ("{filename}/2004/other.md", "{filename}/2004/other.md"),
    ),
)
def test_image_src_rewriting(src, expected):
    assert build(f'<img src="{src}"/>')._content == f'<img src="{expected}"/>'


@pytest.mark.parametrize(
    ("markup", "expected"),
    (
        # Quoting style, attribute order and every other attribute have to come out
        # untouched: only the value of src is the patch's business.
        (
            "<img src='photo.jpg'/>",
            f"<img src='{SITEURL}/2005/photo.jpg'/>",
        ),
        (
            '<img class="a" src="photo.jpg" alt="Some caption"/>',
            f'<img class="a" src="{SITEURL}/2005/photo.jpg" alt="Some caption"/>',
        ),
        (
            '<IMG SRC="photo.jpg"/>',
            f'<IMG SRC="{SITEURL}/2005/photo.jpg"/>',
        ),
        # An alt text mentioning a filename must not be mistaken for a src.
        (
            '<img src="photo.jpg" alt="named photo.jpg"/>',
            f'<img src="{SITEURL}/2005/photo.jpg" alt="named photo.jpg"/>',
        ),
        # Several images in one document, mixing forms.
        (
            '<img src="a.png"/><p>x</p><img src="{attach}b.png"/><img src="c.png"/>',
            (
                f'<img src="{SITEURL}/2005/a.png"/><p>x</p>'
                f'<img src="{{attach}}b.png"/><img src="{SITEURL}/2005/c.png"/>'
            ),
        ),
    ),
)
def test_surrounding_markup_is_preserved(markup, expected):
    assert build(markup)._content == expected


def test_rewrite_is_idempotent():
    """A second pass must be a no-op, since the first one produced absolute URLs."""
    article = build('<img src="photo.jpg"/>')
    once = article._content
    pelican_patches.absolutize_relative_images(article)
    assert article._content == once


def test_pages_are_left_alone():
    """Pages are written to the site root, so a source-relative path cannot resolve.

    Their attachments would also land in output/pages/, which is why the folder is kept
    out of STATIC_PATHS. Rewriting them would invent a URL nothing serves.
    """
    page = build(
        '<img src="photo.jpg"/>', cls=Page, source_path=f"{CONTENT_ROOT}/pages/p.md"
    )
    assert page._content == '<img src="photo.jpg"/>'


def test_article_at_content_root():
    """No folder to anchor to: the URL is built straight off the site root."""
    article = build('<img src="photo.jpg"/>', source_path=f"{CONTENT_ROOT}/post.md")
    assert article._content == f'<img src="{SITEURL}/photo.jpg"/>'


def test_siteurl_trailing_slash_does_not_double_up():
    article = build('<img src="photo.jpg"/>', siteurl=f"{SITEURL}/")
    assert article._content == f'<img src="{SITEURL}/2005/photo.jpg"/>'


@pytest.mark.parametrize("content", ("", "<p>No image here.</p>"))
def test_content_without_images_is_untouched(content):
    assert build(content)._content == content


def test_article_without_source_path_is_safe():
    """Content built in memory has no source path to anchor against, and must not raise."""
    article = build('<img src="photo.jpg"/>', source_path=None)
    assert article._content == '<img src="photo.jpg"/>'


def test_hook_is_registered():
    """Guards the import side effect in pelicanconf.py, which is what installs the hook.

    Nothing else in the build references this function by name, so a lost import would
    otherwise only show up as silently broken images in the feeds.
    """
    from pelican import signals

    receivers = signals.content_object_init.receivers.values()
    resolved = {
        r() if callable(r) and not hasattr(r, "__name__") else r for r in receivers
    }
    assert pelican_patches.absolutize_relative_images in resolved


def test_myst_renderer_is_pinned():
    """Dropping {attach} from a post must not change how that post is parsed.

    pelican-myst-reader picks the Sphinx renderer only when it spots "{filename}",
    "{static}" or "{attach}" in the file, and falls back to docutils otherwise. Migrating
    an image away from the marker therefore used to demote whole articles, and docutils
    then rejects the "{tag}" and "{category}" markers and some of the Pygments lexers the
    corpus uses. Pinning the renderer is what decouples the two.
    """
    import pelicanconf

    assert pelicanconf.MYST_FORCE_SPHINX is True


def test_myst_settings_reach_both_renderers():
    """Every documented MyST option has to apply whichever renderer ends up running.

    The reader keeps one settings key per renderer and silently falls back to its own
    defaults for whichever is missing. Configuring only the docutils side while forcing
    Sphinx would drop the code-block line numbers, reset the heading anchor depth, and
    cut the extension list down to colon_fence and deflist.
    """
    import pelicanconf

    for key, value in pelicanconf.MYST_DOCUTILS_SETTINGS.items():
        assert pelicanconf.MYST_SPHINX_SETTINGS[key] == value, key

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

"""Guards content whose formatting is load-bearing for what the article says.

Most posts survive being reformatted. A few make their point *through* their markup, and
a well-meaning autofix pass flattens the joke without touching a word. This module pins
the markup those articles argue with.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest
from markdown_it import MarkdownIt

CONTENT = Path(__file__).parent.parent / "content"
FALSEHOODS = CONTENT / "2016/falsehoods-programmers-believe-about-falsehoods-lists.md"

FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
OL_START = re.compile(r"<ol(?:\s+start=\"(\d+)\")?>")


def render(path: Path) -> str:
    """Render a post's body the way the site's Markdown engine would.

    MyST is built on markdown-it, and both agree on the only thing asserted below: the
    ``start`` an ordered list carries. Rendering here rather than reading ``output/``
    keeps this hermetic and fast, and a full build confirms the same three values.
    """
    body = FRONTMATTER.sub("", path.read_text(encoding="utf-8"))
    return MarkdownIt("commonmark").render(body)


@pytest.mark.parametrize(
    ("index", "start", "first_item"),
    (
        # "Falsehoods": an ordinary list, opening at 1.
        (0, None, "Falsehoods are true."),
        # "Falsehood lists": opens at 9, so "All falsehoods can be listed" is numbered
        # past the end of the list above it.
        (1, "9", "All falsehoods can be listed."),
        # "List format": opens at 404, and the item claiming numbered lists have no gap
        # is itself preceded by a gap of 403.
        (2, "404", "Numbered lists have no gap."),
    ),
)
def test_falsehood_list_numbering(index, start, first_item):
    """Each list has to keep the number it opens on: that number is the argument.

    Only the first number in a Markdown ordered list reaches the output, as CommonMark
    renumbers the rest. So these three values are the entire joke, and flattening any of
    them to 1 silently removes a counter-example while leaving the prose intact.
    """
    html = render(FALSEHOODS)
    starts = OL_START.findall(html)
    assert len(starts) == 3, f"expected 3 ordered lists, found {len(starts)}"
    assert starts[index] == (start or "")

    items = re.findall(r"<li>(.*?)</li>", html.split("<ol")[index + 1], re.DOTALL)
    assert items[0].strip().startswith(first_item)


def test_falsehood_list_repeats_itself():
    """The falsehood about lists not repeating themselves is stated twice, on purpose."""
    body = FALSEHOODS.read_text(encoding="utf-8")
    assert body.count("Falsehood lists don't repeat themselves.") == 2


def test_falsehood_list_breaks_its_own_format():
    """The item claiming every entry shares one format is the only one set as code."""
    html = render(FALSEHOODS)
    assert "<code>The same format is followed by each item.</code>" in html

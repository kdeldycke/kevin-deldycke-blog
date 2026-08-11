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
    # markdown-it-py ships no type information, so `render()` is typed as returning Any
    # and mypy rejects handing that straight back from a function promising `str`.
    rendered: str = MarkdownIt("commonmark").render(body)
    return rendered


def visible_numbering(html: str) -> list[list[int]]:
    """The numbers a reader actually sees down the left margin, list by list.

    Counts the way a browser does: an ``<ol start>`` sets the counter, each ``<li>``
    increments it, and an explicit ``<li value>`` resets it mid-list.
    """
    lists: list[list[int]] = []
    counter = 1
    # Closing tags are tracked so the bullet lists further down the article, which carry
    # <li> of their own, are not counted as part of the last numbered one.
    inside = False
    for tag in re.findall(r"<ol[^>]*>|</ol>|<li[^>]*>", html):
        if tag.startswith("<ol"):
            start = re.search(r'start="(\d+)"', tag)
            counter = int(start.group(1)) if start else 1
            lists.append([])
            inside = True
        elif tag == "</ol>":
            inside = False
        elif inside:
            value = re.search(r'value="(\d+)"', tag)
            if value:
                counter = int(value.group(1))
            lists[-1].append(counter)
            counter += 1
    return lists


@pytest.mark.parametrize(
    ("index", "numbering", "first_item"),
    (
        # "Falsehoods": an ordinary list, opening at 1.
        (0, [1, 2, 3, 4, 5, 6, 7, 8], "Falsehoods are true."),
        # "Falsehood lists": opens at 9, so "All falsehoods can be listed" is numbered
        # past the end of the list above it.
        (1, [9, 10, 11, 12, 13, 14, 15, 16], "All falsehoods can be listed."),
        # "List format": the section that argues with its own numbering. It opens at 404
        # so the item denying gaps is preceded by one, and item 999 lands between 404 and
        # 406 so the item denying that lists are sorted sits in an unsorted list.
        (2, [404, 999, 406, 407, 408, 409], "Numbered lists have no gap."),
    ),
)
def test_falsehood_list_numbering(index, numbering, first_item):
    """The numbers are the argument, so they have to reach the page intact.

    Markdown only honours the first number of an ordered list and renumbers the rest,
    which is why the out-of-order item is written as HTML with an explicit ``value``.
    Flattening any of this leaves the prose reading the same while quietly removing a
    counter-example.
    """
    lists = visible_numbering(render(FALSEHOODS))
    assert len(lists) == 3, f"expected 3 ordered lists, found {len(lists)}"
    assert lists[index] == numbering

    items = re.findall(r"<li[^>]*>(.*?)</li>", render(FALSEHOODS), re.DOTALL)
    assert items[sum(len(x) for x in lists[:index])].strip().startswith(first_item)


def test_falsehood_list_is_not_sorted():
    """The heart of the gag: the item claiming lists are sorted must break the order."""
    numbers = visible_numbering(render(FALSEHOODS))[2]
    assert numbers != sorted(numbers), "the 'List format' list came out sorted"


def test_falsehood_list_repeats_itself():
    """The falsehood about lists not repeating themselves is stated twice, on purpose."""
    body = FALSEHOODS.read_text(encoding="utf-8")
    assert body.count("Falsehood lists don't repeat themselves.") == 2


def test_falsehood_list_breaks_its_own_format():
    """The item claiming every entry shares one format is the only one set as code."""
    html = render(FALSEHOODS)
    assert "<code>The same format is followed by each item.</code>" in html

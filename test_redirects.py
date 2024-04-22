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

"""Test and validate Cloudflare Pages redirect rules.

See: https://developers.cloudflare.com/pages/configuration/redirects/
"""

from __future__ import annotations

from collections import Counter
from enum import Enum
from typing import Iterator

import pytest
import requests

ROOT_URL = "https://kevin.deldycke.com"
REDIRECT_FILE = "content/extra/_redirects"


def get_redirect_rules() -> Iterator[tuple[str, str, int]]:
    """Parse and validate redirect rules."""
    for line in open(REDIRECT_FILE).read().splitlines():
        assert len(line) <= 1000, f"Redirect rule longer than 1000: {line}"

        line = line.strip()
        if not line or line.startswith("#"):
            continue

        # Validate rule.
        params = line.split()
        assert len(params) in (
            2,
            3,
        ), f"Redirect rule must have 2 or 3 parameters: {line}"

        # Validate source.
        source = params[0]
        assert source.startswith("/"), f"Source must be a file path: {source}"

        # Validate destination.
        destination = params[1]
        assert destination.startswith("/") or destination.startswith(
            "https://"
        ), f"Destination must be a file path or an absolute URL: {destination}"

        # Validate code. Defaults to 302 if not provided.
        if len(params) == 3:
            assert params[
                2
            ].isdigit(), f"HTTP status code must be an integer: {params[2]}"
            code = int(params[2])
        else:
            code = 302

        yield source, destination, code


class CAT(Enum):
    """Category of a path item."""

    STATIC = "static"
    WILDCARD = "wildcard"
    SPLAT = "splat"
    PLACEHOLDER = "placeholder"
    FRAGMENT = "fragment"
    QUERY = "query"
    EXTERNAL = "external"


def split_path(path: str) -> list[tuple[str, CAT]]:
    """Split a path into its components and classify them."""
    items = []

    if path.startswith("https://"):
        return [(path, CAT.EXTERNAL)]

    for item in path.split("/"):
        if item == "*":
            cat = CAT.WILDCARD
        elif item == ":splat":
            cat = CAT.SPLAT
        elif item.startswith(":"):
            assert item[1:].isidentifier()
            cat = CAT.PLACEHOLDER
        elif item.startswith("#"):
            cat = CAT.FRAGMENT
        elif "?" in item:
            cat = CAT.QUERY
            # Check that query parameters do not contain placeholders.
            _, query = item.split("?", 1)
            for param in query.split("&"):
                if "=" in param:
                    key, value = param.split("=", 1)
                    assert key.isalnum()
                    if value.startswith(":"):
                        assert item[1:].isidentifier()
                        cat = CAT.PLACEHOLDER
                        break
        else:
            assert "*" not in item, f"Invalid wildcard in path element: {item}"
            cat = CAT.STATIC

        items.append((item, cat))

    return items


def generate_test_cases():
    """Parse redirect rules and generate test cases."""
    total_static = 0
    total_dynamic = 0

    for source, destination, code in get_redirect_rules():
        # Validate the categories of the source path.
        src_items = split_path(source)
        src_categories = Counter(category for _, category in src_items)

        assert {
            CAT.STATIC,
            CAT.WILDCARD,
            CAT.PLACEHOLDER,
        }.issuperset(
            src_categories
        ), f"Source path only allows wildcards, placeholders and static items: {src_items}"

        assert (
            src_categories[CAT.WILDCARD] <= 1
        ), f"Source path is not allowed to have multiple wildcards: {src_items}"

        # Validate the categories of the destination path.
        dest_items = split_path(destination)
        dest_categories = Counter(category for _, category in dest_items)

        assert CAT.WILDCARD not in set(
            dest_categories
        ), f"Destination path is not allowed to have wildcards: {dest_items}"

        static_categories = {CAT.STATIC, CAT.EXTERNAL}
        if static_categories.issuperset(
            src_categories
        ) and static_categories.issuperset(dest_categories):
            total_static += 1
        else:
            total_dynamic += 1
            # TODO: generate dynamic cases for dynamic redirects.
            continue

        src = f"{ROOT_URL}{source}"

        if CAT.EXTERNAL in dest_categories:
            dest = destination
        else:
            dest = f"{ROOT_URL}{destination}"

        yield pytest.param(
            src,
            dest,
            code,
            id=f"{src} -> {dest} | rule: {source} {destination} {code}",
        )

    assert total_static <= 2000, "Too many static redirects."
    assert total_dynamic <= 100, "Too many dynamic redirects."


@pytest.mark.parametrize(("source", "destination", "code"), generate_test_cases())
def test_permanent_redirects(source, destination, code):
    # Check destination is normalized to have no trailing slash.
    # assert not source.endswith("/")
    # assert destination == "/" or not destination.endswith("/")

    with requests.get(source) as response:
        # The final destination is an existing page that we expect.
        assert response.ok
        assert response.url == destination

        # Check there's only one redirect, meaning that our redirect rules are optimized.
        assert len(response.history) == 1
        assert response.history[0].status_code == code
        if code == 301:
            assert response.history[0].is_redirect
            assert response.history[0].is_permanent_redirect

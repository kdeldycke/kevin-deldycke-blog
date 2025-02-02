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

import random
import re
from collections import Counter
from enum import Enum
from string import ascii_letters, digits
from typing import Iterator

import pytest
import requests

DOMAIN = "deldycke.com"
SUB_DOMAIN = f"kevin.{DOMAIN}"
ROOT_URL = f"https://{SUB_DOMAIN}"
REDIRECT_FILE = "content/extra/_redirects"


validate_placeholder = re.compile(r":[A-Za-z]\w*").match
""" Regular expression to validate placeholder IDs in paths."""


def get_redirect_rules() -> Iterator[tuple[str, str, int]]:
    """Parse and validate redirect rules."""
    for line in open(REDIRECT_FILE).read().splitlines():
        assert len(line) <= 1000, f"Redirect rule longer than 1000: {line}"

        line = line.strip()
        if not line or line.startswith("#"):
            continue

        # Validate rule.
        params = line.split()
        assert (
            2 <= len(params) <= 3
        ), f"Redirect rule must have 2 or 3 parameters: {line}"

        # Validate source.
        source = params[0]
        assert source.startswith("/"), f"Source must be a file path: {source}"

        # Validate destination.
        destination = params[1]
        assert destination.startswith("/") or destination.startswith(
            "https://"  # XXX Only support HTTPs URLs.
        ), f"Destination must be a file path or an absolute HTTPs URL: {destination}"

        # Validate code. Defaults to 302 if not provided.
        if len(params) == 3:
            assert params[2].isdigit(), f"HTTP code must be an integer: {params[2]}"
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
    QUERY = "query"
    FRAGMENT = "fragment"
    EXTERNAL = "external"


def split_path(url: str) -> list[tuple[str, CAT]]:
    """Split an URL into its components and classify them.

    Accept both absolute and relative URLs.
    """
    items = []

    # Extract the path from the URL.
    path: str
    # URL is absolute, separate the host from the path.
    if url.startswith("https://"):
        elements = url.split("/", 3)
        url_root = "/".join(elements[:3])
        items.append((url_root, CAT.EXTERNAL))
        if len(elements) > 3:
            path = elements[3]

    # URL is relative, so it is only a path.
    else:
        # Remove the leading slash, like we do for absolute URLs above.
        assert url.startswith("/"), "Relative path are supposed to start with a slash."
        path = url[1:]

    # Split the path into its components.
    for item in path.split("/"):
        if item == "*":
            cat = CAT.WILDCARD
        elif item == ":splat":
            cat = CAT.SPLAT
        elif item.startswith(":"):
            assert validate_placeholder(item)
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
                        assert validate_placeholder(item)
                        cat = CAT.PLACEHOLDER
                        break
        else:
            assert "*" not in item, f"Invalid wildcard in path element: {item}"
            cat = CAT.STATIC

        items.append((item, cat))

    # A placeholder can only appear once in a path.
    placeholders = Counter(ph for ph, cat in items if cat == CAT.PLACEHOLDER)
    assert all(
        count == 1 for count in placeholders.values()
    ), f"Duplicate placeholders in path: {set(ph for ph, count in placeholders.items() if count > 1)}"

    return items


def create_case(src: str, dest: str, rule_src: str, rule_dest: str, rule_code: int):
    return pytest.param(
        src,
        dest,
        rule_code,
        id=f"{src} -> {dest} | rule: {rule_src} {rule_dest} {rule_code}",
    )


def random_str() -> str:
    return "".join(random.choices(ascii_letters + digits, k=10))


def url_fixtures(*path_items_list: list[tuple[str, CAT]]) -> Iterator[str]:
    """Generate real, fully qualified URLs that can be used as fixtures.

    Takes a list of URLs, already split into their components and categorized.

    Replace placeholders with random strings, and ensure the same placeholders are consistent
    within the set of URLs.
    """
    # Keep track of placeholders' random values to ensure consistency.
    placeholders: dict[str, str] = {}

    for path_items in path_items_list:
        items = []
        for item, cat in path_items:
            if cat == CAT.PLACEHOLDER:
                new_item = placeholders.setdefault(item, random_str())
            elif cat == CAT.WILDCARD:
                # Produce a path with a random number of components.
                new_item = "/".join(random_str() for _ in range(random.randint(2, 5)))
                placeholders[":splat"] = new_item
            elif cat == CAT.SPLAT:
                assert ":splat" in placeholders
                new_item = placeholders[":splat"]
            else:
                new_item = item

            items.append(new_item)

        # Prepend the root URL if the path is not an absolute URL.
        if not path_items or path_items[0][1] != CAT.EXTERNAL:
            items.insert(0, ROOT_URL)

        yield "/".join(items)


def cases_from_rules():
    """Parse redirect rules and generate test cases."""
    total_static = 0
    total_dynamic = 0

    for source, destination, code in get_redirect_rules():
        # Categorize each item in the source and destination paths.
        src_items = split_path(source)
        dest_items = split_path(destination)
        src_categories = Counter(category for _, category in src_items)
        dest_categories = Counter(category for _, category in dest_items)

        # Validate the categories of the source path.
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
        assert (
            CAT.WILDCARD not in dest_categories
        ), f"Destination path is not allowed to have wildcards: {dest_items}"

        # Splat without a wildcard is not allowed.
        assert not (
            CAT.SPLAT in dest_categories and CAT.WILDCARD not in src_categories
        ), f"Source path is missing wildcard for splat placeholder to work: {src_items} -> {dest_items}"

        # The rule is considered static only if both the source and destination paths
        # are composed of static items.
        if {CAT.STATIC, CAT.EXTERNAL}.issuperset((*src_categories, *dest_categories)):
            total_static += 1

            src, dest = url_fixtures(src_items, dest_items)

            # Generate a unique test case.
            yield create_case(src, dest, source, destination, code)

        # The rule is dynamic, so we need to generate multiple test cases.
        else:
            total_dynamic += 1
            # TODO: Generate 2 random test cases per placeholder.

            src, dest = url_fixtures(src_items, dest_items)

            # Random test cases with placeholders will lead to a 404, but not the
            # redirects leading to external URLs.
            if CAT.EXTERNAL not in dest_categories:
                code = 404

            yield create_case(src, dest, source, destination, code)

    assert total_static <= 2000, "Too many static redirects."
    assert total_dynamic <= 100, "Too many dynamic redirects."


@pytest.mark.parametrize(
    ("source", "destination", "code"),
    cases_from_rules(),
)
def test_redirects(source, destination, code):
    with requests.get(source) as response:
        # Check that the source URL is reachable, unless it's a 404 test case
        # (because of a randonly generated placeholder).
        if code != 404:
            assert response.ok

        # Python's requests library always normalize URLs to have no trailing slash.
        if destination == ROOT_URL:
            destination = f"{ROOT_URL}/"
        assert response.url == destination

        # Check there's only one redirect, meaning that our redirect rules are
        # optimized.
        assert len(response.history) == 1

        # Every test case is a redirect.
        if code != 404:
            assert response.history[0].status_code == code

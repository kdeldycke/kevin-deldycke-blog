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

"""Test and validate Cloudflare Pages header rules against the live site.

Every rule in ``content/extra/_headers`` exists because a browser or a reader guesses the
wrong thing without it. A feed served as ``text/xml`` is offered as a download instead of
being subscribed to, and the Stork search index only loads if it arrives as WebAssembly.
None of that shows up in a build: the file is copied verbatim into ``output/`` and only
means anything once Cloudflare is serving it, so the only test worth writing fetches the
real URL.

See: https://developers.cloudflare.com/pages/configuration/headers/
"""

from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path

import pytest
import requests

ROOT_URL = "https://kevin.deldycke.com"
HEADERS_FILE = Path(__file__).parent.parent / "content/extra/_headers"

SAMPLES: dict[str, str] = {
    # The site-wide rule is sampled at the root, but it applies to every response.
    "/*": "/",
    # The feed rules come in pairs: a wildcard for every per-category and per-tag feed,
    # and a literal for the site-wide one at the root. Both are tested, because the
    # wildcard rule does not cover the root and the two have already been edited apart
    # from each other once.
    "/*/feed.rss": "/category/english/feed.rss",
    "/feed.rss": "/feed.rss",
    "/*/feed.atom": "/category/english/feed.atom",
    "/feed.atom": "/feed.atom",
    "/search-index.st": "/search-index.st",
    # Attachment types the site serves that no server guesses correctly. All paths
    # point at real articles, so a sample that stops resolving is itself a finding.
    "/*.numbers": "/2020/cpu-compatibility-asrock-e3c246d2i-noctua-nh-l9i.numbers",
    "/*.reg": "/2010/putty-template.reg",
    "/*.patch": "/2008/mailman-219-7-charset-handling.patch",
    "/*.xcf": "/2008/corner-banner.xcf",
}
"""A concrete URL for each rule in ``_headers``.

Kept as data rather than generated, because a wildcard cannot be turned into a URL that
exists: ``/*.numbers`` matches an infinity of paths and the site serves exactly one. The
mapping is asserted complete below, so adding a rule without a sample fails the suite
rather than silently going untested.
"""


def get_header_rules() -> Iterator[tuple[str, dict[str, str]]]:
    """Parse ``_headers`` into its rules, validating the format on the way through.

    Cloudflare's format is positional: an unindented line opens a rule and names the paths
    it applies to, and the indented lines under it are that rule's headers. A header line
    that loses its indentation silently becomes a path pattern matching nothing, which is
    the failure mode this parser is meant to make loud.
    """
    pattern: str | None = None
    headers: dict[str, str] = {}

    for number, raw in enumerate(
        HEADERS_FILE.read_text(encoding="utf-8").splitlines(), 1
    ):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue

        # Unindented: a new rule starts, so the previous one is complete.
        if raw == line:
            if pattern is not None:
                assert headers, f"Rule {pattern!r} declares no header"
                yield pattern, headers
            assert line.startswith("/"), (
                f"Line {number}: a rule must start with a slash, got {line!r}. An "
                "indented header line that lost its indentation looks exactly like this."
            )
            pattern, headers = line, {}
            continue

        # Indented: a header belonging to the rule above.
        assert pattern is not None, f"Line {number}: header {line!r} precedes any rule"
        assert ":" in line, f"Line {number}: header must be `name: value`, got {line!r}"
        name, _, value = line.partition(":")
        headers[name.strip().lower()] = value.strip()

    if pattern is not None:
        assert headers, f"Rule {pattern!r} declares no header"
        yield pattern, headers


RULES = dict(get_header_rules())


def media_type(value: str) -> str:
    """Strip parameters off a Content-Type so ``; charset=utf-8`` cannot fail a match.

    Cloudflare currently returns these values bare, but a charset appearing later is a
    presentation change rather than a regression, and this test should not be the thing
    that objects to it.
    """
    return value.partition(";")[0].strip().lower()


def test_every_rule_has_a_sample():
    """A rule with no sample URL is a rule nothing checks.

    This is the guard that keeps the suite honest as ``_headers`` grows: the cost of a new
    rule is one line in ``SAMPLES``, and forgetting it fails here rather than quietly
    reducing coverage.
    """
    assert set(RULES) == set(SAMPLES), (
        f"Rules without a sample URL: {sorted(set(RULES) - set(SAMPLES))}. "
        f"Samples for rules that no longer exist: {sorted(set(SAMPLES) - set(RULES))}."
    )


@pytest.mark.parametrize(
    ("pattern", "path", "headers"),
    (
        pytest.param(
            pattern, SAMPLES[pattern], headers, id=f"{pattern} -> {SAMPLES[pattern]}"
        )
        for pattern, headers in RULES.items()
        if pattern in SAMPLES
    ),
)
def test_header_is_served(pattern, path, headers):
    """The rule's headers must actually reach the client, on a URL the rule matches."""
    with requests.get(f"{ROOT_URL}{path}") as response:
        assert response.ok, f"{path} is not reachable, so the rule cannot be tested"

        # A redirect would mean the sample is stale and some other URL answered, which
        # would test the wrong rule while looking like a pass.
        assert not response.history, (
            f"{path} redirected to {response.url}: the sample no longer matches {pattern}"
        )

        for name, expected in headers.items():
            actual = response.headers.get(name)
            assert actual is not None, f"{path} is served without a {name} header"
            if name == "content-type":
                assert media_type(actual) == media_type(expected)
            else:
                assert actual == expected

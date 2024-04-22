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

from __future__ import annotations

import pytest
import requests

ROOT_URL = "https://kevin.deldycke.com"


@pytest.mark.parametrize(
    ("source", "destination"),
    # Test cases mirrors content/extra/_redirects
    (
        ("/extra", "/"),
        ("/page", "/"),
        ("/theme", "/"),
        ("/category", "/categories"),
        ("/tag", "/tags"),
        ("/page/1", "/"),
        ("/documents", "/"),
    ),
)
def test_permanent_redirects(source, destination):
    # Check that source and destination are normalized to have no trailing slash.
    assert not source.endswith("/")
    assert destination == "/" or not destination.endswith("/")

    with requests.get(f"{ROOT_URL}{source}") as response:
        # The final destination is an existing page that we expect.
        assert response.ok
        assert response.url == f"{ROOT_URL}{destination}"

        # Check there's only one redirect, meaning that our redirect rules are permanent, tight and optimized.
        assert len(response.history) == 1
        assert response.history[0].status_code == 301
        assert response.history[0].is_permanent_redirect

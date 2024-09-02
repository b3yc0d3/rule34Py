
import pytest

from rule34Py.html import TagMapPage


TAGMAP_LOCATION_COUNT = 285  # There are 285 districts on the map


@pytest.fixture(scope="module")
def tagmap_html(rule34):
    resp = rule34._get("https://rule34.xxx/static/tagmap.html")
    resp.raise_for_status()
    return resp.text


def test_TagMapPage_init(tagmap_html):
    """The TagMapPage class can be instantiated on its own."""
    tagmap = TagMapPage(tagmap_html)
    assert len(tagmap.map_points.keys()) == TAGMAP_LOCATION_COUNT


def test_TagMapPage_map_points_from_html(tagmap_html):
    """TagMapPage.map_points_from_html() parses tagmap data from html."""
    map_points = TagMapPage.map_points_from_html(tagmap_html)
    from pprint import pprint
    pprint(map_points)
    assert isinstance(map_points, dict)
    assert len(map_points.keys()) == TAGMAP_LOCATION_COUNT

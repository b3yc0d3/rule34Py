
import pytest

from rule34Py.html import TagMapPage, ICamePage
from rule34Py.icame import ICame
from rule34Py.api_urls import API_URLS


ICAME_CHART_LEN = 100  # It's the top-100 chart.
TAGMAP_LOCATION_COUNT = 285  # There are 285 districts on the map


@pytest.fixture(scope="module")
def tagmap_html(rule34):
    resp = rule34._get("https://rule34.xxx/static/tagmap.html")
    resp.raise_for_status()
    return resp.text


@pytest.fixture(scope="module")
def icame_html(rule34):
    resp = rule34._get(API_URLS.ICAME.value)
    resp.raise_for_status()
    return resp.text


def test_ICamePage_init(icame_html):
    """The ICamePage class can be instantiated from html."""
    icame_page = ICamePage(icame_html)
    assert len(icame_page.top_chart) == ICAME_CHART_LEN


def test_ICamePage_top_chart_from_html(icame_html):
    """ICamePage.top_chart_from_html() parses the icame chart from html."""
    top_chart = ICamePage.top_chart_from_html(icame_html)
    assert isinstance(top_chart, list)
    assert len(top_chart) == ICAME_CHART_LEN
    assert isinstance(top_chart[0], ICame)


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

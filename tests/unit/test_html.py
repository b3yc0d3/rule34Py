
import pytest

from rule34Py.api_urls import API_URLS
from rule34Py.html import *
from rule34Py.icame import ICame
from rule34Py.toptag import TopTag


ICAME_CHART_LEN = 100  # It's the top-100 chart.
HISTORY_POOL_ID = 720  # Arbitrary old pool w/ lots of history, that hasn't been updated recently.
TAGMAP_LOCATION_COUNT = 285  # There are 285 districts on the map
TOP_TAGS_CHART_LEN = 100  # It's a top-100 chart.


# FIXTURES #
############

@pytest.fixture(scope="module")
def icame_html(rule34):
    resp = rule34._get(API_URLS.ICAME.value)
    resp.raise_for_status()
    return resp.text


@pytest.fixture(scope="module")
def pool_history_html(rule34):
    resp = rule34._get(f"https://rule34.xxx/index.php?page=pool&s=history&id={HISTORY_POOL_ID}")
    resp.raise_for_status()
    return resp.text


@pytest.fixture(scope="module")
def tagmap_html(rule34):
    resp = rule34._get("https://rule34.xxx/static/tagmap.html")
    resp.raise_for_status()
    return resp.text


@pytest.fixture(scope="module")
def toptags_html(rule34):
    resp = rule34._get(API_URLS.TOPMAP.value)
    resp.raise_for_status()
    return resp.text


# TESTS #
#########

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


def test__PoolHistoryPage__events_from_html(rule34):
    """The events_from_html() method parses history page html for its events."""
    def get_pool_history_html(pool_id, pagination_index=0):
        resp = rule34._get(f"https://rule34.xxx/index.php?page=pool&s=history&id={HISTORY_POOL_ID}&pid={pagination_index}")
        print(resp.headers)
        print(resp.text)
        resp.raise_for_status()
        return resp.text

    # Pool #720 is arbitrarily chosen because it has a long history, but is not
    # recently updated.
    events = PoolHistoryPage.events_from_html(get_pool_history_html(720, 0))
    assert isinstance(events, list)
    assert len(events) == 50  # 50 is the max events per page
    assert isinstance(events[0], PoolHistoryEvent)
    # This event list should overlap with the last 49 entries in the prior.
    events2 = PoolHistoryPage.events_from_html(get_pool_history_html(720, 1))
    dates1 = set([e.date for e in events][1:])
    dates2 = set([e.date for e in events2][:49])
    assert dates1 == dates2


def test__PoolPage__pool_from_html(rule34):
    """The pool_from_html() method generates a Pool object from a page."""
    def get_pool_html(pool_id):
        resp = rule34._get(f"https://rule34.xxx/index.php?page=pool&s=show&id={pool_id}")
        print(resp.headers)
        print(resp.text)
        resp.raise_for_status()
        return resp.text
    # pool 233 chosen because it is: unlikely to change, static in size, and has
    # a differing name and description.
    pool = PoolPage.pool_from_html(get_pool_html(233))
    assert isinstance(pool, Pool)
    assert pool.pool_id == 233
    assert pool.name == "[Sparrow] Learning Her Lesson"
    assert pool.description == "Sparrows work - depicting the milf Farah teaching a class about \"sexual arts\"\
(http://g.e-hentai.org/g/267651/39325aedbe/)"
    assert len(pool.posts) == 6
    assert pool.posts[0] == 1506559
    assert pool.posts[5] == 1506564

    # Pool 920 is empty (0 posts) and has no description.
    pool = PoolPage.pool_from_html(get_pool_html(920))
    assert pool.pool_id == 920
    assert pool.name == "[Adam Wan] November's Bribe"
    assert pool.description == ""
    assert len(pool.posts) == 0


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


def test_TopTagsPage(toptags_html):
    """The TopTagsPage class can be instantiated from html."""
    page = TopTagsPage(toptags_html)
    assert len(page.top_tags) == TOP_TAGS_CHART_LEN


def test_TopTagsPage_top_tags_from_html(toptags_html):
    """TopTagsPage.top_tags_from_html() parses the icame chart from html."""
    top_tags = TopTagsPage.top_tags_from_html(toptags_html)
    assert isinstance(top_tags, list)
    assert len(top_tags) == TOP_TAGS_CHART_LEN
    assert isinstance(top_tags[0], TopTag)

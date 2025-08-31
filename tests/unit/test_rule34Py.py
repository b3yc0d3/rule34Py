"""These tests confirm the functionality of the rule34Py.rule34 class.
"""
import importlib.metadata
import re

import pytest

from rule34Py import Post, Pool
from rule34Py.rule34 import SEARCH_RESULT_MAX
from rule34Py.post_comment import PostComment
from rule34Py.icame import ICame
from rule34Py.toptag import TopTag
from rule34Py.autocomplete_tag import AutocompleteTag

TEST_POOL_ID = 28  # An arbitrary, very-old pool, that is probably stable.
R34_VERSION = importlib.metadata.version("rule34Py")

def test_rule34Py_autocomplete(rule34):
    """The autocomplete method should return a list of tag suggestions."""
    suggestions = rule34.autocomplete("neko")
    
    assert isinstance(suggestions, list)
    
    if suggestions:
        first = suggestions[0]
        assert isinstance(first, AutocompleteTag)
        assert hasattr(first, 'label')
        assert hasattr(first, 'value')
        assert hasattr(first, 'type')
        assert isinstance(first.label, str)
        assert isinstance(first.value, str)
        assert isinstance(first.type, str | None)

    empty_suggestions = rule34.autocomplete("")
    assert isinstance(empty_suggestions, list)

def test_rule34Py_get_comments(rule34):
    """The get_comments() method should fetch a list of comments from a post.
    """
    # TEST_POST_ID is the oldest post from search `neko rating:safe` with multiple comments.
    TEST_POST_ID = 3471384
    comments = rule34.get_comments(TEST_POST_ID)
    assert isinstance(comments, list)
    assert len(comments) > 1
    assert isinstance(comments[0], PostComment)


def test_rule34Py_get_pool(rule34):
    """The client can get a post pool object."""
    TEST_NUM_POSTS = 14  # there are 14 posts in this pool
    FIRST_POST_ID = 952001

    pool = rule34.get_pool(pool_id=TEST_POOL_ID)
    assert isinstance(pool, Pool)
    assert pool.pool_id == TEST_POOL_ID
    assert len(pool.posts) == TEST_NUM_POSTS
    assert pool.posts[0] == FIRST_POST_ID


def test_rule34Py_get_post(rule34):
    """The client get_post() method fetches a single Post.
    """
    TEST_POST_ID = 3471384
    post = rule34.get_post(TEST_POST_ID)
    assert isinstance(post, Post)
    assert post.id == TEST_POST_ID


def test_rule34Py_icame(rule34):
    """The client icame() method fetches the icame leaderboard as a list.
    """
    icame = rule34.icame()
    assert isinstance(icame, list)
    assert len(icame) == 100  # the list length is 100 by default
    assert isinstance(icame[0], ICame)


def test_rule34Py_iter_search(rule34):
    """The iter_search() method will iterate over post search results.
    """
    # The method returns an iterator.
    from collections.abc import Iterator
    iter = rule34.iter_search()
    assert isinstance(iter, Iterator)
    # You can loop over that iterator and get Post objects.
    for post in rule34.iter_search():
        assert isinstance(post, Post)
        break
    # By default, it will iterate until the end of the search results.
    # The "1938" tag is a pretty safe bet to have very few results.
    results = list(rule34.iter_search(tags=["1938"]))
    assert len(results) > 0
    # But you can also specify a max_number of results.
    # The "female" tag is basically guaranteed to have a bunch of results.
    results = list(rule34.iter_search(["female"], max_results=17))
    assert len(results) == 17
    # If the max_results are greater than a single page, the iterator will
    # transparently move to the next page.
    results = list(rule34.iter_search(["female"], max_results=1002))
    assert len(results) == 1002


def test__rule34Py__user_agent(rule34):
    """The client has a user agent attribute that can be user-defined."""
    # Default should be something like "Mozilla/... rule34Py/1.2.3"
    print(rule34.user_agent)
    assert "Mozilla" in rule34.user_agent
    assert "rule34Py" in rule34.user_agent
    assert R34_VERSION in rule34.user_agent
    
    # The user_agent can be changed.
    rule34.user_agent = "foobar"
    resp = rule34._get("http://example.com")
    print(resp.request.headers)
    assert resp.request.headers["User-Agent"] == "foobar"


def test_rule34Py_get_post(rule34):
    """The client get_post() method fetches a single Post by post ID."""
    post = rule34.get_post(8973658)
    assert isinstance(post, Post)
    assert post.id == 8973658
    # Post #2 does not exist.
    assert rule34.get_post(2) is None


def test_rule34Py_random_post(rule34):
    """The client random_post() method fetches a random Post object.
    """
    post = rule34.random_post()
    print(post)
    assert isinstance(post, Post)


def test_rule34Py_random_post_id(rule34):
    """The client random_post_id() method fetches a random Post ID number."""
    id = rule34.random_post_id()
    print(f"id={id}")
    assert isinstance(id, int)
    assert id > 0


def test__rule34Py__request_limiter(rule34):
    """The client has a configurable adapter for the base site that limits requests to some reasonable rate."""
    from time import time

    client = rule34

    def time_requests(num_tests) -> float:
        print("time_requests() =")
        times = []
        ts1 = None
        ts2 = None
        ts0 = time()  # timing session start
        for i in range(0, num_tests + 1):
            client.get_pool(TEST_POOL_ID)
            ts2 = time()
            if ts1 is not None:
                tdelta = ts2 - ts1
                times.append(tdelta)
                print(f"time delta[{i}] = {tdelta} s")
            ts1 = ts2
        session_time = time() - ts0
        print(f"session_time = {session_time}")
        return session_time

    # The default should be once per second
    session_time = time_requests(5)
    assert session_time >= 5 / 1

    # Users can disable the rate limiter.
    # This test can theoretically fail if the normal request time is
    # every long.
    client.set_base_site_rate_limit(False)
    session_time = time_requests(5)
    assert session_time <= 5


def test_rule34Py_search(rule34):
    """The client can search for posts by tags, with pagination."""
    # search by single tag
    results1 = rule34.search(["neko"])
    ids1 = [post.id for post in results1]
    print(f"ids1={ids1[:10]}...")
    assert isinstance(results1, list)  # return type is list
    
    assert len(results1) == SEARCH_RESULT_MAX
    assert isinstance(results1[0], Post)  # return list contains Post objects

    # get a second page of results
    results2 = rule34.search(["neko"], page_id=2)
    ids2 = [post.id for post in results2]
    print(f"ids2={ids2[:10]}...")
    assert set(ids1).isdisjoint(set(ids2))  # page1 and 2 have no posts in common
    
    # test that the limit param is honored
    results3 = rule34.search(["neko"], limit=20)
    ids3 = [post.id for post in results3]
    print(f"ids3={ids3[:10]}...")
    assert len(results3) == 20
    print(set(ids3) - set(ids1))
    assert set(ids3).issubset(set(ids1))

    # Invalid arguments - limit
    with pytest.raises(ValueError) as e:
        rule34.search([], limit=-10)
    with pytest.raises(ValueError):
        rule34.search([], limit=SEARCH_RESULT_MAX + 1)

def test_rule34Py_search_exclude_ai(rule34):
    """The client can search for posts by tags, with excluding ai generated content."""
    # search by single tag
    results1 = rule34.search(["neko"], exclude_ai=True)
    ids1 = [post.id for post in results1]
    print(f"ids1={ids1[:10]}...")
    assert isinstance(results1, list)  # return type is list
    
    assert len(results1) == SEARCH_RESULT_MAX
    assert isinstance(results1[0], Post)  # return list contains Post objects


def test_rule34Py_tag_map(rule34):
    """The client tag_map() method should return a map of tags.
    """
    tag_map = rule34.tag_map()
    assert isinstance(tag_map, dict)
    assert len(tag_map) > 0
    for key, value in tag_map.items():
        assert isinstance(key, str)
        assert isinstance(value, str)
        break  # just check the first tag_map point


def test_rule34Py_tagmap(rule34):
    """The old tagmap() method should throw a deprecation warning, but return the top_tags() method."""
    with pytest.warns(DeprecationWarning) as warnings:
        top_tags = rule34.tagmap()
    # The warning message should direct the user to the new methods.
    assert re.match(r".*top_tags.*", str(warnings[0].message))
    assert re.match(r".*tag_map.*", str(warnings[0].message))
    assert isinstance(top_tags, list)
    assert isinstance(top_tags[0], TopTag)


def test_rule34Py_top_tags(rule34):
    """The top_tags() method returns a list of the top 100 global tags.
    """
    top_tags = rule34.top_tags()
    assert isinstance(top_tags, list)
    assert len(top_tags) == 100
    assert isinstance(top_tags[0], TopTag)

"""These tests confirm the functionality of the rule34Py.rule34 class.
"""
import pytest

from rule34Py import Post
from rule34Py.rule34 import SEARCH_RESULT_MAX
from rule34Py.post_comment import PostComment
from rule34Py.icame import ICame
from rule34Py.toptag import TopTag


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
    TEST_POOL_ID = 28  # An arbitrary, very-old pool, that is probably stable.
    TEST_NUM_POSTS = 14  # there are 14 posts in this pool
    FIRST_POST_ID = 952001
    post_ids = rule34.get_pool(pool_id=TEST_POOL_ID, fast=True)
    # when Fast=True, return type is list[int]
    assert isinstance(post_ids, list)
    assert len(post_ids) == TEST_NUM_POSTS
    assert isinstance(post_ids[0], int)
    assert post_ids[0] == FIRST_POST_ID

    # Test non-fast operation
    posts = rule34.get_pool(pool_id=TEST_POOL_ID, fast=False)
    # when Fast=False, return type is list[Post]
    assert isinstance(posts, list)
    assert len(posts) == TEST_NUM_POSTS
    assert isinstance(posts[0], Post)
    assert posts[0].id == FIRST_POST_ID


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
    # TODO: test the `limit` parameter once, it is working.


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


def test_rule34Py_random_post(rule34):
    """The client random_post() method fetches a random Post object.
    """
    post = rule34.random_post()
    assert isinstance(post, Post)
    # You can specify tags to limit the random search
    post = rule34.random_post(tags=["neko"])
    assert "neko" in post.tags


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


def test_rule34Py_tagmap(rule34):
    """The client tagmap() method should return a map of tags.
    """
    tagmap = rule34.tagmap()
    assert isinstance(tagmap, dict)
    assert len(tagmap) > 0
    for key, value in tagmap.items():
        assert isinstance(key, str)
        assert isinstance(value, str)
        break  # just check the first tagmap point

def test_rule34Py_top_tags(rule34):
    """The top_tags() method returns a list of the top 100 global tags.
    """
    top_tags = rule34.top_tags()
    assert isinstance(top_tags, list)
    assert len(top_tags) == 100
    assert isinstance(top_tags[0], TopTag)

def test_rule34Py_version(rule34):
    """The version() property should just raise a deprecation warning.
    
    Remove this test when the method is removed.
    """
    with pytest.raises(DeprecationWarning) as ex:
        rule34.version
    assert ex.match(r".*Use `rule34Py.version` instead.*")

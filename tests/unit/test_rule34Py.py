"""These tests confirm the functionality of the rule34Py.rule34 class.
"""
import pytest

from rule34Py import Post


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


def test_rule34Py_search(rule34):
    """The client can search for posts by tags, with pagination."""
    # search by single tag
    results1 = rule34.search(["neko"])
    ids1 = [post.id for post in results1]
    print(f"ids1={ids1[:10]}...")
    assert isinstance(results1, list)  # return type is list
    
    assert len(results1) == 1000  # should return the maximum number of posts (1000)
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


def test_rule34Py_search_invalid_args(rule34):
    """The search() method should raise Value exceptions when input values are invalid."""
    # invalid page_ids
    for invalid_page_id in ["foobar"]:
        print(f"Testing invalid_page_id={invalid_page_id}")
        with pytest.raises(Exception) as e:
            rule34.search(["neko"], page_id=invalid_page_id)
    # invalid limits
    for invalid_limit in [-100, 0, None, "foobar"]:
        print(f"Testing invalid_limit={invalid_limit}")
        with pytest.raises(Exception) as e:
            rule34.search(["neko"], limit=invalid_limit)
    # deleted is always invalid
    with pytest.raises(Exception) as e:
        rule34.search(["neko"], deleted=True)
    assert "not implemented" in str(e.value).lower()

"""These tests confirm that the functional advertisements in the project's README are correct and valid.
"""
import inspect

import rule34Py
from rule34Py.icame import ICame
from rule34Py.post import Post
from rule34Py.post_comment import PostComment


# used in the README.md
EXAMPLE_POST = 4153825
EXAMPLE_POOL = 28


def test_module_import():
    """The rule34Py module contains a class called 'rule34Py'."""
    members = inspect.getmembers(rule34Py, inspect.isclass)
    assert "rule34Py" in [m[0] for m in members]

def test_get_comments(rule34):
    """The client can fetch the comments of the example post."""
    comments = rule34.get_comments(EXAMPLE_POST)
    print(comments)
    assert len(comments) > 0  # should be a few here
    assert isinstance(comments[0], PostComment)  # should be PostComments

def test_get_post(rule34):
    """The client can fetch a post by its id."""
    post = rule34.get_post(EXAMPLE_POST)
    print(post)
    assert post.id == EXAMPLE_POST  # post ID should match
    assert isinstance(post, Post)  # should be a post

def test_icame(rule34):
    """The client can get the top 100 icame."""
    icames = rule34.icame()
    assert len(icames) > 0  # should have something in it
    for icame in icames:
        assert isinstance(icame, ICame)

def test_search(rule34):
    """The client can search for posts by tag."""
    results = rule34.search(["neko"], page_id=2, limit=50)
    assert len(results) == 50
    for post in results:
        assert isinstance(post, Post)

def test_get_pool(rule34):
    """The client can get the example pool by id."""
    pool = rule34.get_pool(EXAMPLE_POOL)
    assert isinstance(pool, rule34Py.Pool)
    assert pool.pool_id == 28
    assert len(pool.posts) > 0  # there should be posts here

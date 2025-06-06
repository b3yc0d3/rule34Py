"""This module provides classes representing the Rule34 website's Pool objects."""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class PoolHistoryEvent():
    """A Rule34 Pool history record.

    Parameters:
        date: The datetime of the historical event.
        updater_uname: The user name who initiated the event.
        post_ids: A list of the Pool posts that were affected by the event.
    """

    #: The datetime of the pool history event.
    date: datetime
    #: The user name who initiated the event.
    updater_uname: str

    #: A list of the Pool posts that were affected by the event.
    post_ids: list[int] = field(default_factory=list())


@dataclass
class Pool():
    """A collection of Rule34 Posts.

    Parameters:
        pool_id: The pool's unique numeric ID.
        name: The pool's title.
        description: A summary description of the pool's contents.
        posts: A list of Post ID numbers that are members of the pool.
    """

    #: The pool's unique numeric ID.
    pool_id: int
    #: The pool's title.
    name: str
    #: A summary description of the pool's contents.
    description: str

    #: A list of Post ID numbers that are members of the pool.
    posts: list[int] = field(default_factory = list)


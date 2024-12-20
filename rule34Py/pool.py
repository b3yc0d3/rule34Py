"""This module provides classes representing the Rule34 website's Pool objects."""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class PoolHistoryEvent():
    """A Rule34 Pool history record."""

    date: datetime
    updater_uname: str
    post_ids: list[int] = field(default_factory=list())


@dataclass
class Pool():
    """A collection of Rule34 Posts."""

    pool_id: int
    name: str
    description: str

    posts: list[int] = field(default_factory = list)


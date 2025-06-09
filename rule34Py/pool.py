# rule34Py - Python api wrapper for rule34.xxx
# 
# Copyright (C) 2022-2025 b3yc0d3 <b3yc0d3@gmail.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
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


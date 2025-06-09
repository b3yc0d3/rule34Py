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
"""A module providing classes representing Rule34 Post comments."""


class PostComment:
    """A post comment.
    
    Args:
        id: The comment's numeric ID on Rule34.
        owner_id: The numeric ID of the comment author.
        body: The comment's body text.
        post_id: The numeric ID of the attached post.
        creation: The timestamp string of when the post was made.
    """

    def __init__(self,
        id: int,
        owner_id: int,
        body: str,
        post_id: int,
        creation: str) -> "PostComment":
        """Create a new PostComment."""
        self._id = id
        self._owner_id = owner_id
        self._body = body
        self._post_id = post_id
        self._creation = creation

    @property
    def id(self) -> int:
        """The comment's unique numeric ID."""
        return self._id

    @property
    def author_id(self) -> int:
        """The comment author's unique user ID."""
        return self._owner_id

    @property
    def body(self) -> str:
        """The comment's body text."""
        return self._body

    @property
    def post_id(self) -> int:
        """The numeric ID of the attached post."""
        return self._post_id

    @property
    def creation(self) -> str:
        """Timestamp string of when the comment was created."""
        return self._creation

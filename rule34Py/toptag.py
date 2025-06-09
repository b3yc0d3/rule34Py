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
"""A module for interacting with the Rule34 TopTag map.

https://rule34.xxx/index.php?page=toptags
"""


class TopTag:
    """A TopTag entry.

    Parameters:
        rank: The popularity rank of the tag.
        tagname: The tag name.
        percentage: The percentage of global posts that use the tag.
    """

    def __init__(self, rank: int, tagname: str, percentage: int):
        """Create a new TopTag class."""
        self._rank = rank
        self._tagname = tagname
        self._percentage = percentage

    def __from_dict(json: dict) -> "TopTag":
        """Create a TopTag object from JSON data.

        Returns:
            A new TopTag object, populated with values from the ``json`` dictionary.
        """
        return TopTag(json["rank"], json["tagname"], json["percentage"] * 100)

    @property
    def rank(self) -> int:
        """The popularity rank of the tag."""
        return self._rank

    @property
    def tagname(self) -> str:
        """The tag name."""
        return self._tagname

    @property
    def percentage(self) -> int:
        """The percentage of global posts that use the tag."""
        return self._percentage

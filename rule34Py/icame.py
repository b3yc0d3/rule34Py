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
"""A module containing content related to the rule34.xxx iCame popularity contest.

https://rule34.xxx/index.php?page=icame
"""


class ICame:
    """An iCame contestant.
    
    Represents an entry on the Rule34.xxx iCame top 100 rankings.
    """

    def __init__(self, character_name: str, count: int) -> "ICame":
        """An iCame contestant.

        Args:
            character_name: The name of the character.
                May be an empty string, representing posts that have no tagged character.
            count: The 'iCame(TM) count'.
                A count of how often people came on the character.
        """
        self._character_name = character_name
        self._tag_url = "https://rule34.xxx/index.php?page=post&s=list&tags={0}".format(character_name.replace(" ", "_"))
        self._count = count

    @property
    def character_name(self) -> str:
        """The name of the character."""
        return self._character_name

    @property
    def tag_url(self) -> str:
        """The character tag page URL."""
        return self._tag_url

    @property
    def count(self) -> int:
        """A count of how often people came on the character."""
        return self._count

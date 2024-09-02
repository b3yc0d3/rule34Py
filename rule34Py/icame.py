""""""
"""
rule34Py - Python api wrapper for rule34.xxx

Copyright (C) 2022-2024 b3yc0d3 <b3yc0d3@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

class ICame:
    """
    ICame chart item
    """

    def __init__(self, character_name: str, count: int):
        """
        iCame chart item.

        :param character_name: Name of the character.
        :type character_name: str

        :param count: Count of how often people came on the character.
        :type count: int
        """

        self._character_name = character_name
        self._tag_url = "https://rule34.xxx/index.php?page=post&s=list&tags={0}".format(character_name.replace(" ", "_"))
        self._count = count

    @property
    def character_name(self) -> str:
        """
        Get name of character.

        :return: Name of character.
        :rtype: str
        """

        return self._character_name

    @property
    def tag_url(self) -> str:
        """
        Get url of tag.

        :return: Url of tag.
        :rtype: str
        """

        return self._tag_url

    @property
    def count(self) -> int:
        """
        Get count of how often people came on the character.

        :return: Cum count.
        :rtype: int
        """

        return self._count

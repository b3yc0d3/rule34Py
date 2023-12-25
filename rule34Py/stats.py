""""""
"""
rule34Py - Python api wrapper for rule34.xxx

Copyright (C) 2022-2023 b3yc0d3 <b3yc0d3@gmail.com>

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

class Stat:
    """
    Stat class

    Generic Stat class, mostly used to Top nth lists.
    """
    def __init__(self, place, amount, username):
        """
        Stat class.

        :param place: Positional index.
        :type place: int
        
        :param amount: Count of something.
        :type amount: int

        :param username: Name, either a "username" or a charters name.
        :type username: str
        """

        self.__place = place
        self.__amount = amount
        self.__username = username

    @property
    def place(self):
        """
        Get positional place of the stat.

        :return: Positional index.
        :rtype: int
        """
        return self.__place

    @property
    def amount(self):
        """
        Get amount/count of it.

        :return: Amount of something related to this stat.
        :rtype: int
        """
        return self.__amount

    @property
    def username(self):
        """
        Get username or name of character related to this stat.

        :return: Related username / name of a character to this stat.
        :rtype: str
        """
        return self.__username

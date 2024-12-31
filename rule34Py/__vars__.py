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

__version__tuple__ = ("2", "1", "0")
__author__ = ("b3yc0d3")
__email__ = ("b3yc0d3@gmail.com")

__version__ = ".".join(__version__tuple__) # xx.xx.xx


# Variables
__base_url__ = "https://rule34.xxx/"
__api_url__ = "https://api.rule34.xxx/"
__useragent__ = f"Mozilla/5.0 (compatible; rule34Py/{__version__})"

__headers__ = {
    "User-Agent": __useragent__
}

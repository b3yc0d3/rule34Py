# rule34Py - Python api wrapper for rule34.xxx
# 
# Copyright (C) 2022 Tal A. Baskin <talbaskin.business@gmail.com>
# Copyright (C) 2023-2025 b3yc0d3 <b3yc0d3@gmail.com>
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
"""A module containing URL templates for the rule34.xxx websites."""


from enum import Enum
from rule34Py.__vars__ import __base_url__, __api_url__


class API_URLS(str, Enum):
    """rule34.xxx API endpoint URLs.

    Internal class used to change easily urls, if they should ever change.
    """
    #: The JSON search endpoint.
    SEARCH = f"{__api_url__}index.php?page=dapi&s=post&q=index&limit={{LIMIT}}&tags={{TAGS}}&json=1"
    #: The XML Post comments endpoint.
    COMMENTS = f"{__api_url__}index.php?page=dapi&s=comment&q=index&post_id={{POST_ID}}"
    #: An HTML User favorites endpoint.
    USER_FAVORITES = f"{__api_url__}index.php?page=favorites&s=view&id={{USR_ID}}"
    #: The JSON Post endpoint.
    GET_POST = f"{__api_url__}index.php?page=dapi&s=post&q=index&id={{POST_ID}}&json=1"
    #: The HTML ICAME page URL.
    ICAME = f"{__base_url__}index.php?page=icame"
    #: The HTML Random post URL.
    RANDOM_POST = f"{__base_url__}index.php?page=post&s=random"
    #: An HTML User profile URL.
    USER_PAGE = f"{__api_url__}index.php?page=account&s=profile&id={{USER_ID}}"
    #: An HTML Pool URL.
    POOL = f"{__base_url__}index.php?page=pool&s=show&id={{POOL_ID}}"
    #: The HTML toptags URL.
    TOPMAP = f"{__base_url__}index.php?page=toptags"

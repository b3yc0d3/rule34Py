""""""
"""
rule34Py - Python api wrapper for rule34.xxx

Copyright (C) 2022 Tal A. Baskin <talbaskin.business@gmail.com>
Copyright (C) 2023-2024 b3yc0d3 <b3yc0d3@gmail.com>

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

from enum import Enum
from rule34Py.__vars__ import __base_url__, __api_url__

class API_URLS(str, Enum):
    """
    Api Urls

    Internal class used to change easily urls, if they should ever change.
    """

    SEARCH = f"{__api_url__}index.php?page=dapi&s=post&q=index&limit={{LIMIT}}&tags={{TAGS}}&json=1" # returns: JSON
    COMMENTS = f"{__api_url__}index.php?page=dapi&s=comment&q=index&post_id={{POST_ID}}" # returns: XML
    USER_FAVORITES = f"{__api_url__}index.php?page=favorites&s=view&id={{USR_ID}}" # returns: HTML
    GET_POST = f"{__api_url__}index.php?page=dapi&s=post&q=index&id={{POST_ID}}&json=1" # returns: JSON
    ICAME = f"{__base_url__}index.php?page=icame" # returns: HTML
    RANDOM_POST = f"{__base_url__}index.php?page=post&s=random" #  returns: HTML
    USER_PAGE = f"{__api_url__}index.php?page=account&s=profile&id={{USER_ID}}" # returns: HTML
    POOL = f"{__base_url__}index.php?page=pool&s=show&id={{POOL_ID}}" # returns: HTML
    TOPMAP = f"{__base_url__}index.php?page=toptags"

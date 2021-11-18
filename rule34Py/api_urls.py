from enum import Enum
from rule34Py.__vars__ import __base_url__

class API_URLS(str, Enum):
    SEARCH = f"{__base_url__}index.php?page=dapi&s=post&q=index&limit={{LIMIT}}&tags={{TAGS}}&json=1" # returns: JSON
    COMMENTS = f"{__base_url__}index.php?page=dapi&s=comment&q=index&post_id={{POST_ID}}" # returns: XML
    USER_FAVORITES = f"{__base_url__}index.php?page=favorites&s=view&id={{USR_ID}}" # returns: HTML
    GET_POST = f"{__base_url__}index.php?page=dapi&s=post&q=index&id={{POST_ID}}&json=1" # returns: JSON
    ICAME = f"{__base_url__}icameout.php" # returns: HTML
    RANDOM_POST = f"{__base_url__}index.php?page=post&s=random" #  returns: HTML
    USER_PAGE = f"{__base_url__}index.php?page=account&s=profile&id={{USER_ID}}" # returns: HTML
    POOL = f"{__base_url__}index.php?page=pool&s=show&id={{POOL_ID}}" # returns: HTML
    TOPMAP = f"{__base_url__}index.php?page=toptags"

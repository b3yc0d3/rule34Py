#!/usr/bin/python3
import requests
import random
import urllib.parse as urlparse
from bs4 import BeautifulSoup
from enum import Enum
from urllib.parse import parse_qs
# From this module
from rule34Py.api_urls import API_URLS, __base_url__
from rule34Py.__vars__ import __headers__, __version__
from rule34Py.post import Post
from rule34Py.post_comment import PostComment
from rule34Py.icame import ICame


class rule34Py(Exception):
    """rule34.xxx API wraper
    """

    def __init__(self):
        """rule34.xxx API wraper
        """
        self.__isInit__ = False

    def search(self, tags: list, page_id: int = None, limit: int = 100) -> list:
        """Search for posts

        Args:
            tags (list[str]): Search tags
            page_num (int, optional): Page ID
            limit (int, optional): Limit for Posts. Max 100.

        Returns:
            list: Posts result list

        Tags Cheatsheet: https://rule34.xxx/index.php?page=tags&s=list
        """

        # Check if "limit" is in between 1 and 100
        if limit > 100 or limit <= 0:
            raise Exception("invalid value for \"limit\"\n  valid valius: 1-100")
            return

        params = [
            ["TAGS", "+".join(tags)],
            ["LIMIT", str(limit)],
        ]
        # Add "page_id"
        if page_id != None:
            params.append(["PAGE_ID", str(page_id)])

        url = API_URLS.SEARCH.value
        if page_id != None:
            url += "&pid={{PAGE_ID}}"

        formatted_url = self._parseUrlParams(url, params)
        response = requests.get(formatted_url, headers=__headers__)

        res_status = response.status_code
        res_len = len(response.content)
        ret_posts = []

        if res_status != 200 or res_len <= 0:
            return ret_posts

        for post in response.json():
            pFileUrl = post["file_url"]
            pHash = post["hash"]
            pId = post["id"]
            pScore = post["score"]
            pSize = [post["width"], post["height"]]
            pOwner = post["owner"]
            pTags = post["tags"].split(" ")

            ret_posts.append(Post(pId, pHash, pScore, pSize, pFileUrl, pOwner, pTags))

        return ret_posts

    def get_comments(self, post_id: int) -> list:
        """Get comments of given Post

        Args:
            post_id (int): Post id

        Returns:
            list: List of PostComment
        """

        params = [
            ["POST_ID", str(post_id)]
        ]
        formatted_url = self._parseUrlParams(API_URLS.COMMENTS, params) # Replaceing placeholders
        response = requests.get(formatted_url, headers=__headers__)

        res_status = response.status_code
        res_len = len(response.content)
        ret_comments = []

        if res_status != 200 or res_len <= 0:
            return None

        bfs_raw = BeautifulSoup(response.content.decode("utf-8"), features="xml")
        res_xml = bfs_raw.comments.findAll('comment')

        # loop through all comments
        for comment in res_xml:
            attrs = dict(comment.attrs)
            ret_comments.append(PostComment(attrs["id"], attrs["creator_id"], attrs["body"], attrs["post_id"], attrs["created_at"]))

        return ret_comments

    # TODO: solve the hcaptcher on login page
    # def get_favorites(self, user_id: int, fast: bool = False):
    #     """Get favorites from users
    #
    #     Args:
    #         user_id (int): Id of user
    #         fast (bool): If set to true, only Ids of the posts are returned
    #
    #     Returns:
    #         list: List of Posts (List of ids if "fast" true)
    #     """
    #
    #     return
    #
    #     params = [
    #         ["USER_ID", str(user_id)],
    #     ]
    #
    #     formatted_url = self._parseUrlParams(API_URLS.USER_PAGE.value, params)
    #     response = requests.get(formatted_url, headers=__headers__) # Sending get request
    #
    #     res_status = response.status_code
    #     res_len = len(response.content)
    #     html_string = response.content.decode("utf-8")
    #     ret_favorites = []
    #
    #     if res_status != 200 or res_len <= 0:
    #         return ret_favorites
    #
    #     soup = BeautifulSoup(html_string, "html.parser")
    #     for span in soup.find_all('span', {'class' : 'thumb'}):
    #         print(span["id"][1:])

    def get_pool(self, pool_id: int, fast: bool = True) -> list:
        """Get Pool by Id
        Be aware that if "fast" is set to False, it takes extreme long.

        Args:
            pool_id (int): Id of pool
            fast (bool, optional): If true, returns only post ids

        Returns:
            list: List of Post Objects/id Strings
        """

        params = [
            ["POOL_ID", str(pool_id)]
        ]
        response = requests.get(self._parseUrlParams(API_URLS.POOL.value, params), headers=__headers__)

        res_status = response.status_code
        res_len = len(response.content)
        ret_posts = []

        if res_status != 200 or res_len <= 0:
            return ret_posts

        soup = BeautifulSoup(response.content.decode("utf-8"), features="html.parser")

        for div in soup.find_all("span", class_="thumb"):
            a = div.find("a")
            id = div["id"][1:]

            if fast == True:
                ret_posts.append(id)
            else:
                ret_posts.append(self.get_post(id))

        return ret_posts

    def get_post(self, post_id: int) -> Post:
        """Get Post by Id

        Args:
            id (int): Id of post

        Returns:
            post: Post Object (of None if post not found)
        """

        params = [
            ["POST_ID", str(post_id)]
        ]
        formatted_url = self._parseUrlParams(API_URLS.GET_POST.value, params)
        response = requests.get(formatted_url, headers=__headers__)

        res_status = response.status_code
        res_len = len(response.content)
        ret_posts = []

        if res_status != 200 or res_len <= 0:
            return None

        for post in response.json():
            pFileUrl = post["file_url"]
            pHash = post["hash"]
            pId = post["id"]
            pScore = post["score"]
            pSize = [post["width"], post["height"]]
            pOwner = post["owner"]
            pTags = post["tags"].split(" ")

            ret_posts.append(Post(pId, pHash, pScore, pSize, pFileUrl, pOwner, pTags))

        return ret_posts if len(ret_posts) > 1 else (ret_posts[0] if len(ret_posts) == 1 else ret_posts)

    def icame(self, limit: int = 100) -> list:
        """Gets a list of the top 100 "came-on characters"

        Args:
            limit (int): Limit of returned items (default 100)

        Returns:
            list: Returns list of ICame Objects
        """

        response = requests.get(API_URLS.ICAME.value, headers=__headers__)

        res_status = response.status_code
        res_len = len(response.content)
        ret_topchart = []

        if res_status != 200 or res_len <= 0:
            return ret_topchart

        bfs_raw = BeautifulSoup(response.content.decode("utf-8"), features="html.parser")
        rows = bfs_raw.find("table", border=1).find("tbody").find_all("tr")

        for row in rows:
            if row == None:
                continue

            character_name = row.select('td > a', href=True)[0].get_text(strip=True)
            count = row.select('td')[1].get_text(strip=True)

            ret_topchart.append(ICame(character_name, count))


        return ret_topchart

    def random_post(self, tags: list = None):
        """Get random Post
        Args:
            tags (list, optional): Tag list

        Returns:
            Post: Post Object
        """

        ## Fixed bug: https://github.com/b3yc0d3/rule34Py/issues/2#issuecomment-902728779

        if tags != None:
            search_raw = self.search(tags)
            randnum = random.randint(0, len(search_raw))

            while len(search_raw) <= 0:
                search_raw = self.search(tags)
            else:
                return search_raw[randnum]

        else:
            return self.get_post(self._random_post_id())

    def tagmap(self) -> list:
        """Get TagMap (Top 100 Tags searched)
        Returns:
            list: List of dicts
        """

        response = requests.get(API_URLS.TOPMAP.value, headers=__headers__)

        res_status = response.status_code
        res_len = len(response.content)
        ret_topchart = []

        if res_status != 200 or res_len <= 0:
            return []

        bfs_raw = BeautifulSoup(response.content.decode("utf-8"), features="html.parser")
        rows = bfs_raw.find("table", class_="server-assigns").find_all("tr")

        rows.pop(0)
        rows.pop(0)

        retData = []

        for row in rows:
            tags = row.find_all("td")

            rank = tags[0].string[1:]
            tagname = tags[1].string
            percentage = tags[2].string[:-1]

            retData.append({
                "rank": int(rank),
                "tagname": tagname,
                "percentage": float(percentage.strip())
            })

        return retData


    def _random_post_id(self) -> str:
        res = requests.get(API_URLS.RANDOM_POST.value, headers=__headers__)
        parsed = urlparse.urlparse(res.url)

        return parse_qs(parsed.query)['id'][0]

    def _parseUrlParams(self, url: str, params: list) -> str:
        # Usage: _parseUrlParams("domain.com/index.php?v={{VERSION}}", [["VERSION", "1.10"]])
        retURL = url

        for g in params:
            key = g[0]
            value = g[1]

            retURL = retURL.replace("{" + key + "}", value)

        return retURL

    @property
    def version(self) -> str:
        """Get version of module

        Returns:
            str: Version string (eg. xx.xx.xx)
        """
        return __version__

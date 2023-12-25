""""""
"""
rule34Py - Python api wrapper for rule34.xxx

Copyright (C) 2022 MiningXL <miningxl@gmail.com>
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
from rule34Py.stats import Stat
from rule34Py.toptag import TopTag

"""
TODO: fix typos
"""

class Stats:
    def __get_top(self, name):
        """
        Get Top Taggers

        :param name: Name of a top 10 list.
                    Values may be:
                        - Top 10 taggers
                        - Top 10 commenter
                        - Top 10 forum posters
                        - Top 10 image posters
                        - Top 10 note editors
                        - Top 10 favorites
        :type name: str

        :return: List of stats.
        :rtype: list[Stat]
        """
        retList = []
        response = requests.get(API_URLS.STATS.value, headers=__headers__)

        res_status = response.status_code
        res_len = len(response.content)
        ret_topchart = []

        if res_status != 200 or res_len <= 0:
            return []

        bfs_raw = BeautifulSoup(response.content.decode("utf-8"), features="html.parser")
        tables = bfs_raw.select(".toptencont > table")

        for table in tables:
            title = table.select("thead > tr")[0].get_text(strip=True)

            if title == name:
                trs = table.find("tbody").find_all("tr")

                for tr in trs:
                    tds = tr.find_all("td")
                    # 1 = Place
                    # 2 = Count
                    # 3 = Username
                    retList.append(Stat(tds[0].get_text(strip=True), tds[1].get_text(strip=True), tds[2].get_text(strip=True)))
                    #print(f"{tds[0].get_text(strip=True)} - {tds[1].get_text(strip=True)} - {tds[2].get_text(strip=True)}")
        return retList

    def top_taggers(self):
        """
        Get the top 10 Taggers of the Day.

        :return: List of todays top 10 taggers.
        :rtype: list[Stat]
        """
        return self.__get_top("Top 10 taggers")

    def top_commenters(self):
        """
        Get the top 10 Commentators of the Day.

        :return: List of todays top 10 commentators.
        :rtype: list[Stat]
        """
        return self.__get_top("Top 10 commenters")

    def top_forum_posters(self):
        """
        Get the top 10 Forum Posters of the Day.

        :return: List of todays top 10 (forum) posters.
        :rtype: list[Stat]
        """
        return self.__get_top("Top 10 forum posters")

    def top_image_posters(self):
        """
        Get the top 10 Image Posters of the Day.

        :return: List of todays top 10 image posters.
        :rtype: list[Stat]
        """
        return self.__get_top("Top 10 image posters")

    def top_note_editors(self):
        """
        Get the top 10 Note Editors of the Day.

        :return: List of todays top 10 note editors.
        :rtype: list[Stat]
        """
        return self.__get_top("Top 10 note editors")

    def top_favorites(self):
        """
        Get the top 10 Favorites of the Day.

        :return: List of todays top 10 favorites.
        :rtype: list[Stat]
        """
        return self.__get_top("Top 10 favoriters")

# Main Class
class rule34Py(Exception):
    """
    rule34.xxx API wrapper
    """

    def __init__(self):
        """
        rule34.xxx API wrapper
        """
        self.__isInit__ = False
        self._stats = Stats()

    def search(self,
        tags: list,
        page_id: int = None,
        limit: int = 1000,
        deleted: bool = False,
        ignore_max_limit: bool = False) -> list:
        """
        Search for posts.

        :param tags: List of tags.
        :type tags: list[str]

        :param page_id: Page number/id.
        :type page_id: int

        :param limit: Limit for posts returned per page (max. 1000).
        :type limit: int

        :param ignore_max_limit: If limit of 1000 should be ignored.
        :type ignore_max_limit: bool

        :return: List of Post objects for matching posts.
        :rtype: list[Post]

        For more information, see:

            - `rule34.xxx API Documentation <https://rule34.xxx/index.php?page=help&topic=dapi>`_
            - `Tags cheat sheet <https://rule34.xxx/index.php?page=tags&s=list>`_
        """

        # Check if "limit" is in between 1 and 1000
        if not ignore_max_limit and limit > 1000 or limit <= 0:
            raise Exception("invalid value for \"limit\"\n  value must be between 1 and 1000\n  see for more info:\n  https://github.com/b3yc0d3/rule34Py/blob/master/DOC/usage.md#search")
            return

        params = [
            ["TAGS", "+".join(tags)],
            ["LIMIT", str(limit)],
        ]
        url = API_URLS.SEARCH.value
        # Add "page_id"
        if page_id != None:
            url += f"&pid={{PAGE_ID}}"
            params.append(["PAGE_ID", str(page_id)])

        
        if deleted:
            raise Exception("To include deleted images is not Implemented yet!")
            #url += "&deleted=show"

        formatted_url = self._parseUrlParams(url, params)
        response = requests.get(formatted_url, headers=__headers__)
        
        res_status = response.status_code
        res_len = len(response.content)
        ret_posts = []

        # checking if status code is not 200
        # (it's useless currently, becouse rule34.xxx returns always 200 OK regardless of an error)
        # and checking if content lenths is 0 or smaller
        # (curetly the only way to check for a error response)
        if res_status != 200 or res_len <= 0:
            return ret_posts

        for post in response.json():
            ret_posts.append(Post.from_json(post))

        return ret_posts

    def get_comments(self, post_id: int) -> list:
        """
        Retrieve comments of post by its id.

        :param post_id: Posts id.
        :type post_id: int

        :return: List of comments.
        :rtype: list[PostComment]
        """

        params = [
            ["POST_ID", str(post_id)]
        ]
        formatted_url = self._parseUrlParams(API_URLS.COMMENTS, params) # Replacing placeholders
        response = requests.get(formatted_url, headers=__headers__)

        res_status = response.status_code
        res_len = len(response.content)
        ret_comments = []

        if res_status != 200 or res_len <= 0:
            return ret_comments

        bfs_raw = BeautifulSoup(response.content.decode("utf-8"), features="xml")
        res_xml = bfs_raw.comments.findAll('comment')

        # loop through all comments
        for comment in res_xml:
            attrs = dict(comment.attrs)
            ret_comments.append(PostComment(attrs["id"], attrs["creator_id"], attrs["body"], attrs["post_id"], attrs["created_at"]))

        return ret_comments


    def get_pool(self, pool_id: int, fast: bool = True) -> list:
        """
        Retrieve pool by its id.

        **Be aware that if "fast" is set to False, it may takes longer.**

        :param pool_id: Pools id.
        :type pool_id: int
        
        :param fast: Fast "mode", if set to true only a list of post ids
            will be returned.
        :type fast: bool

        :return: List of post objects (or post ids if fast is set to true).
        :rtype: list[Post|int]
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
        """
        Get post by its id.

        :param post_id: Id of post.
        :type post_id: int

        :return: Post object.
        :rtype: Post
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
            return ret_posts

        for post in response.json():
            ret_posts.append(Post.from_json(post))

        return ret_posts if len(ret_posts) > 1 else (ret_posts[0] if len(ret_posts) == 1 else ret_posts)

    def icame(self, limit: int = 100) -> list:
        """
        Retrieve list of top 100 iCame list.

        :param limit: Limit of returned items.
                        (Default: ``'100'``)
        :type limit: int

        :return: List of iCame objects.
        :rtype: list[ICame]
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
        """
        Get a random post.

        :param tags: Tag list to search. If none, post will be used regardless
                    of it tags.
        :type tags: list[str]

        :return: Post object.
        :rtype: Post
        """

        ## Fixed bug: https://github.com/b3yc0d3/rule34Py/issues/2#issuecomment-902728779
        if tags != None:

            search_raw = self.search(tags, limit=1000)
            if search_raw == []:
                return []

            randnum = random.randint(0, len(search_raw)-1)

            while len(search_raw) <= 0:
                search_raw = self.search(tags)
            else:
                return search_raw[randnum]

        else:
            return self.get_post(self._random_post_id())

    def tagmap(self) -> list:
        """
        Retrieve list of top 100 global tags.

        :return: List of top 100 tags, globally.
        :rtype: list[TopTag]
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

            retData.append(TopTag(rank=rank, tagname=tagname, percentage=percentage))

            #retData.append({
            #    "rank": int(rank),
            #    "tagname": tagname,
            #    "percentage": float(percentage.strip())
            #})

        return retData


    def _random_post_id(self) -> str:
        """
        Get a random posts id.

        **This function is only used internally.**

        :return: Random post id
        :rtype: str
        """

        res = requests.get(API_URLS.RANDOM_POST.value, headers=__headers__)
        parsed = urlparse.urlparse(res.url)

        return parse_qs(parsed.query)['id'][0]

    def _parseUrlParams(self, url: str, params: list) -> str:
        """
        Parse url parameters.

        **This function is only used internally.**

        :return: Url filed with filled in placeholders.
        :rtype: str

        :Example:
            self._parseUrlParams("domain.com/index.php?v={{VERSION}}", [["VERSION", "1.10"]])
        """

        # Usage: _parseUrlParams("domain.com/index.php?v={{VERSION}}", [["VERSION", "1.10"]])
        retURL = url

        for g in params:
            key = g[0]
            value = g[1]

            retURL = retURL.replace("{" + key + "}", value)

        return retURL

    @property
    def stats(self) -> Stats:
        """
        Global Stats.

        :return: Stats class instance.
        :rtype: Stats
        """
        return self._stats

    @property
    def version(self) -> str:
        """
        Rule34Py version.

        :return: Version of rule34py.
        :rtype: str
        """
        return __version__

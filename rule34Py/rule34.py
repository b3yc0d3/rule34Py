# rule34Py - Python api wrapper for rule34.xxx
#
# Copyright (C) 2022 MiningXL <miningxl@gmail.com>
# Copyright (C) 2022-2024 b3yc0d3 <b3yc0d3@gmail.com>
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

"""This module contains the top-level Rule34 API client class."""

from collections.abc import Iterator
from urllib.parse import parse_qs
import random
import urllib.parse as urlparse
import warnings

from bs4 import BeautifulSoup
import requests

from rule34Py.__vars__ import __headers__, __version__, __base_url__
from rule34Py.api_urls import API_URLS
from rule34Py.html import TagMapPage, ICamePage, TopTagsPage
from rule34Py.post import Post
from rule34Py.post_comment import PostComment
from rule34Py.toptag import TopTag

"""
TODO: fix typos
"""

SEARCH_RESULT_MAX = 1000  # API-defined maximum number of search results per request. <https://rule34.xxx/index.php?page=help&topic=dapi>


class rule34Py():
    """The rule34.xxx API client.

    Usage:
    ```python
    client = rule34Py()
    post = client.get_post(1234)
    ```
    """

    user_agent: str = f"Mozilla/5.0 (compatible; rule34Py/{__version__})"

    def __init__(self):
        """Initialize a new rule34 API client instance.

        :return: A new rule34 API client instance.
        :rtype: rule34Py
        """
        pass

    def _get(self, *args, **kwargs) -> requests.Response:
        """Send an HTTP GET request.

        This method largely passes its arguments to the requests.get() method,
        while also inserting a valid User-Agent.

        :return: A requests.Response object from the GET request.
        :rtype: requests.Response
        """
        kwargs["headers"] = kwargs.get("headers", {}) | \
            {"User-Agent": self.user_agent}
        return requests.get(*args, **kwargs)

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
                ret_posts.append(int(id))
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

    def icame(self) -> list:
        """Retrieve list of top 100 iCame list.

        :return: List of iCame objects.
        :rtype: list[ICame]
        """
        response = self._get(API_URLS.ICAME.value)
        response.raise_for_status()
        return ICamePage.top_chart_from_html(response.text)

    def iter_search(
        self,
        tags: list[str] = [],
        max_results: (int | None) = None,
    ) -> Iterator[Post]:
        """Iterate through Post search results, one element at a time.

        This method transparently requests additional results pages until either max_results is reached, or there are no more results. It is possible that additional Posts may be added to the results between page calls, and so it is recommended that you deduplicate results if that is important to you.

        :param tags: Tag list to search.
        :type tags:  list[str]

        :param max_results: The maximum number of results to return before ending the iteration. If 'None', then iteration will continue until the end of the results. Defaults to 'None'.
        :type max_results: int|None

        :return: Yields a Post Iterator.
        :rtype:  Iterator[Post]
        """
        page_id = 0  # what page of the search results we're on
        results_count = 0  # accumulator of how many results have been returned

        while max_results is None or results_count < max_results:
            results = self.search(tags, page_id=page_id)
            if len(results) == 0:  # no results or end of search list
                return
            for result in results:
                if max_results is not None and results_count >= max_results:
                    return
                yield result
                results_count += 1
            page_id += 1

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

    def search(self,
        tags: list[str] = [],
        page_id: int = None,
        limit: int = SEARCH_RESULT_MAX,
    ) -> list[Post]:
        """Search for posts.

        :param tags: List of tags.
        :type tags: list[str]

        :param page_id: Page number/id.
        :type page_id: int

        :param limit: Limit for posts returned per page (max. 1000).
        :type limit: int

        :return: List of Post objects for matching posts.
        :rtype: list[Post]

        For more information, see:

            - `rule34.xxx API Documentation <https://rule34.xxx/index.php?page=help&topic=dapi>`_
        """
        if limit < 0 or limit > SEARCH_RESULT_MAX:
            raise ValueError(f"Search limit must be between 0 and {SEARCH_RESULT_MAX}.")

        params = [
            ["TAGS", "+".join(tags)],
            ["LIMIT", str(limit)],
        ]
        url = API_URLS.SEARCH.value
        # Add "page_id"
        if page_id != None:
            url += f"&pid={{PAGE_ID}}"
            params.append(["PAGE_ID", str(page_id)])

        formatted_url = self._parseUrlParams(url, params)
        response = requests.get(formatted_url, headers=__headers__)
        response.raise_for_status()

        # The Rule34 List API endpoint always returns code 200. But the response
        # might be 0-bytes, if it cannot find the supplied 'tags' param; or an
        # empty JSON array, if there are no results on that 'page_id'.
        if len(response.content) == 0:
            return []

        posts = []
        for post_json in response.json():
            posts.append(Post.from_json(post_json))
        return posts

    def tag_map(self) -> dict[str, str]:
        """Retrieve the tag map points.

        This method uses the tagmap static HTML.
        
        :return: A mapping of country and district codes to their top tag. 3-letter keys are ISO-3 character country codes, 2-letter keys are US-state codes.
        :rtype: dict[str, str]
        """
        resp = self._get(__base_url__ + "static/tagmap.html")
        resp.raise_for_status()
        return TagMapPage.map_points_from_html(resp.text)

    def tagmap(self) -> list[TopTag]:
        """Retrieve list of top 100 global tags.

        This method is deprecated in favor of the top_tags() method.

        :return: List of top 100 tags, globally.
        :rtype: list[TopTag]
        """
        warnings.warn(
            "The rule34Py.tagmap() method is scheduled for deprecation in a future release. If you want to retrieve the Global Top-100 tags list, use the rule34Py.top_tags() method. If you want to retrieve the tag map data points, use the rule34Py.tag_map() method (with an underscore.). See `https://github.com/b3yc0d3/rule34Py/tree/master/docs#functions` for more information.",
            DeprecationWarning,
        )
        return self.top_tags()

    def top_tags(self) -> list[TopTag]:
        """Retrieve list of top 100 global tags.

        :return: List of top 100 tags, globally.
        :rtype: list[TopTag]
        """
        response = self._get(API_URLS.TOPMAP.value)
        response.raise_for_status()
        return TopTagsPage.top_tags_from_html(response.text)

    @property
    def version(self) -> str:
        """Rule34Py version.

        :return: Version of rule34py.
        :rtype: str
        """
        warnings.warn(
            "This method is scheduled for deprecation in a future release of rule34Py. Use `rule34Py.version` instead.",
            DeprecationWarning,
        )
        return __version__

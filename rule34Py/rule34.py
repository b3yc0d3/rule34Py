# rule34Py - Python api wrapper for rule34.xxx
#
# Copyright (C) 2022 MiningXL <miningxl@gmail.com>
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

"""A module containing the top-level Rule34 API client class."""

from collections.abc import Iterator
from typing import Union
from urllib.parse import parse_qs
import os
import urllib.parse as urlparse
import warnings

from bs4 import BeautifulSoup
from requests_ratelimiter import LimiterAdapter
import requests

from rule34Py.__vars__ import (
    __api_url__,
    __base_url__,
    __version__,
)
from rule34Py.api_urls import API_URLS
from rule34Py.html import TagMapPage, ICamePage, TopTagsPage, PoolPage
from rule34Py.pool import Pool
from rule34Py.post import Post
from rule34Py.post_comment import PostComment
from rule34Py.toptag import TopTag


#: The default client user_agent, if one is not specified in the environment.
DEFAULT_USER_AGENT: str = f"Mozilla/5.0 (compatible; rule34Py/{__version__})"
#: API-defined maximum number of search results per request.
#: [`Rule34 Docs <https://rule34.xxx/index.php?page=help&topic=dapi>`_]
SEARCH_RESULT_MAX: int = 1000


class rule34Py():
    """The rule34.xxx API client.

    This class is the primary broker for interactions with the real Rule34 servers.
    It transparently chooses to interact with either the REST server endpoint, or the PHP interactive site, depending on what methods are executed.

    Example:
        .. code-block:: python

            client = rule34Py()
            post = client.get_post(1234)
    """

    CAPTCHA_COOKIE_KEY: str = "cf_clearance"  #: Captcha clearance HTML cookie key

    _base_site_rate_limiter = LimiterAdapter(per_second=1)
    #: Client captcha clearance token. Defaults to either the value of the ``R34_CAPTCHA_CLEARANCE`` environment variable; or None, if the environment variable is not asserted.
    #: Can be overridden at runtime by the user.
    captcha_clearance: Union[str, None] = os.environ.get("R34_CAPTCHA_CLEARANCE", None)
    #: The ``requests.Session`` object used when the client makes HTML requests.
    session: requests.Session = None
    #: The ``User-Agent`` HTML header value used when the client makes HTML requests.
    #: Defaults to either the value of the ``R34_USER_AGENT`` environment variable; or the ``rule34Py.rule34.DEFAULT_USER_AGENT``, if not asserted.
    #: Can be overridden by the user at runtime to change User-Agents.
    user_agent: str = os.environ.get("R34_USER_AGENT", DEFAULT_USER_AGENT)

    def __init__(self):
        """Initialize a new rule34 API client instance."""
        self.session = requests.session()
        self.session.mount(__base_url__, self._base_site_rate_limiter)

    def _get(self, *args, **kwargs) -> requests.Response:
        """Send an HTTP GET request.

        This method largely passes its arguments to the `requests.session.get() <https://requests.readthedocs.io/en/latest/api/#requests.Session.get>`_ method, while also inserting a valid User-Agent and captcha clearance.

        Returns:
            The Response object from the GET request.
        """
        # headers
        kwargs.setdefault("headers", {})
        kwargs["headers"].setdefault("User-Agent", self.user_agent)

        # cookies
        kwargs.setdefault("cookies", {})
        if self.captcha_clearance is not None:
            kwargs["cookies"]["cf_clearance"] = self.captcha_clearance

        return self.session.get(*args, **kwargs)

    def get_comments(self, post_id: int) -> list[PostComment]:
        """Retrieve the comments left on a post.

        Args:
            post_id: The Post's ID number.

        Error:
            Due to a bug in the rule34 site API, the creation timestamp in returned comments are erroneously set to the time that the comment API request is received, not the comments' true creation times.

        Returns:
            List of comments returned from the request.
            If the post has no comments, an empty list will be returned.

        Raises:
            requests.HTTPError: The backing HTTP GET operation failed.
        """  # noqa: DOC502
        params = [
            ["POST_ID", str(post_id)]
        ]
        formatted_url = self._parseUrlParams(API_URLS.COMMENTS, params)
        response = self._get(formatted_url)
        response.raise_for_status()

        comments = []
        comment_soup = BeautifulSoup(response.content.decode("utf-8"), features="xml")
        for e_comment in comment_soup.find_all("comment"):
            comment = PostComment(
                id = e_comment["id"],
                owner_id = e_comment["creator_id"],
                body = e_comment["body"],
                post_id = e_comment["post_id"],
                creation = e_comment["created_at"],
            )
            comments.append(comment)

        return comments

    def get_pool(self, pool_id: int) -> Pool:
        """Retrieve a pool of Posts.

        Note:
            This method uses the interactive website and is rate-limited.

        Args:
            pool_id: The pool's object ID on Rule34.

        Returns:
            A Pool object representing the requested pool.

        Raises:
            requests.HTTPError: The backing HTTP GET operation failed.
        """  # noqa: DOC502
        params = [
            ["POOL_ID", str(pool_id)]
        ]
        response = self._get(self._parseUrlParams(API_URLS.POOL.value, params))
        response.raise_for_status()
        return PoolPage.pool_from_html(response.text)

    def get_post(self, post_id: int) -> Union[Post, None]:
        """Get a Post by its ID.

        Args:
            post_id: The Post's Rule34 ID.

        Returns:
            The Post object matching the post_id; or None, if the post_id is not found.

        Raises:
            requests.HTTPError: The backing HTTP GET operation failed.
        """  # noqa: DOC502
        params = [
            ["POST_ID", str(post_id)]
        ]
        formatted_url = self._parseUrlParams(API_URLS.GET_POST.value, params)
        response = self._get(formatted_url)
        response.raise_for_status()

        # The Posts list API returns an empty response when filters match no posts.
        if len(response.content) == 0:
            return None

        post_json = response.json()
        return Post.from_json(post_json[0])

    def icame(self) -> list["ICame"]:
        """Retrieve a list of the top 100 iCame objects.

        Note:
            This method uses the interactive website and is rate-limited.

        Returns:
            The current top 100 iCame objects.

        Raises:
            requests.HTTPError: The backing HTTP GET operation failed.
        """  # noqa: DOC502
        response = self._get(API_URLS.ICAME.value)
        response.raise_for_status()
        return ICamePage.top_chart_from_html(response.text)

    def iter_search(
        self,
        tags: list[str] = [],
        max_results: Union[int, None] = None,
    ) -> Iterator[Post]:
        """Iterate through Post search results, one element at a time.

        This method transparently requests additional results pages until either ``max_results`` is reached, or there are no more results.
        It is possible that additional Posts may be added to the results between page calls, and so it is recommended that you deduplicate results if that is important to you.

        Args:
            tags: A list of tags to search.
                If the tags list is empty, all posts will be returned.
            max_results: The maximum number of results to return before ending the iteration.
                If ``None``, then iteration will continue until the end of the results.

        Yields:
            An iterator representing each Post element of the search results.

        Raises:
            requests.HTTPError: The backing HTTP GET operation failed.
        """  # noqa: DOC502
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
        """Parse url parameters.

        Args:
            url: URL, containing placeholder values.
            params: A list of parameter values, to substitute into the URL's placeholders.

        Example:
            .. code-block:: python

                formatted_url = _parseUrlParams(
                    "domain.com/index.php?v={{VERSION}}",
                    [["VERSION", "1.10"]]
                    )

        Returns:
            The input URL, reformatted to contain the parameters in place of their placeholders.
        """
        retURL = url

        for g in params:
            key = g[0]
            value = g[1]

            retURL = retURL.replace("{" + key + "}", value)

        return retURL

    def random_post(self) -> Post:
        """Get a random post.

        This method behaves similarly to the website's Post > Random function.

        Note:
            This method uses the interactive website and is rate-limited.

        Returns:
            A random Post.
        
        Raises:
            requests.HTTPError: The backing HTTP GET operation failed.
        """  # noqa: DOC502
        return self.get_post(self.random_post_id())

    def random_post_id(self) -> int:
        """Get a random Post ID.

        This method returns the Post ID contained in the 302 redirect the
        website responds with, when you use the "random post" function.

        Note:
            This method uses the interactive website and is rate-limited.

        Returns:
            A random post ID.

        Raises:
            requests.HTTPError: The backing HTTP GET operation failed.
        """  # noqa: DOC502
        response = self._get(API_URLS.RANDOM_POST.value)
        response.raise_for_status()
        parsed = urlparse.urlparse(response.url)
        return int(parse_qs(parsed.query)['id'][0])

    def search(self,
        tags: list[str] = [],
        page_id: Union[int, None] = None,
        limit: int = SEARCH_RESULT_MAX,
    ) -> list[Post]:
        """Search for posts.

        Args:
            tags: A list of tags to search for.
            page_id: The search page number to request, or None.
                If None, search will eventually return all pages.
            limit: The maximum number of post results to return per page.
                Defaults to ``SEARCH_RESULT_MAX`` (1000, by Rule34 policy).

        Returns:
            A list of Post objects, representing the search results.

        Raises:
            requests.HTTPError: The backing HTTP GET operation failed.
            ValueError: An invalid ``limit`` value was requested.

        References:
            - `rule34.xxx API Documentation <https://rule34.xxx/index.php?page=help&topic=dapi>`_
        """  # noqa: DOC502
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
        response = self._get(formatted_url)
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

    def set_base_site_rate_limit(self, enabled: bool):
        """Enables or disables the base site (rule34.xxx) API rate limiter."""
        if enabled:
            self.session.mount(__base_url__, self._base_site_rate_limiter)
        else:
            del self.session.adapters[__base_url__]

    def tag_map(self) -> dict[str, str]:
        """Retrieve the tag map points.

        Note:
            This method uses the interactive website and is rate-limited.

        Returns:
            A mapping of country and district codes to their top tag.
            3-letter keys are ISO-3 character country codes, 2-letter keys are US-state codes.

        Raises:
            requests.HTTPError: The backing HTTP GET operation failed.
        """  # noqa: DOC502
        resp = self._get(__base_url__ + "static/tagmap.html")
        resp.raise_for_status()
        return TagMapPage.map_points_from_html(resp.text)

    def tagmap(self) -> list[TopTag]:
        """Retrieve list of top 100 global tags.

        Warning:
            This method is deprecated.

        Warn:
            This method is deprecated in favor of the top_tags() method.

        Returns:
            A list of the current top 100 tags, globally.

        Raises:
            requests.HTTPError: The backing HTTP GET operation failed.
        """  # noqa: DOC502
        warnings.warn(
            "The rule34Py.tagmap() method is scheduled for deprecation in a future release. If you want to retrieve the Global Top-100 tags list, use the rule34Py.top_tags() method. If you want to retrieve the tag map data points, use the rule34Py.tag_map() method (with an underscore.). See `https://github.com/b3yc0d3/rule34Py/tree/master/docs#functions` for more information.",
            DeprecationWarning,
        )
        return self.top_tags()

    def top_tags(self) -> list[TopTag]:
        """Retrieve list of top 100 global tags.

        Returns:
            A list of the current top 100 tags, globally.

        Raises:
            requests.HTTPError: The backing HTTP GET operation failed.
        """  # noqa: DOC502
        response = self._get(API_URLS.TOPMAP.value)
        response.raise_for_status()
        return TopTagsPage.top_tags_from_html(response.text)

    @property
    def version(self) -> str:
        """Rule34Py version.

        Warning:
            This method is deprecated.

        Warns:
            This method is deprecated in favor of rule34Py.version.

        Returns:
            The version string of the rule34Py package.
        """
        warnings.warn(
            "This method is scheduled for deprecation in a future release of rule34Py. Use `rule34Py.version` instead.",
            DeprecationWarning,
        )
        return __version__

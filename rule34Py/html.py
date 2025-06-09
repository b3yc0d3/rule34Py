# rule34Py - Python api wrapper for rule34.xxx
# 
# Copyright (C) 2025 b3yc0d3 <b3yc0d3@gmail.com>
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
"""This module contains classes for parsing HTML pages from the rule34.xxx site."""

from datetime import datetime
import json
import re

from bs4 import BeautifulSoup

from rule34Py.icame import ICame
from rule34Py.pool import Pool, PoolHistoryEvent
from rule34Py.toptag import TopTag


class ICamePage():
    """The Rule34 'icame' page.

    https://rule34.xxx/index.php?page=icame

    This class can be instantiated as an object that automatically parses
    the useful information from the page's html, or used as a static class
    to parse the page's html directly.

    Args:
        html: The page HTML to parse.
    """

    #: The top icame results, in descending order.
    #: ie. element 0 is the most popular tag.
    top_chart: list[ICame] = []

    def __init__(self, html: str):
        """Create a new ICamePage object."""
        self.top_chart = ICamePage.top_chart_from_html(html)

    @staticmethod
    def top_chart_from_html(html: str) -> list[ICame]:
        """Parse the ICame Top 100 chart from the page html.

        Args:
            html: The ICame page HTML, as a string.

        Returns:
            A list of the top 100 ICame characters and their counts.
        """
        e_doc = BeautifulSoup(html, features="html.parser")

        top_chart = []
        e_rows = e_doc.find("table", class_="highlightable").find("tbody").find_all("tr")
        for e_row in e_rows:
            if e_row is None:
                continue
            
            character_name = e_row.select('td > a', href=True)[0].get_text(strip=True)
            count = e_row.select('td')[2].get_text(strip=True)

            top_chart.append(ICame(character_name, count))

        return top_chart


class PoolHistoryPage():
    """A Rule34 Pool history page."""

    @staticmethod
    def events_from_html(html: str) -> list[PoolHistoryEvent]:
        """Parse the history event entries from the page html.

        Args:
            html: The pool history page HTML to parse.

        Returns:
            A list of ``PoolHistoryEvents`` representing the changes in this Pool.
        """
        e_doc = BeautifulSoup(html, "html.parser")

        events = []
        e_events_table = e_doc.find("div", id="content").find("table")
        for e_row in e_events_table.find("tbody").find_all("tr"):
            e_data = e_row.find_all("td")

            post_ids = e_data[0].text.split(" ")
            post_ids = [int(id) for id in post_ids]
            uname = e_data[1].text
            date = datetime.fromisoformat(e_data[2].text)

            events.append(PoolHistoryEvent(
                date = date,
                updater_uname = uname,
                post_ids = post_ids,
            ))

        return events


class PoolPage():
    """A Rule34 post Pool page."""

    #: Regex matcher for the pool's ID.
    RE_PAGE_ID = re.compile(r"id=(\d+)")

    @staticmethod
    def pool_from_html(html: str) -> Pool:
        """Generate a Pool object from the page HTML.

        Args:
            html: The pool page HTML, as a string.

        Returns:
            A Pool object representing the parsed page information.
        """
        e_doc = BeautifulSoup(html, "html.parser")
        e_content = e_doc.find("div", id="content")

        # The pool html does not explicitly describe the pool ID anywhere, so
        # extract it implicitly from the pool history link href.
        e_subnavbar = e_doc.find("ul", id="subnavbar")
        e_history = e_subnavbar.find_all("a")[-1]  # last link on the bar
        assert e_history.text == "History"  # check for safety
        id_match = re.search(r"id=(\d+)", e_history["href"])
        pool_id = int(id_match.group(1))

        e_title = e_content.find("h4")
        name = e_title.text.removeprefix("Pool: ")

        description = e_title.find_next_sibling("div").text

        pool = Pool(
            pool_id = pool_id,
            name = name,
            description = description,
        )

        e_pool = e_content.find("div", id="pool-show")
        for e_post in e_pool.find_all("span", class_="thumb"):
            post_id = int(e_post["id"].removeprefix("p"))
            pool.posts.append(post_id)

        return pool


class TagMapPage():
    """The rule34.xxx/static/tagmap.html page.

    This class can be instantiated as an object that automatically parses
    the useful information from the page's html, or used as a static class
    to parse the page's html directly.

    Args:
        html: The Tag Map page HTML, as a string.
    """

    #: Regex matcher for the TagMap page's plotly plot
    RE_NEWPLOT = re.compile(r"newPlot\((.*)\)", flags=re.S)
    #: Regex matcher for each plotly point on the tag map
    RE_PLOT_POINT = re.compile(r"({[^}]+})", flags=re.S)
    #: The JSON keys of the data points embedded in the plotly block
    MAP_POINT_KEYS = {"locationmode", "locations", "text"}

    #: The most popular tag in each country or region code.
    #: Formatted as ``[location_code, top_tag]``.
    map_points: dict[str, str] = {}

    def __init__(self, html: str):
        """Create a new TagMapPage from the page's HTML."""
        self.map_points = TagMapPage.map_points_from_html(html)

    @staticmethod
    def map_points_from_html(html: str) -> dict[str, str]:
        """Parse the map data from a Tag Map Page.
        
        Args:
            html: The Tag Map page HTML as a string.

        Returns:
            The map data as a dictionary of ``[location_code, top_tag]``.
        """
        e_doc = BeautifulSoup(html, "html.parser")
        map_points = {}

        # The map plot script is the 3rd script in the page.
        e_script_plot = list(e_doc.find_all("script"))[2]
        match_newplot = TagMapPage.RE_NEWPLOT.search(e_script_plot.text)
        match_points = TagMapPage.RE_PLOT_POINT.findall(match_newplot.group(1))
        for match_point in match_points:
            try:
                point_data = json.loads(match_point)
            except json.decoder.JSONDecodeError:
                # some matches are not tag points and aren't even JSON
                continue
            if not TagMapPage.MAP_POINT_KEYS.issubset(point_data.keys()):
                continue
            for location in point_data["locations"]:
                map_points[location] = point_data["text"]

        return map_points


class TopTagsPage():
    """The rule34.xxx/index.php?Page=toptags page.

    This class can be instantiated as an object that automatically parses
    the useful information from the page's html, or used as a static class
    to parse the page's html directly.

    Args:
        html: The Top Tags page HTML, as a string.
    """

    #: The top-tags ranking list on this page.
    top_tags: list[TopTag] = []

    def __init__(self, html: str):
        """Create a new TopTagsPage from the page's HTML."""
        self.top_tags = TopTagsPage.top_tags_from_html(html)

    @staticmethod
    def top_tags_from_html(html: str) -> list[TopTag]:
        """Parse the "Top 100 tags, global" table from the page.

        Args:
            html: The Top Tags page HTML, as a string.

        Returns:
            A list of TopTags representing the top 100 chart.
        """
        e_doc = BeautifulSoup(html, features="html.parser")
        e_rows = e_doc.find("table", class_="server-assigns").find_all("tr")

        top_tags = []
        # Skip the first two rows; they are the table title and headers.
        for e_row in e_rows[2:]:
            e_tags = e_row.find_all("td")

            rank = e_tags[0].string[1:]
            tagname = e_tags[1].string
            percentage = e_tags[2].string[:-1]

            top_tags.append(TopTag(
                rank=rank,
                tagname=tagname,
                percentage=percentage,
            ))

        return top_tags

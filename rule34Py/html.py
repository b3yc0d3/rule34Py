"""This module contains classes for parsing HTML pages from the rule34.xxx site."""

from datetime import datetime
import json
import re

from bs4 import BeautifulSoup

from rule34Py.icame import ICame
from rule34Py.toptag import TopTag
from rule34Py.pool import Pool, PoolHistoryEvent


class ICamePage():
    """The Rule34 'icame' page.
    
    This class can be instantiated as an object that automatically parses
    the useful information from the page's html, or used as a static class
    to parse the page's html directly.
    """

    top_chart: list[ICame] = []

    def __init__(self, html: str):
        self.top_chart = ICamePage.top_chart_from_html(html)

    @staticmethod
    def top_chart_from_html(html: str) -> list[ICame]:
        """Parse the ICame Top 100 chart from the page html.
        
        :returns: A list of the top 100 ICame characters and their counts.
        :rtype: list[ICame]
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
    """A Rule34 Pool history page.
    """

    @staticmethod
    def events_from_html(html: str) -> list[PoolHistoryEvent]:
        """Parse the history event entries from the page html."""
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

    RE_PAGE_ID = re.compile(r"id=(\d+)")

    @staticmethod
    def pool_from_html(html: str) -> Pool:
        """Generate a Pool object from the page HTML."""
        e_doc = BeautifulSoup(html, "html.parser")
        e_content = e_doc.find("div", id="content")

        # The pool html does not explicitly describe the pool ID anywhere, so
        # extract it implictly from the pool history link href.
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
    """

    RE_NEWPLOT = re.compile(r"newPlot\((.*)\)", flags=re.S)
    RE_PLOT_POINT = re.compile(r"({[^}]+})", flags=re.S)
    MAP_POINT_KEYS = {"locationmode", "locations", "text"}

    map_points: dict[str, str] = {}

    def __init__(self, html: str):
        self.map_points = TagMapPage.map_points_from_html(html)

    @staticmethod
    def map_points_from_html(html: str) -> dict[str, str]:
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
    """

    top_tags: list[TopTag] = []

    def __init__(self, html: str):
        self.top_tags = TopTagsPage.top_tags_from_html(html)
        
    @staticmethod
    def top_tags_from_html(html: str) -> list[TopTag]:
        """Parse the "Top 100 tags, global" table from the page.
        
        :returns: A list of TopTags representing the top 100 chart.
        :rtype: list[TopTag]
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

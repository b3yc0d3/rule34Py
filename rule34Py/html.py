"""This module contains classes for parsing HTML pages from the rule34.xxx site."""

import json
import re

from bs4 import BeautifulSoup


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

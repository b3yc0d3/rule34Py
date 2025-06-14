"""This module contains unit tests for the rule34Py top-level module."""

import re

import rule34Py


def test__module__metadata():
    """The module should contain author name, email, and version dunders."""
    RE_VERSION = re.compile(r"^\d+\.\d+\.\d+$")

    assert rule34Py.__author__ == "b3yc0d3"
    assert rule34Py.__email__ == "b3yc0d3@gmail.com"
    assert RE_VERSION.match(rule34Py.__version__)

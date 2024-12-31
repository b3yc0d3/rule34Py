"""This module contains unit tests for the rule34Py top-level module."""

import re

import rule34Py


def test_version():
    """The module should contain a version triplet in a `version` variable."""
    RE_VERSION = re.compile(r"^\d+\.\d+\.\d+$")
    assert RE_VERSION.match(rule34Py.version)

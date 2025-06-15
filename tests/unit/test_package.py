"""Tests for package metadata and composition."""

from importlib.metadata import metadata, version

import packaging.version
import pytest


PACKAGE_NAME = "rule34Py"  # The expected name of the package.


def test__package__metadata():
    """The package metadata should contain correct ownership and license
    versions, and accessible version metadata."""
    data = metadata(PACKAGE_NAME)
    assert data["Maintainer"] == "b3yc0d3"
    assert data["Maintainer-email"] == "b3yc0d3@gmail.com"
    assert data["Name"] == PACKAGE_NAME
    assert data["License"] == "GPL-3.0-only"

    # The package version should be exposed via the importlib.metadata.version
    # method and be PEP 440 compliant.
    try:
        packaging.version.parse(data["Version"])
        packaging.version.parse(version(PACKAGE_NAME))
    except packaging.version.InvalidVersion:
        pytest.fail(f"Invalid version string. {version(PACKAGE_NAME)}")

    # The package keywords MUST note that it is an NSFW package.
    assert set(["adult", "nsfw"]).issubset(data["Keywords"].split(","))

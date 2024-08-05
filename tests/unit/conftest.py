import pytest

from rule34Py import rule34Py
from tests.fixtures import mock34


@pytest.fixture(scope="module")
def rule34(mock34):
    r34 = rule34Py()
    yield r34

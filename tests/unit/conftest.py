import pytest

from rule34Py import rule34Py
from tests.fixtures import mock34


@pytest.fixture(scope="module")
def rule34(mock34):
    r34 = rule34Py()
    r34.api_key = "0000000"
    r34.user_id = "0000000"
    yield r34

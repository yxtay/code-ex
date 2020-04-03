import pytest

from src.merge_the_tools import merge_the_tools

cases = [
    ("AABCAAADA", 3, ["AB", "CA", "AD"]),
]


@pytest.mark.parametrize("string, k,expected", cases)
def test(string, k, expected):
    result = merge_the_tools(string, k)
    assert result == expected

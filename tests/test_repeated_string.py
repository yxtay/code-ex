import pytest

from src.repeated_string import repeatedString

cases = [
    ("aba", 10, 7),
    ("a", 1000000000000, 1000000000000),
]


@pytest.mark.parametrize("s,n,expected", cases)
def test(s, n, expected):
    s = "aba"
    n = 10
    expected = 7
    result = repeatedString(s, n)
    assert result == expected

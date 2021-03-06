import pytest

from src.two_strings import two_strings

cases = [
    ("hello", "world", "YES"),
    ("hi", "world", "NO"),
]


@pytest.mark.parametrize("s1, s2, expected", cases)
def test(s1, s2, expected):
    result = two_strings(s1, s2)
    assert result == expected

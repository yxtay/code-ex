import pytest

from src.sherlock_anagrams import sherlock_anagrams

cases = [
    ("abba", 4),
    ("abcd", 0),
    ("ifailuhkqq", 3),
    ("kkkk", 10),
    ("cdcd", 5),
]


@pytest.mark.parametrize("s, expected", cases)
def test(s, expected):
    result = sherlock_anagrams(s)
    assert result == expected

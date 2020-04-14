import pytest

from src.make_anagram import make_anagram

cases = [
    ("cde", "abc", 4),
    ("cde", "dcf", 2),
]


@pytest.mark.parametrize("a, b, expected", cases)
def test(a, b, expected):
    result = make_anagram(a, b)
    assert result == expected

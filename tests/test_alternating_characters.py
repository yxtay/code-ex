import pytest

from src.alternating_characters import alternating_characters

cases = [
    ("AAAA", 3),
    ("BBBBB", 4),
    ("ABABABAB", 0),
    ("BABABA", 0),
    ("AAABBB", 4),
]


@pytest.mark.parametrize("s, expected", cases)
def test(s, expected):
    result = alternating_characters(s)
    assert result == expected

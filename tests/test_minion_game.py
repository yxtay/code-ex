import pytest

from src.minion_game import minion_game

cases = [
    ("BANANA", ("STUART", 12)),
]


@pytest.mark.parametrize("string,expected", cases)
def test(string, expected):
    result = minion_game(string)
    assert result == expected

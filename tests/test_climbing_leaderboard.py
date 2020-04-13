import pytest

from src.climbing_leaderboard import climbing_leaderboard

cases = [
    ([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120], [6, 4, 2, 1]),
    ([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102], [6, 5, 4, 2, 1]),
]


@pytest.mark.parametrize("scores, alice, expected", cases)
def test(scores, alice, expected):
    result = climbing_leaderboard(scores, alice)
    assert result == expected

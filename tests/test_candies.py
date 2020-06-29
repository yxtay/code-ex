import pytest

from src.candies import candies

cases = [
    (3, [1, 2, 2], 4),
    (10, [2, 4, 2, 6, 1, 7, 8, 9, 2, 1], 19),
    (8, [2, 4, 3, 5, 2, 6, 4, 5], 12),
    (3, [3, 2, 1], 6),
]


@pytest.mark.parametrize("n, arr, expected", cases)
def test_candles(n, arr, expected):
    result = candies(n, arr)
    assert result == expected

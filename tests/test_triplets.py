import pytest

from src.triplets import triplets

cases = [
    ([1, 3, 5], [2, 3], [1, 2, 3], 8),
    ([1, 4, 5], [2, 3, 3], [1, 2, 3], 5),
    ([1, 3, 5, 7], [5, 7, 9], [7, 9, 11, 13], 12),
]


@pytest.mark.parametrize("a, b, c, expected", cases)
def test_pairs(a, b, c, expected):
    result = triplets(a, b, c)
    assert result == expected

import pytest

from src.rot_left import rotLeft

cases = [
    ([1, 2, 3, 4, 5], 4, [5, 1, 2, 3, 4]),
    ([41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51],
     10,
     [77, 97, 58, 1, 86, 58, 26, 10, 86, 51, 41, 73, 89, 7, 10, 1, 59, 58, 84, 77]),
    ([33, 47, 70, 37, 8, 53, 13, 93, 71, 72, 51, 100, 60, 87, 97],
     13,
     [87, 97, 33, 47, 70, 37, 8, 53, 13, 93, 71, 72, 51, 100, 60]),
]


@pytest.mark.parametrize("a,d,expected", cases)
def test(a, d, expected):
    result = rotLeft(a, d)
    assert result == expected

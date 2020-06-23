import pytest

from src.non_divisible_subset import non_divisible_subset

cases = [
    (3, [1, 7, 2, 4], 3),
    (7, [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436], 11),
]


@pytest.mark.parametrize("k, s, expected", cases)
def test(k, s, expected):
    result = non_divisible_subset(k, s)
    assert result == expected

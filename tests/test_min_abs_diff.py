import pytest

from src.min_abs_diff import min_abs_diff

cases = [
    ([3, -7, 0], 3),
    ([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75], 1),
    ([1, -3, 71, 68, 17], 3),
]


@pytest.mark.parametrize("arr, expected", cases)
def test(arr, expected):
    result = min_abs_diff(arr)
    assert result == expected

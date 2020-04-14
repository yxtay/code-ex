import pytest

from src.count_swaps import count_swaps

cases = [
    ([6, 4, 1], (3, 1, 6)),
    ([3, 2, 1], (3, 1, 3)),
    ([4, 2, 3, 1], (5, 1, 4))
]


@pytest.mark.parametrize("arr, expected", cases)
def test(arr, expected):
    result = count_swaps(arr)
    assert result == expected

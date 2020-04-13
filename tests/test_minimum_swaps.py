import pytest

from src.minimum_swaps import minimum_swaps

cases = [
    ([7, 1, 3, 2, 4, 5, 6], 5),
    ([4, 3, 1, 2], 3),
    ([2, 3, 4, 1, 5], 3),
    ([1, 3, 5, 2, 4, 6, 7], 3),
]


@pytest.mark.parametrize("arr, expected", cases)
def test(arr, expected):
    result = minimum_swaps(arr)
    assert result == expected

import pytest

from src.max_subset_sum import max_subset_sum

cases = [
    ([3, 7, 4, 6, 5], 13),
    ([2, 1, 5, 8, 4], 11),
    ([3, 5, -7, 8, 10], 15),
    ([3, 5, -7, 8, 10, 1], 15),
    ([3, 7], 7),
    ([3], 3),
]


@pytest.mark.parametrize("arr, expected", cases)
def test_max_subset_sum(arr, expected):
    result = max_subset_sum(arr)
    assert result == expected

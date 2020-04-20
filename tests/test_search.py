import pytest

from src.search import linear_search

cases = [([12, 1, 34, 17], 17, 3), ([2, 3, 56, 13, 1], 56, 2)]


@pytest.mark.parametrize("arr, key, expected", cases)
def test_linear_search(arr, key, expected):
    result = linear_search(arr, key)
    assert result == expected

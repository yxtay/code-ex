import pytest

from src.unfairness import max_min

cases = [
    (3, [10, 100, 300, 200, 1000, 20, 30], 20),
    (4, [1, 2, 3, 4, 10, 20, 30, 40, 100, 200], 3),
    (2, [1, 2, 1, 2, 1], 0),
]


@pytest.mark.parametrize("k, arr, expected", cases)
def test_max_min(k, arr, expected):
    result = max_min(k, arr)
    assert result == expected

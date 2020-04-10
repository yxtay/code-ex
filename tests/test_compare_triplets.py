import pytest

from src.compare_triplets import compare_triplets

cases = [
    ([5, 6, 7], [3, 6, 10], [1, 1]),
    ([17, 28, 30], [99, 16, 8], [2, 1]),
    ([1, 2, 3], [1, 2, 3], [0, 0]),
    ([6, 8, 12], [7, 9, 15], [0, 3]),
]


@pytest.mark.parametrize("a, b, expected", cases)
def test(a, b, expected):
    result = compare_triplets(a, b)
    assert result == expected

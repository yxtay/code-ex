import pytest

from src.count_triplets import count_triplets

cases = [
    ([1, 2, 2, 4], 2, 2),
    ([1, 3, 9, 9, 27, 81], 3, 6),
    ([1, 5, 5, 25, 125], 5, 4),
    ([1, 2, 1, 2, 4], 2, 3)
]


@pytest.mark.parametrize("arr, r, expected", cases)
def test(arr, r, expected):
    result = count_triplets(arr, r)
    assert result == expected

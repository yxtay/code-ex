import pytest

from src.simple_array_sum import simple_array_sum

cases = [
    ([1, 2, 3], 6),
    ([1, 2, 3, 4, 10, 11], 31),
    ([338, 65, 713, 595, 428, 610, 728, 573, 871, 868], 5789),
]


@pytest.mark.parametrize("arr, expected", cases)
def test(arr, expected):
    result = simple_array_sum(arr)
    assert result == expected

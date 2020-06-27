import pytest

from src.get_minimum_cost import get_minimum_cost

cases = [
    (3, [2, 5, 6], 13),
    (2, [2, 5, 6], 15),
    (3, [1, 3, 5, 7, 9], 29),
    (2, [1, 3, 5, 7, 9], 35),
]


@pytest.mark.parametrize("friends, flowers, expected", cases)
def test_get_minimum_cost(friends, flowers, expected):
    result = get_minimum_cost(friends, flowers)
    assert result == expected

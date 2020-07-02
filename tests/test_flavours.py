import pytest

from src.flavours import what_flavours

cases = [
    ([1, 4, 5, 3, 2], 4, (1, 4)),
    ([2, 2, 4, 3], 4, (1, 2)),
]


@pytest.mark.parametrize("cost, money, expected", cases)
def test_what_flavours(cost, money, expected):
    result = what_flavours(cost, money)
    assert result == expected

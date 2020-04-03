import pytest

from src.sock_merchant import sockMerchant

cases = [
    (9, [10, 20, 20, 10, 10, 30, 50, 10, 20], 3),
    (10, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3], 4),
]


@pytest.mark.parametrize("n,ar,expected", cases)
def test_1(n, ar, expected):
    result = sockMerchant(n, ar)
    assert result == expected

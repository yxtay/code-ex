import pytest

from src.extra_long_factorials import extra_long_factorials

cases = [
    (25, 15511210043330985984000000),
    (30, 265252859812191058636308480000000),
]


@pytest.mark.parametrize("n, expected", cases)
def test(n, expected):
    result = extra_long_factorials(n)
    assert result == expected

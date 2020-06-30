import pytest

from src.super_digit import super_digit

cases = [
    ("9875", 1, 2),
    ("9875", 4, 8),
    ("148", 3, 3),
    ("123", 3, 9),
    ("0", 1, 0),
    ("999", 9, 9),
]


@pytest.mark.parametrize("n, k, expected", cases)
def test_super_digit(n, k, expected):
    result = super_digit(n * k)
    assert result == expected

import pytest

from src.staircase import staircase

cases = [
    (5, 13),
    (1, 1),
    (3, 4),
    (7, 44),
]


@pytest.mark.parametrize("n, expected", cases)
def test_staircase(n, expected):
    result = staircase(n)
    assert result == expected

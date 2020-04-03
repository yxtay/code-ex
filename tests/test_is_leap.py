import pytest

from src.is_leap import is_leap

cases = [
    (1990, False),
    (2000, True),
    (2004, True),
    (2100, False),
    (2400, True),
    (3455, False),
    (1992, True),
]


@pytest.mark.parametrize("year,expected", cases)
def test(year, expected):
    result = is_leap(year)
    assert result == expected

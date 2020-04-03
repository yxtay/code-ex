import pytest

from src.counting_valleys import countingValleys

cases = [
    (8, "UDDDUDUU", 1),
    (12, "DDUUDDUDUUUD", 2),
]


@pytest.mark.parametrize("n,s,expected", cases)
def test(n, s, expected):
    result = countingValleys(n, s)
    assert result == expected

import pytest

from src.abbreviation import abbreviation, abbreviation_dp

cases = [
    ("daBcd", "ABC", True),
    ("aaAA", "AA", True),
    ("AbCdE", "AFE", False),
    ("beFgH", "EFG", False),
    ("beFgH", "EFH", True),
]


@pytest.mark.parametrize("a, b, expected", cases)
def test_abbreviation(a, b, expected):
    result = abbreviation(a, b)
    assert result == expected


@pytest.mark.parametrize("a, b, expected", cases)
def test_abbreviation_dp(a, b, expected):
    result = abbreviation_dp(a, b)
    assert result == expected

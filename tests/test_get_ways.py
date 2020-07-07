import pytest

from src.get_ways import get_ways, get_ways_dp, get_ways_memo

cases = [(4, [1, 2, 3], 4), (10, [2, 5, 3, 6], 5)]


@pytest.mark.parametrize("n, c, expected", cases)
def test_get_ways(n, c, expected):
    result = get_ways(n, c)
    assert result == expected


@pytest.mark.parametrize("n, c, expected", cases)
def test_get_ways_memo(n, c, expected):
    result = get_ways_memo(n, c)
    assert result == expected


@pytest.mark.parametrize("n, c, expected", cases)
def test_get_ways_dp(n, c, expected):
    result = get_ways_dp(n, c)
    assert result == expected

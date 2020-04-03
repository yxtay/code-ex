import pytest

from src.jumping_on_clouds import jumpingOnClouds

cases = [
    (7, [0, 0, 1, 0, 0, 1, 0], 4),
    (6, [0, 0, 0, 1, 0, 0], 3),
]


@pytest.mark.parametrize("n,c,expected", cases)
def test(n, c, expected):
    result = jumpingOnClouds(c)
    assert result == expected

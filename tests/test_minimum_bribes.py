import pytest

from src.minimum_bribes import minimum_bribes

cases = [
    ([2, 1, 5, 3, 4], 3),
    ([2, 5, 1, 3, 4], None),
]


@pytest.mark.parametrize("q, expected", cases)
def test(q, expected):
    result = minimum_bribes(q)
    assert result == expected

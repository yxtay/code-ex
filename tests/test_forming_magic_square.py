import pytest

from src.forming_magic_square import forming_magic_square

cases = [
    ([[5, 3, 4], [1, 5, 8], [6, 4, 2]], 7),
    ([[4, 9, 2], [3, 5, 7], [8, 1, 5]], 1),
    ([[4, 8, 2], [4, 5, 7], [6, 1, 6]], 4),
    ([[4, 5, 8], [2, 4, 1], [1, 9, 7]], 14),
    ([[2, 9, 8], [4, 2, 7], [5, 6, 7]], 21),
    ([[4, 4, 7], [3, 1, 5], [1, 7, 9]], 20),
]


@pytest.mark.parametrize("s, expected", cases)
def test(s, expected):
    result = forming_magic_square(s)
    assert result == expected

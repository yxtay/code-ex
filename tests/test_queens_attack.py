import pytest

from src.queens_attack import queens_attack

cases = [
    (4, 0, 4, 4, [], 9),
    (5, 3, 4, 3, [[5, 5], [4, 2], [2, 3]], 10),
    (1, 0, 1, 1, [], 0),
]


@pytest.mark.parametrize("n, k, r_q, c_q, obstacles, expected", cases)
def test_queens_attack(n, k, r_q, c_q, obstacles, expected):
    result = queens_attack(n, k, r_q, c_q, obstacles)
    assert result == expected

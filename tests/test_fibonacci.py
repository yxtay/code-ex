import pytest

from src.fibonacci import fibonacci, fibonacci_cache, fibonacci_lru, fibonacci_mem

cases = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
]


@pytest.mark.parametrize("n, expected", cases)
def test_fibonacci(n, expected):
    result = fibonacci(n)
    assert result == expected


@pytest.mark.parametrize("n, expected", cases)
def test_fibonacci_mem(n, expected):
    result = fibonacci_mem(n)
    assert result == expected


@pytest.mark.parametrize("n, expected", cases)
def test_fibonacci_cache(n, expected):
    result = fibonacci_cache(n)
    assert result == expected


@pytest.mark.parametrize("n, expected", cases)
def test_fibonacci_lru(n, expected):
    result = fibonacci_lru(n)
    assert result == expected

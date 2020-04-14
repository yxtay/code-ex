import pytest

from src.freq_query import freq_query

cases = [
    ([(1, 1), (2, 2), (3, 2), (1, 1), (1, 1), (2, 1), (3, 2)], [0, 1]),
    ([(3, 4), (2, 1003), (1, 16), (3, 1)], [0, 1]),
]


@pytest.mark.parametrize("queries, expected", cases)
def test(queries, expected):
    result = freq_query(queries)
    assert result == expected

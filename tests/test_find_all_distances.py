import pytest

from src.find_all_distances import Graph

cases = [
    (4, [[1, 2], [1, 3]], 1, [6, 6, -1]),
    (3, [[2, 3]], 2, [-1, 6]),
    (6, [[1, 2], [2, 3], [3, 4], [1, 5]], 1, [6, 12, 18, 6, -1]),
    (7, [[1, 2], [1, 3], [3, 4], [2, 5]], 2, [6, 12, 18, 6, -1, -1]),
]


@pytest.mark.parametrize("n, connections, source, expected", cases)
def test_abbreviation(n, connections, source, expected):
    graph = Graph(n)
    for s, d in connections:
        graph.connect(s - 1, d - 1)
    result = graph.find_all_distances(source - 1)
    assert result == expected

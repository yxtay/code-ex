import pytest

from src.nearest_clone import find_shortest

cases = [
    (4, [1, 1, 4], [2, 3, 2], [1, 2, 1, 1], 1, 1),
    (4, [1, 1, 4], [2, 3, 2], [1, 2, 3, 4], 2, -1),
    (5, [1, 1, 2, 3], [2, 3, 4, 5], [1, 2, 3, 3, 2], 2, 3),
]


@pytest.mark.parametrize("graph_nodes, graph_from, graph_to, ids, val, expected", cases)
def test_find_shortest(graph_nodes, graph_from, graph_to, ids, val, expected):
    result = find_shortest(graph_nodes, graph_from, graph_to, ids, val)
    assert result == expected

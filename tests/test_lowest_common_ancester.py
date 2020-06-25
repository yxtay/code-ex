import pytest

from src.lowest_common_ancester import BinarySearchTree, lowest_common_ancester

cases = [
    ([4, 2, 3, 1, 7, 6], [1, 7], 4),
    ([4, 2, 3, 1, 7, 6], [4, 7], 4),
    ([4, 2, 3, 1, 7, 6], [1, 3], 2),
    ([4, 2, 3, 1, 7, 6], [2, 3], 2),
    ([4, 2, 3, 1, 7, 6], [1, 2], 2),
    ([4, 2, 3, 1, 7, 6], [2, 6], 4),
    ([1, 2], [1, 2], 1),
    ([5, 3, 8, 2, 4, 6, 7], [7, 3], 5),
    ([8, 4, 9, 1, 2, 3, 6, 5], [1, 2], 1),
    ([9, 7, 8, 5, 6, 4, 3, 1], [1, 6], 5),
    ([8, 4, 2, 1, 3, 6, 5, 7, 10, 14, 15, 9, 12, 11, 13], [15, 11], 14),
]


@pytest.mark.parametrize("values, queries, expected", cases)
def test_lowest_common_ancester(values, queries, expected):
    tree = BinarySearchTree()
    for val in values:
        tree.create(val)
    result = lowest_common_ancester(tree.root, *queries)
    assert result.info == expected

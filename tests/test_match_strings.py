import pytest

from src.match_strings import matching_strings

cases = [
    (["ab", "ab", "abc"], ["ab", "abc", "bc"], [2, 1, 0]),
    (["aba", "baba", "aba", "xzxb"], ["aba", "xzxb", "ab"], [2, 1, 0]),
    (["def", "de", "fgh"], ["de", "lmn", "fgh"], [1, 0, 1]),
]


@pytest.mark.parametrize("strings, queries, expected", cases)
def test_matching_strings(strings, queries, expected):
    result = matching_strings(strings, queries)
    assert result == expected

import pytest

from src.is_balanced import is_balanced

cases = [
    ("{[()]}", True),
    ("{[(])}", False),
    ("{{[[(())]]}}", True),
]


@pytest.mark.parametrize("s, expected", cases)
def test_is_balanced(s, expected):
    result = is_balanced(s)
    assert result == expected

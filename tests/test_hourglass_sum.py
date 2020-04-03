import pytest

from src.hourglass_sum import hourglassSum

cases = [
    ("""
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
""", 19),
    ("""
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 9 2 -4 -4 0
0 0 0 -2 0 0
0 0 -1 -2 -4 0
""", 13),
    ("""
-9 -9 -9 1 1 1
0 -9 0 4 3 2
-9 -9 -9 1 2 3
0 0 8 6 6 0
0 0 0 -2 0 0
0 0 1 2 4 0
""", 28),
]


@pytest.mark.parametrize("arr_str,expected", cases)
def test(arr_str, expected):
    arr = []
    for line in arr_str.strip().split("\n"):
        arr.append(list(map(int, line.rstrip().split())))
    result = hourglassSum(arr)
    assert result == expected

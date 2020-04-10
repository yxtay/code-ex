import pytest

from src.reverse_array import reverse_array

cases = [
    ([1, 4, 3, 2], [2, 3, 4, 1]),
    ([6676, 3216, 4063, 8373, 423, 586, 8850, 6762], [6762, 8850, 586, 423, 8373, 4063, 3216, 6676]),
    ([305, 97, 1290, 5591, 5930, 9317, 440, 6533, 7470], [7470, 6533, 440, 9317, 5930, 5591, 1290, 97, 305]),
    ([9053, 4443], [4443, 9053]),
    ([5833, 9919, 6731], [6731, 9919, 5833]),
]


@pytest.mark.parametrize("arr, expected", cases)
def test(arr, expected):
    result = reverse_array(arr)
    assert result == expected

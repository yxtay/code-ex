import pytest

from src.pairs import pairs

cases = [
    (2, [1, 5, 3, 4, 2], 3),
    (
        1,
        [
            363374326,
            364147530,
            61825163,
            1073065718,
            1281246024,
            1399469912,
            428047635,
            491595254,
            879792181,
            1069262793,
        ],
        0,
    ),
    (2, [1, 3, 5, 8, 6, 4, 2], 5),
]


@pytest.mark.parametrize("k, arr, expected", cases)
def test_pairs(k, arr, expected):
    result = pairs(k, arr)
    assert result == expected

from collections import Counter

import pytest

from src.activity_notifications import activity_notifications, compute_median

cases = [
    ([10, 20, 30], 20),
    ([20, 30, 40], 30),
    ([30, 40, 50], 40),
    ([10, 20, 30, 40], 25),
    ([1, 1, 1], 1),
    ([1, 1, 1, 1], 1),
]


@pytest.mark.parametrize("arr, expected", cases)
def test_median(arr, expected):
    result = compute_median(Counter(arr))
    assert result == expected


cases = [([10, 20, 30, 40, 50], 3, 1), ([2, 3, 4, 2, 3, 6, 8, 4, 5], 5, 2), ([1, 2, 3, 4, 4], 4, 0)]


@pytest.mark.parametrize("expenditure, d, expected", cases)
def test(expenditure, d, expected):
    result = activity_notifications(expenditure, d)
    assert result == expected

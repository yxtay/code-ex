import pytest

from src.time_delta import time_delta

cases = [
    ("Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000", 25200),
    ("Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000", 88200),
]


@pytest.mark.parametrize("t1,t2,expected", cases)
def test(t1, t2, expected):
    result = time_delta(t1, t2)
    assert result == expected

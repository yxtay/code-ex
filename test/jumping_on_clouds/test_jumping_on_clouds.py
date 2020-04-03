from src.jumping_on_clouds.main import jumpingOnClouds


def test_1():
    n = 7
    c = [0, 0, 1, 0, 0, 1, 0]
    expected = 4
    result = jumpingOnClouds(c)
    assert result == expected


def test_2():
    n = 6
    c = [0, 0, 0, 1, 0, 0]
    expected = 3
    result = jumpingOnClouds(c)
    assert result == expected

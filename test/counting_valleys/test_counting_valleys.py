from src.counting_valleys.main import countingValleys


def test_1():
    n = 8
    s = "UDDDUDUU"
    expected = 1
    result = countingValleys(n, s)
    assert result == expected


def test_2():
    n = 12
    s = "DDUUDDUDUUUD"
    expected = 2
    result = countingValleys(n, s)
    assert result == expected

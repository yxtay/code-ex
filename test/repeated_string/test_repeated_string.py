from src.repeated_string.main import repeatedString


def test_1():
    s = "aba"
    n = 10
    expected = 7
    result = repeatedString(s, n)
    assert result == expected


def test_2():
    s = "a"
    n = 1000000000000
    expected = 1000000000000
    result = repeatedString(s, n)
    assert result == expected

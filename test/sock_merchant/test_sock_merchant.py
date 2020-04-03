from src.sock_merchant.main import sockMerchant


def test_1():
    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    expected = 3
    result = sockMerchant(n, ar)
    assert result == expected


def test_2():
    n = 10
    ar = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
    expected = 4
    result = sockMerchant(n, ar)
    assert result == expected

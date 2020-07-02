from bisect import bisect_right


def triplets(a, b, c):
    count = 0
    a = sorted(set(a))
    c = sorted(set(c))
    for val in set(b):
        count += bisect_right(a, val) * bisect_right(c, val)
    return count

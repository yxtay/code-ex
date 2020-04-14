from collections import Counter


def make_anagram(a, b):
    a_count = Counter(a)
    b_count = Counter(b)

    a_b = a_count - b_count
    b_a = b_count - a_count
    return sum(a_b.values()) + sum(b_a.values())

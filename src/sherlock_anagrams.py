from collections import Counter


def sherlock_anagrams(s):
    substrings = generate_sorted_substrings(s)
    anagram_counts = Counter(substrings)
    counts = sum(c * (c - 1) // 2 for c in anagram_counts.values())
    return counts


def generate_sorted_substrings(s):
    for substr in generate_substrings(s):
        yield "".join(sorted(substr))


def generate_substrings(s):
    for l in range(1, len(s) + 1):
        for substr in generate_substrings_l(s, l):
            yield substr


def generate_substrings_l(s, l):
    for i in range(len(s) - l + 1):
        yield s[i:i + l]


def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

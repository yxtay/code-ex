from collections import Counter


def matching_strings(strings, queries):
    counts = Counter(strings)
    results = [counts.get(q_str, 0) for q_str in queries]
    return results

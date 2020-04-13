from bisect import bisect_right


def climbing_leaderboard(scores, alice):
    scores = sort_unique(scores)
    ranks = []
    for a in alice:
        index = bisect_right(scores, a)
        ranks.append(len(scores) - index + 1)

    return ranks


def sort_unique(scores):
    return sorted(set(scores))

from collections import Counter


def count_triplets(arr, r):
    v2 = Counter()
    v3 = Counter()
    count = 0
    for k in arr:
        count += v3[k]
        v3[k * r] += v2[k]
        v2[k * r] += 1

    return count


def get_triplets(i, r):
    j = i * r
    k = j * r
    return i, j, k

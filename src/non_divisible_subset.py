from collections import Counter


def non_divisible_subset(k, s):
    # Write your code here
    remainders = [n % k for n in s]
    counts = Counter(remainders)

    # for divisible number, only include 1
    size = min(counts[0], 1)
    for i in range(1, k // 2 + 1):
        if i != k - i:
            size += max(counts[i], counts[k - i])

    if k % 2 == 0:
        size += 1
    return size

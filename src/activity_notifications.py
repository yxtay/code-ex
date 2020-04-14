from collections import Counter


def activity_notifications(expenditure, d):
    count = 0
    counter = Counter(expenditure[:d])
    for i in range(len(expenditure) - d):
        median = compute_median(counter)

        if expenditure[i + d] >= 2 * median:
            count += 1

        counter[expenditure[i]] -= 1
        counter[expenditure[i + d]] += 1
    return count


def compute_median(counter):
    d = sum(counter.values())
    mid = d // 2

    count = 0
    sorted_keys = sorted(counter.keys())
    for i, k in enumerate(sorted_keys):
        count += counter[k]
        if count > mid:
            if d % 2 == 1:
                return k
            else:
                if counter[k] > 1:
                    return k
                else:
                    return (k + sorted_keys[i - 1]) / 2

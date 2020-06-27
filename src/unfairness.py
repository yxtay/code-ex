def max_min(k, arr):
    arr = sorted(arr)

    min_range = 10 ** 9
    for i in range(len(arr) - k + 1):
        min_range = min(arr[i + k - 1] - arr[i], min_range)
    return min_range

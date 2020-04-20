def min_abs_diff(arr):
    arr = sorted(arr)
    min_diff = abs(arr[0] - arr[1])
    for i in range(1, len(arr) - 1):
        diff = abs(arr[i] - arr[i + 1])
        if diff < min_diff:
            min_diff = diff
    return min_diff

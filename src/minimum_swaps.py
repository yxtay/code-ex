def minimum_swaps(arr):
    arr = [v - 1 for v in arr]

    swaps = 0
    for i, _ in enumerate(arr):
        while i != arr[i]:
            arr[arr[i]], arr[i] = arr[i], arr[arr[i]]
            swaps += 1

    return swaps

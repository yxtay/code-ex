def linear_search(arr, key):
    for i in range(0, len(arr)):
        if arr[i] == key:
            return i
    return -1


def binary_search(arr, key):
    arr = sorted(arr)

    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == key:
            return middle
        else:
            if key < arr[middle]:
                right = middle - 1
            else:
                left = middle + 1
    return -1

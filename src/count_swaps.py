def count_swaps(arr):
    n = len(arr)
    count = 0

    # Traverse through all array elements
    for i in range(n - 1):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                count += 1
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        # IF no two elements were swapped
        # by inner loop, then break
        if not swapped:
            break

    print(f"Array is sorted in {count} swaps.")
    print(f"First Element: {arr[0]}")
    print(f"Last Element: {arr[-1]}")
    return count, arr[0], arr[-1]


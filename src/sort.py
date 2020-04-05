def merge_sort(arr):
    def merge(arr, left_arr, right_arr):
        i = j = k = 0

        # Copy data to temp arrays left_arr[] and right_arr[]
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        left_arr = arr[:mid]  # Dividing the array elements
        right_arr = arr[mid:]  # into 2 halves

        merge_sort(left_arr)  # Sorting the first half
        merge_sort(right_arr)  # Sorting the second half
        merge(arr, left_arr, right_arr)  # merge


def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        # IF no two elements were swapped
        # by inner loop, then break
        if not swapped:
            break


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # element present at index number i

        j = i - 1
        while j >= 0 and key < arr[j]:  # comparing elements with the next until the last item
            arr[j + 1] = arr[j]
            j -= 1  # comparing each element to the elements present to its left
        arr[j + 1] = key  # new item becomes the key


def selection_sort(arr):
    # i indicates how many items were sorted
    for i in range(len(arr) - 1):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i + 1, len(arr) - 1):
            # Update the min_index if the element at j is lower than it
            if arr[j] < arr[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        arr[i], arr[min_index] = arr[min_index], arr[i]


def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:

        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2


def quick_sort(arr):
    def partition(array, low, high):
        pivot = array[high]
        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                array[i], array[j] = array[j], array[i]

        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    def quick_sort_rec(array, low, high):

        if low < high:
            pi = partition(array, low, high)
            quick_sort_rec(array, low, pi - 1)
            quick_sort_rec(array, pi + 1, high)

    quick_sort_rec(arr, 0, len(arr) - 1)

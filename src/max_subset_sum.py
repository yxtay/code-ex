def max_subset_sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        max_array = [arr[0], max(arr[:2])]
        for i in range(2, len(arr)):
            max_array.append(max(max_array[i-2], max_array[i-1], max_array[i-2] + arr[i]))
        return max_array[-1]

def candies(n, arr):
    candies_arr = [1] * n
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            candies_arr[i] = candies_arr[i - 1] + 1

    for i in range(1, n):
        if arr[n - i - 1] > arr[n - i] and candies_arr[n - i - 1] <= candies_arr[n - i]:
            candies_arr[n - i - 1] = candies_arr[n - i] + 1

    return sum(candies_arr)

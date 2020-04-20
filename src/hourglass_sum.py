#!/bin/python3

import os


# Complete the hourglassSum function below.
def hourglassSum(arr):
    sums = []
    for i in range(4):
        for j in range(4):
            hourglass_arr = arr[i][j : j + 3] + [arr[i + 1][j + 1]] + arr[i + 2][j : j + 3]
            sums.append(sum(hourglass_arr))

    return max(sums)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + "\n")

    fptr.close()

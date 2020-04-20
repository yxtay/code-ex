#!/bin/python3

import os


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    idx = 0
    count = 0

    while idx + 1 < len(c):
        if idx + 2 < len(c) and c[idx + 2] != 1:
            idx += 2
        else:
            idx += 1
        count += 1
    return count


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + "\n")

    fptr.close()

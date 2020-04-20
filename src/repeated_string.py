#!/bin/python3

import os


# Complete the repeatedString function below.
def repeatedString(s, n):
    # count repeated
    count = 0
    for ch in s:
        if ch == "a":
            count += 1
    count *= n // len(s)

    # count remainder
    remainder = n % len(s)
    for ch in s[:remainder]:
        if ch == "a":
            count += 1
    return count


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + "\n")

    fptr.close()

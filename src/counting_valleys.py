#!/bin/python3

import os


# Complete the countingValleys function below.
def countingValleys(n, s):
    s = s[:n]

    height = 0
    is_valley = False
    count = 0

    for step in s:
        if step == "U":
            height += 1
        elif step == "D":
            height -= 1
        else:
            pass

        if height < 0:
            if not is_valley:
                count += 1
            is_valley = True
        else:
            is_valley = False

    return count


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + "\n")

    fptr.close()

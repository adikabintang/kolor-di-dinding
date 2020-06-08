# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
#!/bin/python3

import math
import os
import random
import re
import sys

def _helper_sum(arr: [int], start_row: int, start_col: int) -> int:
    #00, 01, 02, 11, 20, 21, 22
    total = 0
    total += arr[start_row][start_col] + arr[start_row][start_col + 1] + \
        arr[start_row][start_col + 2]
    start_row += 1
    total += arr[start_row][start_col + 1]
    start_row += 1
    total += arr[start_row][start_col] + arr[start_row][start_col + 1] + \
        arr[start_row][start_col + 2]
    return total

# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxi = _helper_sum(arr, 0, 0)
    for row in range(4):
        for col in range(4):
            maxi = max(maxi, _helper_sum(arr, row, col))

    return maxi

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

# https://www.hackerrank.com/challenges/count-triplets-1/
from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    left = defaultdict(int) # when a key does not exist, it returns 0 instead of exception
    right = defaultdict(int)
    for n in arr:
        right[n] += 1
    
    ctr = 0
    for n in arr:
        right[n] -= 1
        if n % r == 0:
            ctr += left[n // r] * right[n * r]
        left[n] += 1
    
    return ctr


assert countTriplets([1, 2, 2, 4], 2) == 2
assert countTriplets([1, 3, 9, 9, 27, 81], 3) == 6
assert countTriplets([1, 5, 5, 25, 125], 5) == 4
assert countTriplets([1, 4, 16, 64], 4) == 2
assert countTriplets([1, 2, 4], 2) == 1
assert countTriplets([1, 1, 1], 3) == 0
assert countTriplets([1], 3) == 0
assert countTriplets([2, 3, 4], 1) == 0
assert countTriplets([1, 1, 1], 1) == 1
assert countTriplets([1, 1, 1, 1], 1) == 4


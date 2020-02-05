# Runtime: 88 ms, faster than 64.15% of Python3 online submissions
# Memory Usage: 15.2 MB, less than 16.40% of Python3 online submissions
def singleNumber(nums: [int]):
    d = {}
    for i in nums:
        if i in d.keys():
            del d[i]
        else:
            d[i] = 1
    
    for k, v in d.items():
        if v == 1:
            return k

    return 0

a = [2,2,1]
print(singleNumber(a))

b = [4,1,2,1,2]
print(singleNumber(b))
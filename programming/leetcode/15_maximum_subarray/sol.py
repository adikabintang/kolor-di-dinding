import unittest

# def maxSubArray(self, nums: List[int]) -> int:
#         if nums == None:
#             return 0

#         max_temp = sum(nums)
#         i = 0
#         sum_temp = 0
#         while i < len(nums):
#             j = i
#             i += 1
#             sum_temp = 0
#             while j < len(nums):
#                 sum_temp += nums[j]
#                 j += 1
#                 if sum_temp > max_temp:
#                     max_temp = sum_temp

#         return max_temp

def maxSubArray(nums: [int]) -> int:
    if nums == None or len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]

    sum_array = sum(nums)
    i = 1
    temp_sum = nums[0]

    while i < len(nums) and temp_sum < sum_array:
        temp_sum += nums[i]
        i += 1

    i -= 1

    print("i: %d, nums[i]: %d" % (i, nums[i]))
    
    # find left side max
    j = i
    left_sum = 0
    max_left = nums[i]
    while j >= 0:
        left_sum += nums[j]
        j -= 1
        if left_sum > max_left:
            max_left = left_sum

    # max_left -= nums[i]

    j = i + 1
    if j < len(nums):
        right_sum = 0
        max_right = nums[j]
        while j < len(nums):
            right_sum += nums[j]
            j += 1
            if right_sum > max_right:
                max_right = right_sum
        
        if max_right + nums[i] > max_right:
            max_right += nums[i]
    else:
        max_right = 0
        if max_left + nums[i] > max_left:
            max_left += nums[i]

    # right_sum = 0
    # max_right = 0
    # while j < len(nums):
    #     right_sum += nums[j]
    #     j += 1
    #     if right_sum > max_right:
    #         max_right = right_sum
    
    return max_left + max_right

my_test = unittest.TestCase()

arr = [1, 1, 1, 1, 1, 1, 1, 1, -12, 6, 1]
my_test.assertEqual(maxSubArray(arr), 8)
arr = [-1, 0, 2, -4, -5, 5, 6, 0]
my_test.assertEqual(maxSubArray(arr), 11)
arr = [-2,1,-3,4,-1,2,1,-5,4]
my_test.assertEqual(maxSubArray(arr), 6)
arr = [1, 2, 3, 4, 5]
my_test.assertEqual(maxSubArray(arr), 15)
arr = []
my_test.assertEqual(maxSubArray(arr), 0)
arr = [6]
my_test.assertEqual(maxSubArray(arr), 6)
arr = [7, 0]
my_test.assertEqual(maxSubArray(arr), 7)
arr = [-1, -2]
my_test.assertEqual(maxSubArray(arr), -1)
arr = [-2, -1]
my_test.assertEqual(maxSubArray(arr), -1)
arr = [-2, -1, -3]
my_test.assertEqual(maxSubArray(arr), -1)

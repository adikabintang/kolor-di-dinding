def group_sum_5(start: int, nums: [int], target: int) -> bool:
    if target < 0:
        return False
    
    if start >= len(nums):
        return target == 0
    
    r = False
    if nums[start] % 5 == 0:
        if start + 1 < len(nums):
            if nums[start + 1] != 1:
                r = group_sum_5(start + 1, nums, target - nums[start])
            else:
                r = group_sum_5(start + 2, nums, target)    
    else:
        r = group_sum_5(start + 1, nums, target)
    
    if r == False:
        if start + 1 < len(nums):
            if nums[start + 1] == 1:
                r = group_sum_5(start + 2, nums, target)
            else:
                r = group_sum_5(start + 1, nums, target - nums[start])
        else:
            r = group_sum_5(start + 1, nums, target - nums[start])
    
    return r

if __name__ == "__main__":
    print(group_sum_5(0, [2, 5, 10, 4], 19))
    print(group_sum_5(0, [2, 5, 10, 4], 17))
    print(group_sum_5(0, [2, 5, 10, 4], 12))
    print(group_sum_5(0, [3, 5, 1], 9))
    print(group_sum_5(0, [3, 5, 1], 5))
    
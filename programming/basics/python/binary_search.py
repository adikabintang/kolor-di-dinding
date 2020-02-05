def bin_search(nums: [int], target: int) -> int:
    right = len(nums)
    middle_index = right // 2
    left = 0
    found_index = -1
    
    while right > left:
        if target < nums[middle_index]:
            right = middle_index
            middle_index = (right - left) // 2
        elif target > nums[middle_index]:
            left = middle_index
            middle_index = (right + left) // 2
        else:
            found_index = middle_index
            break

    return found_index
            
nums = [1, 2, 3, 4, 5, 6, 7]
for i in nums:
    print(bin_search(nums, i))

print(bin_search(nums, -7))

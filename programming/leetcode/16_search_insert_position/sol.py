def searchInsert(nums: [int], target: int) -> int:
        right = len(nums) - 1
        middle_index = len(nums) // 2
        left = 0
        found_index = 0
        
        if target < nums[left]:
            return 0
        elif target > nums[right]:
            return right + 1

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

            if middle_index - left <= 1:
                if target == nums[left]:
                    found_index = left
                elif target == nums[right]:
                    found_index = right
                elif target == nums[middle_index]:
                    found_index = middle_index
                else:
                    if target > nums[middle_index]:
                        found_index = middle_index + 1
                    elif target < nums[middle_index]:
                        found_index = middle_index
                break
            
        return found_index

a = [1,3,6,9]
b = 9
print(searchInsert(a, b))

a = [1,3]
b = 1
print(searchInsert(a, b))

a = [1,3,5,6]
b = 5
print(searchInsert(a, b))

a = [1,3,5,6]
b = 2
print(searchInsert(a, b))

a = [1,3,5,6]
b = 7
print(searchInsert(a, b))

a = [1,3,5,6]
b = 0
print(searchInsert(a, b))
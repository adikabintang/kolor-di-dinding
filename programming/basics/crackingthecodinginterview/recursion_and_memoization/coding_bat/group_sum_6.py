'''
https://codingbat.com/prob/p199368

Given an array of ints, is it possible to choose a group of some of the ints, beginning at the start index, such that the group sums to the given target? However, with the additional constraint that all 6's must be chosen. (No loops needed.)


groupSum6(0, [5, 6, 2], 8) → true
groupSum6(0, [5, 6, 2], 9) → false
groupSum6(0, [5, 6, 2], 7) → false

public boolean groupSum6(int start, int[] nums, int target) {
  if (target < 0) return false;
  
  if (start >= nums.length) return target == 0;
  
  boolean r = false;
  if (nums[start] == 6)
    r = groupSum6(start + 1, nums, target - nums[start]);
  else
    r = groupSum6(start + 1, nums, target);

  if (nums[start] != 6 && r == false)
    r = groupSum6(start + 1, nums, target - nums[start]);
  
  return r;
}
'''
def group_sum_6(start: int, nums: [int], target: int) -> bool:
    if target < 0:
        return False
    
    if start >= len(nums):
        return target == 0
    
    res = False
    if nums[start] == 6:
        res = group_sum_6(start + 1, nums, target - nums[start])
    else:
        res = group_sum_6(start + 1, nums, target)
    
    if nums[start] != 6 and res == False:
        res = group_sum_6(start + 1, nums, target - nums[start])
    
    return res

if __name__ == "__main__":
    print(group_sum_6(0, [5, 6, 2], 8))
    print(group_sum_6(0, [5, 6, 2], 9))
    print(group_sum_6(0, [5, 6, 2], 7))
    print(group_sum_6(0, [6, 6, 1], 7))

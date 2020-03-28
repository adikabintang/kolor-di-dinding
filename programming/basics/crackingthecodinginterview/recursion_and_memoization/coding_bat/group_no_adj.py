'''
https://codingbat.com/prob/p169605
Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given target with this additional constraint: If a value in the array is chosen to be in the group, the value immediately following it in the array must not be chosen. (No loops needed.)


groupNoAdj(0, [2, 5, 10, 4], 12) → true
groupNoAdj(0, [2, 5, 10, 4], 14) → false
groupNoAdj(0, [2, 5, 10, 4], 7) → false

public boolean groupNoAdj(int start, int[] nums, int target) {
  if (target < 0) return false;
  
  if (start >= nums.length) return target == 0;
  
  boolean r = groupNoAdj(start + 1, nums, target);
  if (!r)
    r = groupNoAdj(start + 2, nums, target - nums[start]);
  
  return r;
}
'''
def group_no_adj(start: int, nums: [int], target: int) -> bool:
    if target < 0:
        return False
    
    if start >= len(nums):
        return target == 0
    
    r = group_no_adj(start + 1, nums, target)
    if r == False:
        r = group_no_adj(start + 2, nums, target - nums[start])
    
    return r

if __name__ == "__main__":
    print(group_no_adj(0, [2, 5, 10, 4], 12))
    print(group_no_adj(0, [2, 5, 10, 4], 14))
    print(group_no_adj(0, [2, 5, 10, 4], 7))

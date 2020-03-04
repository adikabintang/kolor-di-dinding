'''
https://codingbat.com/prob/p108997

public boolean array6(int[] nums, int index) {
  if (index == nums.length - 1 && nums[index] != 6 || nums.length == 0) {
    return false;
  }
  
  if (nums[index] == 6) {
    return true;
  }
  
  return array6(nums, index + 1);
}
'''
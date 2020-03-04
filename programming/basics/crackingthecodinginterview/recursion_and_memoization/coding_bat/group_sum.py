'''
https://codingbat.com/prob/p145416

My step in learning:
watch this: https://www.youtube.com/watch?v=DKCbsiDBN6c
then this: https://www.youtube.com/watch?v=kyLxTdsT8ws

Then, take a look at the hint from the codingbat:
"The base case is when start>=nums.length. In that case, return true if target==0. 
Otherwise, consider the element at nums[start]. The key idea is that there are 
only 2 possibilities -- nums[start] is chosen or it is not. Make one recursive 
call to see if a solution is possible if nums[start] is chosen (subtract 
nums[start] from target in that call). Make another recursive call to see if a 
solution is possible if nums[start] is not chosen. Return true if either of the 
two recursive calls returns true."

First, draw the solution. decide the "bonding function(s)" are. The bonding functions
are applied at the beginning of the function to terminate the recursion.
'''
def group_sum(start: int, nums: [int], target: int):
    if target == 0:
        return True
    
    if start >= len(nums):
        return target == 0
    
    if group_sum(start + 1, nums, target - nums[start]):
        return True
    else:
        return group_sum(start + 1, nums, target)
    
if __name__ == "__main__":
    print(group_sum(0, [2, 4, 8], 10))
    print(group_sum(0, [2, 4, 8], 14))
    print(group_sum(0, [2, 4, 8], 9))

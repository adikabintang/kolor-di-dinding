/**
 * https://leetcode.com/problems/subarray-sum-equals-k/
 * Runtime: 448 ms, faster than 73.20% of C online submissions
 * Memory Usage: 6.4 MB, less than 100.00% of C online submissions 
 */

int subarraySum(int* nums, int numsSize, int k){
    int total = 0;
    int i = 0;
    for (i = 0; i < numsSize; i++)
    {
        int temp = k, j;
        for (j = i; j < numsSize; j++)
        {
            temp -= nums[j];
            if (temp == 0)
                total++;
        }
    }
    return total;
}

/**
 * time: 216 ms
 * memory: 7.7 MB
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int i = 0, j = 0;
    int *arr = malloc(2 * sizeof(int));
    for (i = 0; i < numsSize; i++) {
        for (j = i + 1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                arr[0] = i;
                arr[1] = j;
                *returnSize = 2;
            }
        }
    }
    
    return arr;
}


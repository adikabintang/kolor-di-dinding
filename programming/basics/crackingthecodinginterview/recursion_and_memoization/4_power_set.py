class Solution:
    def __init__(self):
        self.all_subset = []

    def get_subset(self, arr):
        self.all_subset = []
        self.__get_subset_helper(0, arr)
        return self.all_subset

    def __get_subset_helper(self, idx, arr, temp=None):
        if temp == None:
            temp = []
        
        if idx == len(arr):
            self.all_subset.append(temp)
            return
        
        holder = temp[:]
        holder.append(arr[idx])
        self.__get_subset_helper(idx + 1, arr, holder)
        self.__get_subset_helper(idx + 1, arr, temp)

def print_all(arr):
    for a in arr:
        print(a)

arr = [1, 2, 3, 4, 5]
s = Solution()
res = s.get_subset(arr)
print_all(res)

print(len(res))

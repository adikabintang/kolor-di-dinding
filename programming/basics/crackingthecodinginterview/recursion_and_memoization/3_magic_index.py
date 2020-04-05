def find_magic_idx(arr, left, right):
    res = -1
    m = (left + right) // 2
    
    if m == arr[m]:
        return m
    
    if left >= right:
        return res
    
    if m < arr[m]:
        res = find_magic_idx(arr, left, m)
        if res == -1:
            res = find_magic_idx(arr, m+1, right)
    else:
        res = find_magic_idx(arr, m+1, right)
        if res == -1:
            res = find_magic_idx(arr, left, m)
    
    return res

# arr = [-2, -1, 1, 3, 4]
# print(find_magic_idx(arr, 0, len(arr)-1))

# arr = [-1, 1, 3, 4, 5]
# print(find_magic_idx(arr, 0, len(arr)-1))

arr = [-10, 1, 1, 2, 10, 11, 12]
print(find_magic_idx(arr, 0, len(arr)-1))

def search_idx(arr: [int], n: int, l: int, r: int) -> int:
    if l > r:
        return -1
    
    m = (l + r) // 2
    if arr[m] == n:
        return m
    
    if arr[l] < arr[m]: # left side is normal
        if n < arr[m] and n >= arr[l]:
            return search_idx(arr, n, l, m-1)
        else:
            return search_idx(arr, n, m+1, r)
    elif arr[m] < arr[r]: # right side is normal
        if n > arr[m] and n <= arr[r]:
            return search_idx(arr, n, m+1, r)
        else:
            return search_idx(arr, n, l, m-1)
    elif arr[l] == arr[m]: # left or right side is repeats
        if arr[m] != arr[r]:
            return search_idx(arr, n, m+1, r)
        else: # search for the bottom halves
            res = search_idx(arr, n, l, m-1)
            if res == -1: # search right
                return search_idx(arr, n, m+1, r)
            else:
                return res
    
    return -1

arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
print(search_idx(arr, 5, 0, len(arr) - 1))
print(search_idx(arr, 20, 0, len(arr) - 1))

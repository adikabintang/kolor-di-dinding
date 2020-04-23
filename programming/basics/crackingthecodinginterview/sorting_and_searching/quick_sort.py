def partition(arr, left, right):
    pivot = arr[(left + right) // 2]

    while left <= right:
        while arr[left] < pivot:
            left += 1
        
        while arr[right] > pivot:
            right -= 1
        
        if left <= right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left += 1
            right -= 1
    
    return left
    
def quick_sort(arr, left, right):
    index = partition(arr, left, right)
    if left < index - 1:
        quick_sort(arr, left, index - 1)
    
    if index < right:
        quick_sort(arr, index, right)

#arr = [i for i in range(4, 0, -1)]
arr = [10, 9, 2, 12, 1, 11]
print(arr)
quick_sort(arr, 0, len(arr) - 1)
print(arr)
# print("----")
# arr = [i for i in range(4, 0, -1)]
# print(arr)
# quick_sort(arr, 0, len(arr) - 1)
# arr = [i for i in range(1, 5)]
# print(arr)
# print("----")
# arr = [i for i in range(5, 0, -1)]
# print(arr)
# quick_sort(arr, 0, len(arr) - 1)
# print(arr)
# print("----")
# arr = [4, 1, 2, 5, 7, 3, 5, 7, 1, 0, 99]
# print(arr)
# quick_sort(arr, 0, len(arr) - 1)
# print(arr)
# print("----")
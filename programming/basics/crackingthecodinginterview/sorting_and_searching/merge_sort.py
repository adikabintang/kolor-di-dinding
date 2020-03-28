def dummy(arr: [int]):
    for i in range(0, len(arr)):
        arr[i] += 1

def merge_conquer(arr, left_a, right_a, left_b, right_b):
    i = left_b
    j = left_a
    helper_array = []
    while j <= right_a and i <= right_b:
        if arr[i] < arr[j]:
            helper_array.append(arr[i])
            i += 1
        elif arr[i] > arr[j]:
            helper_array.append(arr[j])
            j += 1
        else:
            helper_array.append(arr[j])
            helper_array.append(arr[i])
            j += 1
            i += 1
    
    while i <= right_b:
        helper_array.append(arr[i])
        i += 1
    
    while j <= right_a:
        helper_array.append(arr[j])
        j += 1
    
    #print(helper_array)
    i = left_a
    for n in helper_array:
        arr[i] = n
        i += 1
    #print(arr)

# also the divide
def merge_sort(arr, left_index, right_index):
    if left_index != right_index:
        middle = (left_index + right_index) // 2
        merge_sort(arr, left_index, middle)
        merge_sort(arr, middle + 1, right_index)
        merge_conquer(arr, left_index, middle, middle + 1, right_index)

arr = [i for i in range(1, 5)]
print(arr)
merge_sort(arr, 0, len(arr) - 1)
print(arr)
print("----")
arr = [i for i in range(4, 0, -1)]
print(arr)
merge_sort(arr, 0, len(arr) - 1)
print(arr)
print("----")
arr = [i for i in range(5, 0, -1)]
print(arr)
merge_sort(arr, 0, len(arr) - 1)
print(arr)
print("----")
arr = [4, 1, 2, 5, 7, 3, 5, 7, 1, 0, 99]
print(arr)
merge_sort(arr, 0, len(arr) - 1)
print(arr)
print("----")
# print(arr)
# a = [2, 3, 4, 1, 2, 3]
# merge_conquer(a, 0, 2, 3, 5)
# a = [1, 2, 3, 4, 5, 6]
# merge_conquer(a, 0, 2, 3, 5)
# a = [4, 5, 6, 1, 2, 3]
# merge_conquer(a, 0, 2, 3, 5)
# dummy(arr)
# print(arr)
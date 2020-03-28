def search_index(arr: [int], n: int) -> int:
    return binary_search(arr, n, 0, len(arr) - 1)

def binary_search(arr, n, left, right):
    if left == right:
        return left if arr[left] == n else -1

    if left < right:
        m = (left + right) // 2
        if n == arr[m]:
            return m
        elif n > arr[m]:
            return binary_search(arr, n, m+1, right)
        else:
            return binary_search(arr, n, 0, m)
    
    return -1

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    for i in range (-1, 10):
        print("%d: %d" % (i, search_index(arr, i)))

def print_image(arr):
    n = len(arr)
    for i in range(0, n):
        print(arr[i])

def rotate(arr):
    n = len(arr) - 1
    l = 0
    right = n
    bottom = n
    top = 0
    x = 0

    while x < len(arr) - 1:
        j = n
        for i in range(x, n):
            tmp = arr[top][i]
            arr[top][i] = arr[j][l]
            arr[j][l] = arr[bottom][j]
            arr[bottom][j] = arr[i][right]
            arr[i][right] = tmp
            j -= 1
        
        x += 1
        n -= 1
        right -= 1
        top += 1
        bottom -= 1
        l += 1

img = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print_image(img)
rotate(img)
print("----")
print_image(img)

print("=======")
img = [[1, 2, 3], [5, 6, 7], [9, 10, 11]]
print_image(img)
rotate(img)
print("----")
print_image(img)
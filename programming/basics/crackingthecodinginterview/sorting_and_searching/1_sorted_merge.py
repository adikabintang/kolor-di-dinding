def sorted_merge(a: [int], b: [int], i, j):
    k = i + j + 1

    while j >= 0:
        if i >= 0 and a[i] > b[j]:
            a[k] = a[i]
            i -= 1
        else:
            a[k] = b[j]
            j -= 1
        k -= 1

if __name__ == "__main__":
    a = [7, 8, 9, -1, -1, -1]
    b = [1, 2, 3]

    sorted_merge(a, b, 2, 2)
    print(a)

    a = [7, 9, 12, -1, -1, -1]
    b = [4, 8, 17]

    sorted_merge(a, b, 2, 2)
    print(a)

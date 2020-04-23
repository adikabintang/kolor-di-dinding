import time

def countPrimes(n: int) -> int:
    arr = [i for i in range(2, n)]
    index = 0
    while True:
        if arr[index] ** 2 > n:
            break

        i = arr.index(arr[index] ** 2)
        for j in arr[i:]:
            if j % arr[index] == 0:
                arr.remove(j)
        
        if arr[index] * arr[index + 1] > n:
            break
        index += 1
    
    print(arr)
    return len(arr)

print(countPrimes(100))
#countPrimes(7) 452

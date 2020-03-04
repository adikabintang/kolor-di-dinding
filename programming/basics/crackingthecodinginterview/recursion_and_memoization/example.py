import time

def fib(n: int):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)

cache_1 = [None] * 10

def fib_memoized_1(n: int):
    if n == 0 or n == 1:
            return n
    else:
        if n < len(cache_1) and cache_1[n]:
            return cache_1[n]
        
        val = fib_memoized_1(n - 2) + fib_memoized_1(n - 1)
        if n < len(cache_1):
            cache_1[n] = val

        return val

for i in range(10):
    print(fib_memoized_1(i))

t0 = int(round(time.time() * 1000))
print(fib_memoized_1(30))
t1 = int(round(time.time() * 1000))
print("time: %d" % (t1 - t0))

# without cache: 303, 288, 280
# with cache: 0
# with caching the first 10: 17
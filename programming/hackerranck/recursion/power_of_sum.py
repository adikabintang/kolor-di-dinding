# https://www.hackerrank.com/challenges/the-power-sum/problem

def power_sum(x, n, i=None):
    if x < 0:
        return 0
    
    if i is None:
        i = int(x ** (1/n))
    
    if i == 0:
        return 1 if x == 0 else 0
    
    if x == 0:
        return 1
    
    r = power_sum(x - int(i ** n), n, i - 1)
    r += power_sum(x, n, i - 1)
    return r

print(power_sum(13, 2))
print(power_sum(10, 2))
print(power_sum(100, 2))

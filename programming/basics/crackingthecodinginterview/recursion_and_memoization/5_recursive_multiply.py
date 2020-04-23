def recursive_mult(p: int, q: int) -> int:
    if p == 0 or q == 0:
        return 0
    
    if q == 1:
        return p
    
    if q > p:
        temp = p
        p = q
        q = temp
    
    return p + recursive_mult(p, q - 1)

print(recursive_mult(2, 3))
print(recursive_mult(1, 8))
print(recursive_mult(8, 1))

print(recursive_mult(8, 7))

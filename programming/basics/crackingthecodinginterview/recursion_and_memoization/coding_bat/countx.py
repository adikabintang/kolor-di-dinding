'''
https://codingbat.com/prob/p170371
Given a string, compute recursively (no loops) the number of lowercase 'x' chars 
in the string.


countX("xxhixx") → 4
countX("xhixhix") → 3
countX("hi") → 0
'''
def count_x(s: str):
    if len(s) == 0:
        return 0
    
    total = 0
    if s[0] == 'x':
        total = 1
    
    return total + count_x(s[1:])

print(count_x("xhixhix"))

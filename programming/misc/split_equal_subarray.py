# Given an array of numbers(ex [3 2 5]), find if its possible to split it into 
# 2 parts with equal sum without reordering (ex [3 2 ] and [5] ) and 
# false if not possible!

# re-implement tail with bash????

# mirror of BT: https://www.careercup.com/question?id=12177758
# Write a program to find the mirror image of a binary tree?

# if a tree is like

# 01
# 02 03
# 04 05 06 07

# The mirror will be like

# 01
# 03 02
# 07 06 05 04

# Write a function to sort a list of integers that looks like this [5,2,0,3,0,1,6,0] -> [1,2,3,5,6,0,0,0] in the most efficient way.

# Provided list of IPs and ports check if the host is accessible on that particular port using python and bash. (done)

# https://leetcode.com/articles/design-in-memory-file-system/

# Given that: '1' mapped to--> 'a', '2' -->'b', '3'--> 'c'...like wise... '26'-->'z'. 
# Output should be in the following pattern : 
# Ex.1) if we input f="111", the output should be: aaa, ak, ka //(111)->aaa, (1, 11)->ak, (11,1)->ka 
# Ex. 2) f="131" output: aca, ma //(131)->aca, (13,1)->ma 
# Ex. 3) f="101", output: ja //(10,1)->ja

# arrange vowel and then consonant 

def is_splittable(arr: [int]) -> bool:
    total = sum(arr)
    left = 0
    right = 0

    for i in range(len(arr)):
        right += arr[i]
        left = total - right
        if left == right:
            return True
    
    return False

assert is_splittable([1, 2, 1, 2]) == True
assert is_splittable([1, 2, 3, 2]) == False
assert is_splittable([7, 1, 1, 2, 5]) == True

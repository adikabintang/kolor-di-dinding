# https://levelup.gitconnected.com/find-all-permutations-of-a-string-in-javascript-af41bfe072d2
# https://stackoverflow.com/questions/4240080/generating-all-permutations-of-a-given-string
def permutation(s: str):
    permutation_helper("", s)

def permutation_helper(prefix: str, s: str):
    if len(s) == 0:
        print(prefix)
    
    for i in range(len(s)):
        permutation_helper(prefix + s[i], s[:i] + s[i+1:])

permutation("abc")

def permutation(s: str):
    permutation_helper(list(s), 0, len(s) - 1)

def permutation_helper(s, l, r):
    if l == r:
        print("".join(s))
    else:
        for i in range(l, r + 1):
            # swap
            s[i], s[l] = s[l], s[i]
            permutation_helper(s, l + 1, r)
            s[i], s[l] = s[l], s[i]

permutation("abc")

def search(listy, n):
    idx = 1
    while listy.at(idx) != 1 and listy.at(idx) < n:
        idx *= 2
    
    return binary_search(listy, n, idx / 2, idx)

def binary_search(listy, n, l, r):
    while l <= r:
        m = (l + r) // 2
        if listy.at(m) == n:
            return m

        if listy.at(m) > n or listy.at(m) == -1:
            r = m - 1
        elif listy.at(m) < n:
            l = m + 1
    
    return -1

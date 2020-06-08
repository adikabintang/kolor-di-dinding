def minimumBribes(q):
    bribes = 0
    i = len(q) - 1
    while i >= 2:
        if (q[i] - 1) != i:
            chaos = True
            j = i
            while j >= i - 2:
                if q[j] == i + 1:
                    chaos = False
                    break
                j -= 1
            bribes += i - j
            if chaos:
                print("Too chaotic")
                return
            while j < i:
                temp = q[j]
                q[j] = q[j+1]
                q[j+1] = temp
                j += 1
        i -= 1
    
    if (q[i] - 1) != i:
        bribes += 1

    print(bribes)

minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]) # 7
minimumBribes([2, 1, 5, 3, 4]) #r: 3; 112
minimumBribes([2, 5, 1, 3, 4])
minimumBribes([5, 1, 2, 3, 7, 8, 6, 4])

# approach: check one by one the correct position and how far they bribe
# then SHIFT back to the correct position
# 1 2 5 3 7 8 6 4 # 8: 2
# 1 2 5 3 7 6 4 8 # 7: 2
# 1 2 5 3 6 4 7 8 # 6: 1
# 1 2 5 3 4 6 7 8 # 5: 2
# 1 2 3 4 5 6 7 8 # 4: 0


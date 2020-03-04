import time

class TripleStep:
    def __init__(self):
        self.memo = None

    def num_ways(self, n):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        return self.num_ways(n-1) + self.num_ways(n-2) + self.num_ways(n-3)
    
    def num_ways_with_memo(self, n):
        if self.memo is None:
            self.memo = [0] * (n + 1)
        
        if n < 0:
            return 0
        elif n == 0:
            return 1
        
        if self.memo[n] == 0:
            self.memo[n] = self.num_ways_with_memo(n-1) + \
                self.num_ways_with_memo(n-2) + \
                    self.num_ways_with_memo(n-3)

        return self.memo[n] 

if __name__ == "__main__":
    t = TripleStep()
    t0 = int(round(time.time() * 1000))
    print(t.num_ways(30))
    t1 = int(round(time.time() * 1000))
    print("no memoization: %d ms" % (t1 - t0))
    t0 = int(round(time.time() * 1000))
    print(t.num_ways_with_memo(30))
    t1 = int(round(time.time() * 1000))
    print("memoization: %d ms" % (t1 - t0))

    print()
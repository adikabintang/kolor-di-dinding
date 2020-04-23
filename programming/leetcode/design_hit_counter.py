# https://leetcode.com/problems/design-hit-counter/
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hit_ctr = {}
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp in self.hit_ctr:
            self.hit_ctr[timestamp] += 1
        else:
            self.hit_ctr[timestamp] = 1
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        start = timestamp - (5 * 60)
        counter = 0
        for t, c in self.hit_ctr.items():
            if t > start and t <= timestamp:
                counter += c
        return counter
        
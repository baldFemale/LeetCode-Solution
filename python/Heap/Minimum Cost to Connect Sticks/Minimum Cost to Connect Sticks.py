import heapq

class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        heapq.heapify(sticks)
        res = 0
        while len(sticks)>1:
            p1 = heapq.heappop(sticks)
            p2 = heapq.heappop(sticks)
            res+=p1+p2
            heapq.heappush(sticks,p1+p2)
        return res

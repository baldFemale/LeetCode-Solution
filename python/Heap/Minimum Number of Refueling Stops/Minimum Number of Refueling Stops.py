import heapq


class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        stations.append([target, float("inf")])
        heap = []
        heapq.heapify(heap)

        res = 0
        pre = 0
        tank = startFuel
        for location, capacity in stations:
            tank -= (location - pre)
            while tank < 0 and heap:
                v = heapq.heappop(heap)
                tank -= v
                res += 1
            if tank < 0:
                return -1
            heapq.heappush(heap, -capacity)
            pre = location
        return res

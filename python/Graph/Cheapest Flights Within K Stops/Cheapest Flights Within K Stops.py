import heapq
from collections import defaultdict


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """

        graph = defaultdict(dict)
        for f in flights:
            graph[f[0]][f[1]] = f[2]

        heap = [(0, src, K + 1)]
        while heap:
            dis, cur, k = heapq.heappop(heap)
            if cur == dst:
                return dis
            if k > 0:
                for i in graph[cur]:
                    heapq.heappush(heap, (dis + graph[cur][i], i, k - 1))
        return -1
import heapq


class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        ratio = [(1.0 * wage[i] / quality[i], quality[i], wage[i]) for i in range(len(quality))]
        ratio.sort()

        res = float("inf")
        s = 0
        heap = []
        for r, q, w in ratio:
            heapq.heappush(heap, -q)
            s += q

            if len(heap) > K:
                s += heapq.heappop(heap)
            if len(heap) == K:
                res = min(res, r * s)

        return res




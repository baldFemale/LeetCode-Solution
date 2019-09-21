import heapq


class Solution(object):
    def minBuildTime(self, blocks, split):
        """
        :type blocks: List[int]
        :type split: int
        :rtype: int
        """

        heapq.heapify(blocks)

        while len(blocks) > 1:
            node1 = heapq.heappop(blocks)
            node2 = heapq.heappop(blocks)
            heapq.heappush(blocks, max(node1, node2) + split)

        return blocks[0]

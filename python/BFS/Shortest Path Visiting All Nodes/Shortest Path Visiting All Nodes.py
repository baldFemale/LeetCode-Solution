from collections import defaultdict


class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        N = len(graph)
        queue = [(i, 1 << i) for i in range(N)]
        dist = defaultdict(lambda: N * N)
        for i in range(N):
            dist[(i, 1 << i)] = 0

        while queue:
            node, path = queue.pop(0)
            d = dist[(node, path)]
            if path == 2 ** N - 1:
                return d
            for nex in graph[node]:
                temp = (1 << nex) | path
                if dist[(nex, temp)] > d + 1:
                    dist[(nex, temp)] = d + 1
                    queue.append((nex, temp))

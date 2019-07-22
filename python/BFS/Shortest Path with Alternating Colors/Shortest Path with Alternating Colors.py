from collections import defaultdict


class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        """
        :type n: int
        :type red_edges: List[List[int]]
        :type blue_edges: List[List[int]]
        :rtype: List[int]
        """
        redGraph = defaultdict(list)
        blueGraph = defaultdict(list)

        for i, j in red_edges:
            redGraph[i].append(j)
        print(redGraph)
        for i, j in blue_edges:
            blueGraph[i].append(j)

        red_seen = set()
        blue_seen = set()
        queue = []
        queue.append((0, 0))
        queue.append((0, 1))
        red_seen.add(0)
        blue_seen.add(0)

        step = 0
        res = [float("inf") for i in range(n)]

        while queue:
            size = len(queue)
            while size > 0:
                node, color = queue.pop(0)
                if color == 0:
                    for nex in blueGraph[node]:
                        if nex not in blue_seen:
                            queue.append((nex, 1))
                            blue_seen.add(nex)
                            res[nex] = min(res[nex], step + 1)
                else:
                    for nex in redGraph[node]:
                        if nex not in red_seen:
                            queue.append((nex, 0))
                            red_seen.add(nex)
                            res[nex] = min(res[nex], step + 1)
                size -= 1
            step += 1
        res[0] = 0
        return [i if i != float("inf") else -1 for i in res]


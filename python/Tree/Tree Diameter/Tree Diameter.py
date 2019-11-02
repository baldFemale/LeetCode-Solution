from collections import defaultdict


class Solution(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        self.res = 0

        graph = defaultdict(list)

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        def bfs(node, parent):
            print(node, parent)
            if len(graph[node]) == 1:
                if graph[node][0] == parent:
                    if 1 > self.res:
                        self.res = 1
                    return 1
                else:
                    t = 1 + bfs(graph[node][0], node)
                    if t > self.res:
                        self.res = t
                    return t
            else:
                res = []
                for i in graph[node]:
                    if i == parent:
                        continue
                    else:
                        res.append(bfs(i, node))
                print(res)
                if len(res) == 1:
                    if res[0] > self.res:
                        self.res = res[0] + 1
                    return res[0] + 1
                else:
                    res.sort()
                    if res[-1] + res[-2] > self.res:
                        self.res = res[-1] + res[-2]
                    return 1 + res[-1]

        bfs(0, None)
        return self.res
from collections import defaultdict


class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:

        child = defaultdict(list)

        for i, j in enumerate(parent):
            child[j].append(i)

        s = {}

        def dp(node):
            if len(child[node]) == 0:
                s[node] = value[node]
                return s[node]
            else:
                if node == -1:
                    t = 0
                else:
                    t = value[node]
                for i in child[node]:
                    t += dp(i)
                s[node] = t
                return s[node]

        dp(-1)

        s[-1] = 1

        print(s)

        queue = [-1]
        res = 0

        while queue:
            for i in range(len(queue)):
                node = queue.pop()
                if s[node] == 0:
                    pass
                else:
                    res += 1
                    for j in child[node]:
                        queue.append(j)
        return res - 1
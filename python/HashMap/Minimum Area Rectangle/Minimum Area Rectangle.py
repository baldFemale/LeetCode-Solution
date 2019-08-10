from collections import defaultdict


class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        p = defaultdict(list)
        for x, y in points:
            p[x].append(y)
        res = float("inf")

        latex = {}
        for x in sorted(p):
            p[x].sort()
            for i in range(len(p[x])):
                for j in range(i):
                    y1, y2 = p[x][j], p[x][i]
                    if (y1, y2) in latex:
                        res = min(res, (y2 - y1) * (x - latex[(y1, y2)]))
                    latex[(y1, y2)] = x
        return res if res != float("inf") else 0

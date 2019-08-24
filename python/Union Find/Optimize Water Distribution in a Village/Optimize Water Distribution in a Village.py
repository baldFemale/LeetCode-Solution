class DSU:
    def __init__(self):
        self.parents = range(10001)
        self.rank = [0 for i in range(10001)]

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.rank[xr] < self.rank[yr]:
            self.parents[xr] = yr
        elif self.rank[xr] > self.rank[yr]:
            self.parents[yr] = xr
        else:
            self.parents[xr] = yr
            self.rank[yr] += 1
        return True


class Solution(object):
    def minCostToSupplyWater(self, n, wells, pipes):
        """
        :type n: int
        :type wells: List[int]
        :type pipes: List[List[int]]
        :rtype: int
        """
        dsu = DSU()
        dic = {}
        for i, w in enumerate(wells):
            dic[(0, i + 1)] = w
        for i, j, p in pipes:
            dic[(i, j)] = p

        keys = sorted(dic.keys(), key=lambda x: dic[x])
        res = 0
        for i, j in keys:
            if dsu.find(i) == dsu.find(j):
                continue
            else:
                dsu.union(i, j)
                res += dic[(i, j)]
        return res

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
    def minimumCost(self, N, conections):
        """
        :type N: int
        :type conections: List[List[int]]
        :rtype: int
        """
        conections.sort(key=lambda x: x[-1])

        count = N
        res = 0
        dsu = DSU()
        for i, j, v in conections:
            if dsu.union(i - 1, j - 1):
                count -= 1
                res += v
        if count == 1:
            return res
        else:
            return -1

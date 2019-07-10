class DSU:
    def __init__(self):
        self.parents = range(20001)
        self.rank = [0] * 20001

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return
        else:
            if self.rank[xr] < self.rank[yr]:
                self.parents[xr] = yr
            elif self.rank[xr] > self.rank[xr]:
                self.parents[yr] = xr
            else:
                self.parents[yr] = xr
                self.rank[xr] += 1
            return


class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        dsu = DSU()
        for x, y in stones:
            dsu.union(x, y + 10000)

        return len(stones) - len(set([dsu.find(x) for x, y in stones]))

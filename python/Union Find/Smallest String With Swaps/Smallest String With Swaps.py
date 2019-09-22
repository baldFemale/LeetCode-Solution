from collections import defaultdict


class DSU:
    def __init__(self):
        self.parents = range(100001)
        self.rank = [0 for i in range(100001)]

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
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """

        dsu = DSU()
        for pair in pairs:
            dsu.union(pair[0], pair[1])

        dic = defaultdict(list)

        for i, j in enumerate(s):
            dic[dsu.find(i)].append(j)

        for key in dic.keys():
            dic[key].sort()
        # print(dic)
        res = ""

        for i in range(len(s)):
            res += dic[dsu.find(i)].pop(0)
        return res

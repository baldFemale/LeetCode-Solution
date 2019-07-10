from collections import defaultdict


class DSU:
    def __init__(self):
        self.parents = range(10001)
        self.rank = [0]*10001

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return
        if self.rank[xr] < self.rank[yr]:
            self.parents[xr] = yr
        elif self.rank[xr] > self.rank[yr]:
            self.parents[yr] = xr
        else:
            self.parents[xr] = yr
            self.rank[yr] += 1
        return


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        dsu = DSU()
        em_to_name = {}
        em_to_id = {}
        i = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em_to_name[email] = name
                if email not in em_to_id:
                    em_to_id[email] = i
                    i += 1
                dsu.union(em_to_id[acc[1]], em_to_id[email])

        ans = defaultdict(list)
        for email in em_to_name:
            ans[dsu.find(em_to_id[email])].append(email)

        res = []
        for k in ans:
            temp = []
            v = ans[k]
            temp.append(em_to_name[v[0]])
            temp += (sorted(v))
            res.append(temp)
        return res

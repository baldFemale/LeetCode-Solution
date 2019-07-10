class DSU:
    def __init__(self):
        self.parents = range(10001)
        self.rank = [0 for i in range(10001)]

    def find(self, x):
        if self.parents[x]!=x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        xr,yr = self.find(x),self.find(y)
        if xr == yr:
            return False
        if self.rank[xr]<self.rank[yr]:
            self.parents[xr] = yr
        elif self.rank[xr]>self.rank[yr]:
            self.parents[yr] = xr
        else:
            self.parents[xr] = yr
            self.rank[yr] += 1
        return True

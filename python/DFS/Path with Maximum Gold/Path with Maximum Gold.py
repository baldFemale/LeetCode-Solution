class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        self.res = -float("inf")

        def dfs(i, j, seen, s):
            seen.add((i, j))
            self.res = max(self.res, s)
            for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                if 0 <= i + x < m and 0 <= j + y < n:
                    if grid[x + i][j + y] != 0 and (x + i, j + y) not in seen:
                        temp = set(seen)
                        dfs(i + x, j + y, temp, s + grid[x + i][j + y])

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    dfs(i, j, set(), grid[i][j])
        return self.res

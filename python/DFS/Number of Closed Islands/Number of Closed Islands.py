class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        self.seen = set()

        def dfs(i, j):
            if i == -1 or i == m:
                return True
            if j == -1 or j == n:
                return True

            self.seen.add((i, j))

            if grid[i][j] == 1:
                return False

            tag = False
            for x, y in [[1, 0], [0, -1], [-1, 0], [0, 1]]:
                if (i + x, j + y) not in self.seen:
                    t = dfs(i + x, j + y)
                    tag = tag or t
            return tag

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i, j) not in self.seen:
                    t = dfs(i, j)
                    if not t:
                        res += 1

        return res
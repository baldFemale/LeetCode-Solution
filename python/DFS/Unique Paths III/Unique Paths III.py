class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        empty = 1
        self.res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    empty += 1
                elif grid[i][j] == 1:
                    start_x, start_y = i, j
                elif grid[i][j] == 2:
                    end_x, end_y = i, j

        def dfs(x, y, empty):
            if not (0 <= x < m and 0 <= y < n):
                return
            if grid[x][y] < 0:
                return
            if (x, y) == (end_x, end_y):
                if empty == 0:
                    self.res += 1
                return
            grid[x][y] = -2
            dfs(x + 1, y, empty - 1)
            dfs(x - 1, y, empty - 1)
            dfs(x, y + 1, empty - 1)
            dfs(x, y - 1, empty - 1)
            grid[x][y] = 0

        dfs(start_x, start_y, empty)
        return self.res

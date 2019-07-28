class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        top = [i for i in grid]
        left = [[i[j] for j in range(len(grid[0]))] for i in grid]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    if i:
                        top[i][j] = top[i - 1][j] + 1
                    if j:
                        left[i][j] = left[i][j - 1] + 1

        for r in range(min(len(grid), len(grid[0])), 0, -1):
            for i in range(len(grid) + 1 - r):
                for j in range(len(grid[0]) + 1 - r):
                    if min(top[i + r - 1][j], top[i + r - 1][j + r - 1], left[i][j + r - 1],
                           left[i + r - 1][j + r - 1]) >= r:
                        return r ** 2
        return 0

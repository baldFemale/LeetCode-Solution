from collections import deque


class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        queue = deque()
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    queue.append((i, j))
        if len(queue) == 0 or len(queue) == N * N:
            return -1
        level = 0
        while queue:
            size = len(queue)
            while size:
                size -= 1
                x, y = queue.popleft()
                for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    if 0 <= x + dx < N and 0 <= y + dy < N and grid[x + dx][y + dy] == 0:
                        queue.append((x + dx, y + dy))
                        grid[x + dx][y + dy] = 1
            level += 1
        return level - 1

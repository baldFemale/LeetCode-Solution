class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        matrix = [[0 for i in range(m)] for j in range(n)]

        for i, j in indices:
            for k in range(m):
                matrix[i][k] += 1
            for k in range(n):
                matrix[k][j] += 1

        res = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] % 2 == 1:
                    res += 1
        return res
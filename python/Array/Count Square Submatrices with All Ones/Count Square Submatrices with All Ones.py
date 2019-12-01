class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        m = len(matrix)
        n = len(matrix[0])

        va = set([i ** 2 for i in range(1, 300)])

        for j in range(m):
            for i in range(1, n):
                matrix[j][i] += matrix[j][i - 1]

        for i in range(1, m):
            for j in range(n):
                matrix[i][j] += matrix[i - 1][j]

        res = 0
        for i in range(m):
            for j in range(n):
                k = 0
                while i - k >= 0 and j - k >= 0:
                    if i - k > 0 and j - k > 0:
                        t = matrix[i][j] + matrix[i - k - 1][j - k - 1] - matrix[i - k - 1][j] - matrix[i][j - k - 1]
                    elif i - k == 0 and j - k == 0:
                        t = matrix[i][j]
                    elif i - k == 0:
                        t = matrix[i][j] - matrix[i][j - k - 1]
                    else:
                        t = matrix[i][j] - matrix[i - k - 1][j]
                    if t == (k + 1) ** 2:
                        res += 1
                        k += 1
                    else:
                        break
        return res


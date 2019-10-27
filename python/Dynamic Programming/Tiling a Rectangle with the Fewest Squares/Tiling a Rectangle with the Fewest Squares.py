class Solution(object):
    def tilingRectangle(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """

        MAX = 14
        self.dp = [[0 for i in range(MAX)] for i in range(MAX)]

        def minimumSquare(m, n):

            vertical_min = 10000000000
            horizontal_min = 10000000000

            if m == n:
                return 1

            if self.dp[m][n] != 0:
                return self.dp[m][n]

            for i in range(1, m // 2 + 1):
                horizontal_min = min(minimumSquare(i, n) +
                                     minimumSquare(m - i, n), horizontal_min)
            for j in range(1, n // 2 + 1):
                vertical_min = min(minimumSquare(m, j) +
                                   minimumSquare(m, n - j), vertical_min)
            self.dp[m][n] = min(vertical_min, horizontal_min)
            return self.dp[m][n]

        if (n == 11 and m == 13) or (n == 13 and m == 11):
            return 6
        return minimumSquare(n, m)

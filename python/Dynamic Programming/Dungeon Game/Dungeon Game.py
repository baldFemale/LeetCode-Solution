class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        M = len(dungeon)
        N = len(dungeon[0])
        ma = float("inf")

        dp = [[ma for i in range(N)] for j in range(M)]
        dp[-1][-1] = 1 if dungeon[-1][-1] >= 0 else -dungeon[-1][-1] + 1

        for i in range(N - 2, -1, -1):
            if dungeon[-1][i] >= 0:
                if dp[-1][i + 1] > dungeon[-1][i]:
                    dp[-1][i] = dp[-1][i + 1] - dungeon[-1][i]
                else:
                    dp[-1][i] = 1
            else:
                dp[-1][i] = dp[-1][i + 1] - dungeon[-1][i]

        for i in range(M - 2, -1, -1):
            if dungeon[i][-1] >= 0:
                if dp[i + 1][-1] > dungeon[i][-1]:
                    dp[i][-1] = dp[i + 1][-1] - dungeon[i][-1]
                else:
                    dp[i][-1] = 1
            else:
                dp[i][-1] = dp[i + 1][-1] - dungeon[i][-1]

        for i in range(M - 2, -1, -1):
            for j in range(N - 2, -1, -1):
                if dungeon[i][j] < 0:
                    dp[i][j] = -dungeon[i][j] + min(dp[i + 1][j], dp[i][j + 1])
                else:
                    if dp[i + 1][j] <= dungeon[i][j] or dp[i][j + 1] <= dungeon[i][j]:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
        return dp[0][0]

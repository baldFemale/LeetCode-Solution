class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [[0 for i in range(len(s) + 1)] for j in range(len(t) + 1)]

        for i in range(len(dp[0])):
            dp[0][i] = 1

        for i in range(len(dp) - 1):
            for j in range(len(dp[0]) - 1):
                if s[j] == t[i]:
                    dp[i + 1][j + 1] = dp[i][j] + dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j]
        return dp[-1][-1]

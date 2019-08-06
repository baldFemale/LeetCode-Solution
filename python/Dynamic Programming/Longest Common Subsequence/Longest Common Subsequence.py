class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n = len(text1)
        m = len(text2)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if text2[i] == text1[j]:
                    dp[i + 1][j + 1] = max(dp[i][j] + 1, dp[i][j + 1], dp[i][j + 1])
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        print(dp)
        return dp[-1][-1]

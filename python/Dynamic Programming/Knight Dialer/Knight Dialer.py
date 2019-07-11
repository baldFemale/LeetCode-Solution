class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """

        dp = [1] * 10
        mod = 10 ** 9 + 7

        for i in range(1, N):
            temp = list(dp)
            dp[0] = (temp[4] + temp[6]) % mod
            dp[1] = (temp[6] + temp[8]) % mod
            dp[2] = (temp[7] + temp[9]) % mod
            dp[3] = (temp[4] + temp[8]) % mod
            dp[4] = (temp[3] + temp[9] + temp[0]) % mod
            dp[6] = (temp[1] + temp[7] + temp[0]) % mod
            dp[7] = (temp[2] + temp[6]) % mod
            dp[8] = (temp[1] + temp[3]) % mod
            dp[9] = (temp[2] + temp[4]) % mod
        return (sum(dp) - dp[5]) % mod if N > 1 else 10
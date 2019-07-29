class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)

        if k >= n // 2:
            pre = prices[0]
            res = 0
            for p in prices[1:]:
                if p >= pre:
                    res += p - pre
                pre = p
            return res

        else:
            dp = [[0 for i in range(n)] for j in range(k + 1)]
            for i in range(1, k + 1):
                temp = dp[i - 1][0] - prices[0]
                for j in range(1, n):
                    dp[i][j] = max(dp[i][j - 1], prices[j] + temp)
                    temp = max(temp, dp[i - 1][j] - prices[j])
            return dp[-1][-1]

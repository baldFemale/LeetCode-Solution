class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        dp = {0: 0}

        for r in rods:
            for d, s in dp.items():
                dp[d + r] = max(dp.get(d + r, 0), s)
                if d >= r:
                    dp[d - r] = max(dp.get(d - r, 0), s + r)
                else:
                    dp[r - d] = max(dp.get(r - d, 0), s + d)
        return dp[0]

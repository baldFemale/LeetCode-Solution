class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pre = float("inf")
        res = 0

        for p in prices:
            if p > pre:
                res += p - pre
            pre = p

        return res

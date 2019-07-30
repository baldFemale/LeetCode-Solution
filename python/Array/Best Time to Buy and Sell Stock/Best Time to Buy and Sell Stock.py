class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        res = 0
        pre = prices[0]

        for p in prices:
            if p <= pre:
                pre = p
            else:
                if p > pre:
                    res = max(res, p - pre)
        return res

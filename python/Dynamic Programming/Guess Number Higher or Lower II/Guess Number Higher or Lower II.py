class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """

        cache = {}

        def dp(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            else:
                if i >= j:
                    return 0
                res = float("inf")
                for cur in range(i, j + 1):
                    res = min(res, cur + max(dp(i, cur - 1), dp(cur + 1, j)))
                cache[(i, j)] = res
                return res

        return dp(1, n)

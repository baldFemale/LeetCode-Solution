from functools import lru_cache


class Solution(object):
    def minimumMoves(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0

            res = 1 + dp(i, j - 1)
            if arr[j] == arr[j - 1]:
                res = 1 + dp(i, j - 2)

            for k in range(i, j - 1):
                if arr[j] == arr[k]:
                    res = min(res, dp(i, k - 1) + dp(k + 1, j - 1))
            return res

        return dp(0, len(arr) - 1)

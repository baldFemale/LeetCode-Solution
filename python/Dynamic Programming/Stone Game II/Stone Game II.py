class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """

        a = []
        for p in piles[::-1]:
            if not a:
                a.append(p)
            else:
                a.append(p + a[-1])
        a = a[::-1]

        from functools import lru_cache
        @lru_cache(None)
        def dp(i, m):
            if i + 2 * m >= len(piles):
                return a[i]
            else:
                return a[i] - min(dp(i + x, max(m, x)) for x in range(1, 2 * m + 1))

        return dp(0, 1)
tt56
class Solution(object):
    def mergeStones(self, stones, K):
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        """
        N = len(stones)
        prefix = [0 for i in range(N + 1)]
        for i in range(N):
            prefix[i + 1] += (prefix[i] + stones[i])

        inf = float("inf")

        import functools

        @functools.lru_cache(None)
        def dp(i, j, m):
            if (j - i + 1 - m) % (K - 1) != 0:
                return inf
            if i == j:
                return inf if m != 1 else 0
            if m == 1:
                return dp(i, j, K) + prefix[j + 1] - prefix[i]

            return min(dp(i, mid, 1) + dp(mid + 1, j, m - 1) for mid in range(i, j))

        res = dp(0, N - 1, 1)
        return res if res != inf else -1

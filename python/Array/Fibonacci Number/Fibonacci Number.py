class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        cache = {0: 0, 1: 1}

        def helper(n):
            return cache[n] if n in cache else helper(n - 1) + helper(n - 2)

        return helper(N)

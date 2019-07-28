class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {
            0:0,
            1:1,
            2:1
        }

        def helper(n):
            if n in cache:
                return cache[n]
            else:
                cache[n-1] = helper(n-1)
                cache[n-2] = helper(n-2)
                cache[n-3] = helper(n-3)
                cache[n] = cache[n-1]+cache[n-2]+cache[n-3]
                return cache[n]
        return helper(n)

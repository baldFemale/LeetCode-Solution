class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """

        def count(val):
            count = 0
            j = n

            for i in range(1, m + 1):
                while i * j > val:
                    j -= 1
                count += j
            return count >= k

        lo = 0
        high = m * n
        while lo < high:
            mid = (lo + high) // 2
            if count(mid):
                high = mid
            else:
                lo = mid + 1
        return lo

class Solution(object):
    def maximizeSweetness(self, sweetness, K):
        """
        :type sweetness: List[int]
        :type K: int
        :rtype: int
        """

        def check(chunk):
            count = 0
            cur = 0
            for i in sweetness:
                cur += i
                if cur >= chunk:
                    count += 1
                    cur = 0
            return count >= K + 1

        left = 1
        right = sum(sweetness) // (K + 1)

        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return right


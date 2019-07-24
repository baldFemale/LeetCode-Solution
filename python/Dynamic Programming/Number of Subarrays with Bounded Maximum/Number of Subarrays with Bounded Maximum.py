class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """

        dp = [0 for i in range(len(A) + 1)]
        pre = -1

        for i in range(len(A)):
            if A[i] < L:
                dp[i + 1] = dp[i]
            elif A[i] > R:
                pre = i
            else:
                dp[i + 1] = i - pre
        return sum(dp)

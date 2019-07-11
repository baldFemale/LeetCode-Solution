class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        dp = A[0]

        for row in A[1:]:
            temp = [float("inf")] + dp + [float("inf")]
            for i in range(1, len(A) + 1):
                dp[i - 1] = row[i - 1] + min(temp[i - 1:i + 2])
        return min(dp)
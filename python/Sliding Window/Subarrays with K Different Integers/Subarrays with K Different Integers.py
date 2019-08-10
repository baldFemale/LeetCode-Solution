class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        def helper(A, K):
            window = {}
            i = 0
            res = 0
            for j in range(len(A)):
                if A[j] not in window or window[A[j]] == 0:
                    K -= 1
                window[A[j]] = window.get(A[j], 0) + 1

                while K < 0:
                    window[A[i]] -= 1
                    if window[A[i]] == 0:
                        K += 1
                    i += 1
                res += j - i + 1
            return res

        return helper(A, K) - helper(A, K - 1)

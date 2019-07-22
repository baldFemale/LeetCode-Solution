class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0

        for j in range(1, len(A), 2):
            if A[j] % 2 == 1:
                continue
            else:
                while i + 2 < len(A) and A[i] % 2 == 0:
                    i += 2
                A[i], A[j] = A[j], A[i]
                i += 2
        return A

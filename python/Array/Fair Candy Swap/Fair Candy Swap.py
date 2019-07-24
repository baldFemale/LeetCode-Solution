class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sum_A = sum(A)
        sum_B = sum(B)
        A = set(A)
        B = set(B)

        for i in A:
            if ((sum_A + sum_B) // 2 - sum_A) + i in B:
                return [i, ((sum_A + sum_B) // 2 - sum_A) + i]

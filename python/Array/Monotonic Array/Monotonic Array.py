class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        increase = True
        decrease = True

        for i in range(1, len(A)):
            if A[i] - A[i - 1] > 0:
                decrease = False
            if A[i] - A[i - 1] < 0:
                increase = False
        return increase or decrease

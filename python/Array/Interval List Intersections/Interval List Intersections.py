class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        i = 0
        j = 0
        res = []
        while i < len(A) and j < len(B):
            if A[i][-1] < B[j][-1]:
                if A[i][-1] >= max(A[i][0], B[j][0]):
                    res.append([max(A[i][0], B[j][0]), A[i][-1]])
                i += 1
            else:
                if B[j][-1] >= max(A[i][0], B[j][0]):
                    res.append([max(A[i][0], B[j][0]), B[j][-1]])
                j += 1
        return res

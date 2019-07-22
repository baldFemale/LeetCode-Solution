class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        res = -float("inf")
        for j in [1, -1]:
            for k in [1, -1]:
                temp = []
                for i in range(len(arr1)):
                    temp.append(arr1[i] * j + arr2[i] * k + i)
                res = max(res, max(temp) - min(temp))
        return res


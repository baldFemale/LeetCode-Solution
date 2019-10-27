class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(1,1001):
            for j in range(1,1001):
                if customfunction.f(i,j)==z:
                    res.append([i,j])
                elif customfunction.f(i,j)>z:
                    break
            if customfunction.f(i,1)>z:
                break
        return res
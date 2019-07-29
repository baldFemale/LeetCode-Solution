class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[0 for i in range(len(M[0]))] for j in range(len(M))]

        for i in range(len(M)):
            for j in range(len(M[0])):
                count = 0
                temp = 0
                for x in [1, 0, -1]:
                    for y in [1, 0, -1]:
                        if 0 <= i + x < len(M) and 0 <= j + y < len(M[0]):
                            temp += M[i + x][j + y]
                            count += 1
                res[i][j] = temp // count
        return res

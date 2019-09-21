import heapq


class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """

        h = [(mat[i][0], 0, i) for i in range(len(mat))]
        heapq.heapify(h)

        dic = {}
        for i in range(len(mat)):
            dic[mat[i][0]] = dic.get(mat[i][0], 0) + 1
            if dic[mat[i][0]] == len(mat):
                return mat[i][0]

        while h:
            v, index, row = heapq.heappop(h)
            if index == len(mat[0]) - 1:
                return -1
            dic[v] -= 1

            heapq.heappush(h, (mat[row][index + 1], index + 1, row))

            dic[mat[row][index + 1]] = dic.get(mat[row][index + 1], 0) + 1
            if dic[mat[row][index + 1]] == len(mat):
                return mat[row][index + 1]

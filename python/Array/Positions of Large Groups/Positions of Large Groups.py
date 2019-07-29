class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        i = 0
        j = 0
        res = []
        while j < len(S) and i < len(S):
            while j + 1 < len(S) and S[j + 1] == S[j]:
                j += 1
            if j - i + 1 >= 3:
                res.append([i, j])
            i = j + 1
            j = j + 1
        return res

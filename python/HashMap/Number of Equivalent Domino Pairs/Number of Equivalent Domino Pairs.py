class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        dic = {}
        res = 0
        for domin in dominoes:
            domin = (min(domin[0], domin[1]), max(domin[0], domin[1]))

            if domin in dic:
                res += dic[domin]
                dic[domin] += 1
            else:
                dic[domin] = 1
        return res

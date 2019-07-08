class Solution(object):
    def countTriplets(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dic = {}

        for i in A:
            for j in A:
                dic[i & j] = dic.get(i & j, 0) + 1

        res = 0
        for i in A:
            for k in dic:
                if i & k == 0:
                    res += dic[k]
        return res

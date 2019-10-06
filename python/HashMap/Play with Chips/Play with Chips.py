from collections import Counter


class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        c = Counter(chips)

        res = float("inf")
        for k in c.keys():
            temp = 0
            for j in c.keys():
                dis = abs(j - k) % 2
                temp += dis * c[j] * 1
            res = min(res, temp)
        return res

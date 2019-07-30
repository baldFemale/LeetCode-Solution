class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        dic = {}

        for t in time:
            dic[t % 60] = dic.get(t % 60, 0) + 1

        res = 0
        for k, v in dic.items():
            if k == 0 or k == 30:
                res += v * (v - 1)
            else:
                if 60 - k in dic:
                    res += v * dic[60 - k]
        return res // 2

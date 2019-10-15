from collections import defaultdict


class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        dd = defaultdict(dict)
        mod = 10 ** 9 + 7

        for i in range(1, 7):
            dd[i] = {1: 1}

        for i in range(1, n):
            temp = defaultdict(dict)
            for j in range(1, 7):
                s = 0
                for k in range(1, 7):
                    if k != j:
                        s += sum(dd[k].values()) % mod
                    else:
                        for kk in dd[j].keys():
                            if kk + 1 <= rollMax[k - 1]:
                                temp[j][kk + 1] = dd[j][kk] % mod
                temp[j][1] = s
            dd = temp
        res = sum([sum(dd[k].values()) for k in range(1, 7)])
        return res % mod



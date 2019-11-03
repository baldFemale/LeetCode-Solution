from collections import Counter


class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """

        c1 = Counter(s1)
        c2 = Counter(s2)
        dic = {
            "xy": 0,
            "yx": 0,
        }

        if (c1["x"] + c2["x"]) % 2 == 1:
            return -1

        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            else:
                if s1[i] == "x":
                    dic["xy"] += 1
                else:
                    dic["yx"] += 1

        res = 0
        if dic["xy"] % 2 == 0:
            res += dic["xy"] // 2
            res += dic["yx"] // 2

            return res

        else:
            res += dic["xy"] // 2
            res += dic["yx"] // 2
            res += 2
            return res
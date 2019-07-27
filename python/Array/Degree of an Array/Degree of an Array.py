from collections import defaultdict


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = defaultdict(list)

        for i, j in enumerate(nums):
            dic[j].append(i)

        degree = 0
        length = float("inf")
        print(dic)

        for k, v in dic.items():
            print(k, v)
            print(degree, length)
            if len(v) > degree:
                degree = len(v)
                if degree == 1:
                    length = 1
                else:
                    length = v[-1] - v[0] + 1
            elif len(v) == degree and len(v) > 1 and v[-1] - v[0] + 1 <= length:
                length = v[-1] - v[0] + 1

        return length

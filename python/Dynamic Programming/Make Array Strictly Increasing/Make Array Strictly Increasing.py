import bisect
from collections import defaultdict


class Solution:
    def makeArrayIncreasing(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """

        dp = {-1: 0}

        arr2.sort()

        for i in arr1:
            tmp = defaultdict(lambda: float("inf"))

            for k in dp.keys():
                if i > k:
                    tmp[i] = min(tmp[i], dp[k])

                index = bisect.bisect(arr2, k)
                if index < len(arr2):
                    tmp[arr2[index]] = min(tmp[arr2[index]], dp[k] + 1)
            dp = tmp
        if dp:
            return min(dp.values())
        return -1

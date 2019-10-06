from collections import defaultdict


class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        index = defaultdict(list)
        for i, j in enumerate(arr):
            index[j].append(i)

        s = set(arr)

        dp = {i: 1 for i in range(len(arr))}

        for i in range(len(arr)):
            if arr[i] + difference in s:
                for j in index[arr[i] + difference]:
                    if j > i:
                        dp[j] = max(dp[j], dp[i] + 1)
        # print(dp)

        return max(dp.values())



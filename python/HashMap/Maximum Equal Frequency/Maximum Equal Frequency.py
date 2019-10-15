from collections import defaultdict


class Solution(object):
    def maxEqualFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cnt = defaultdict(int)
        freq = defaultdict(int)
        res = 0
        maxF = 0

        for i, j in enumerate(nums):
            cnt[j] += 1
            freq[cnt[j] - 1] -= 1
            freq[cnt[j]] += 1

            maxF = max(maxF, cnt[j])

            if maxF == 1 or maxF * freq[maxF] == i or (maxF - 1) * (freq[maxF - 1] + 1) == i:
                res = max(res, i + 1)
        return res

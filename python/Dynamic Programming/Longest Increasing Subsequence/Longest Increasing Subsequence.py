import bisect


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        res = 0
        for i in nums:
            index = bisect.bisect_left(dp,i)
            if index==len(dp):
                dp.append(i)
                res = max(res,len(dp))
            else:
                dp[index] = i
        return res

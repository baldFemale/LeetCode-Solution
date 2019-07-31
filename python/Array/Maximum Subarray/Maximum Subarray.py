class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = 0
        res = -float("inf")

        for i in nums:
            pre = max(i, pre + i)
            res = max(res, pre)
        return res

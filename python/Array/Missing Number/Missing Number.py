class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = 0
        for i in nums:
            temp ^= i

        for i in range(1, len(nums) + 1):
            temp ^= i

        return temp

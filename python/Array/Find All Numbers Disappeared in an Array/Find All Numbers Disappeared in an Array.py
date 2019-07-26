class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in nums:
            i = abs(i)
            if nums[i - 1] > 0:
                nums[i - 1] *= -1
        print(nums)

        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res

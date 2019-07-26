class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candinate = None

        for i in nums:
            if count == 0:
                candinate = i
            if i == candinate:
                count += 1
            else:
                count -= 1
        return candinate

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        count = 0
        for i in nums:
            if i==1:
                count+=1
            else:
                res = max(count,res)
                count = 0
        return max(res,count)

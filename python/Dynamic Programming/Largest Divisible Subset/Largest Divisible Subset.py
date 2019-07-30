class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        nums.sort()

        dp = [1 for i in range(len(nums))]
        parent = {}
        count = 0
        maxindex = None

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j
                        if dp[i] > count:
                            count = dp[i]
                            maxindex = i

        if not maxindex:
            return [nums[0]]

        res = []
        while maxindex in parent:
            res.append(nums[maxindex])
            maxindex = parent[maxindex]
        res.append(nums[maxindex])
        return res[::-1]

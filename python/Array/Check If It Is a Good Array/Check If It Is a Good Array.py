class Solution(object):
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = list(set(nums))

        def gcd(a, b):
            if a < b:
                a, b = b, a
            while b:
                a, b = b, a % b

            return a

        nums.sort()
        t = nums[0]

        if t == 1:
            return True
        if len(nums) == 1:
            return False

        tt = gcd(nums[0], nums[1])
        for i in range(2, len(nums)):
            tt = gcd(nums[i], tt)
            if tt == 1:
                return True
        return False if tt != 1 else True

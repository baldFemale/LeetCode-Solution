class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            cur = i
            seen = set([i])
            tag = nums[i]
            while tag * nums[(cur + nums[cur]) % len(nums)] > 0 and (cur + nums[cur]) % len(nums) not in seen:
                seen.add((cur + nums[cur]) % len(nums))
                cur = (cur + nums[cur]) % len(nums)
            if tag * nums[(cur + nums[cur]) % len(nums)] > 0 and cur != (cur + nums[cur]) % len(nums):
                return True
            else:
                for i in seen:
                    nums[i] = 0

        return False
